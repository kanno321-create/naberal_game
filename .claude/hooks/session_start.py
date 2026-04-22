#!/usr/bin/env python3
"""
session_start.py — 공용 SessionStart Hook (Layer 1 naberal_harness)

목적: 세션 시작 시 스튜디오 **자동 감사** 실행.
     - SKILL.md 500줄 초과 경고 (Progressive Disclosure 위반)
     - deprecated 패턴 잔존 검사
     - CONFLICT_MAP.md 존재 여부 + 미해결 A급 카운트
     - 결과를 세션 시작 메시지에 컨텍스트로 주입

각 스튜디오가 자기 `.claude/hooks/`에 복사해 사용.
"""
from __future__ import annotations
import json
import sys
import re
from pathlib import Path


def find_studio_root(start: Path) -> Path | None:
    cur = start.resolve()
    for _ in range(10):
        if (cur / ".claude").is_dir():
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent
    return None


def count_long_skills(studio_root: Path, threshold: int = 500) -> list[tuple[str, int]]:
    """SKILL.md 중 threshold 줄 초과 파일 목록."""
    skills_dir = studio_root / ".claude" / "skills"
    if not skills_dir.exists():
        return []
    long_files = []
    for skill_md in skills_dir.rglob("SKILL.md"):
        try:
            line_count = sum(1 for _ in skill_md.open("r", encoding="utf-8", errors="ignore"))
            if line_count > threshold:
                rel = skill_md.relative_to(studio_root)
                long_files.append((str(rel), line_count))
        except Exception:
            pass
    return long_files


def check_conflict_map(studio_root: Path) -> dict:
    """CONFLICT_MAP.md 존재 여부 + A급 미해결 카운트."""
    cm = studio_root / ".planning" / "codebase" / "CONFLICT_MAP.md"
    if not cm.exists():
        return {"exists": False, "a_grade_open": 0}

    try:
        content = cm.read_text(encoding="utf-8", errors="ignore")
        # 간단 휴리스틱: "A-\d+" 패턴 카운트 (A급 충돌 번호)
        a_matches = re.findall(r"A-\d+", content)
        # 🚫 또는 "정답 확정:" 뒤가 비어있으면 미해결로 간주 (단순화)
        return {
            "exists": True,
            "a_grade_total": len(set(a_matches)),
            # 실제 "미해결" 판정은 복잡 — 여기선 총계만
        }
    except Exception:
        return {"exists": True, "a_grade_total": -1}


def summarize_work_handoff(studio_root: Path, max_lines: int = 30) -> str | None:
    """WORK_HANDOFF.md 첫 N줄 요약 (현재 세션 상태 + 박제된 결정사항).

    F-CTX-01 재발 방지 — 세션 시작 시 이전 세션 핸드오프를 자동 주입.
    """
    wh = studio_root / "WORK_HANDOFF.md"
    if not wh.exists():
        return None
    try:
        lines = wh.read_text(encoding="utf-8", errors="ignore").splitlines()[:max_lines]
        return "\n".join(lines)
    except Exception:
        return None


def list_env_keys(studio_root: Path) -> list[str]:
    """`.env` 에 저장된 key 이름 목록 (값은 마스킹, 이름만 노출).

    F-CTX-01 재발 방지: API key 재질문 절대 금지 근거 자료.
    """
    env = studio_root / ".env"
    if not env.exists():
        return []
    try:
        keys = []
        for line in env.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key_name = line.split("=", 1)[0].strip()
            if key_name:
                keys.append(key_name)
        return keys
    except Exception:
        return []


def load_memory_index(studio_root: Path) -> str | None:
    """`.claude/memory/MEMORY.md` 인덱스 전체 로드.

    auto memory 규약: MEMORY.md 는 200줄 이내 index 전용.
    """
    idx = studio_root / ".claude" / "memory" / "MEMORY.md"
    if not idx.exists():
        return None
    try:
        return idx.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None


def sync_global_to_local_memory(studio_root: Path) -> dict:
    """Claude Code 전역 auto-memory → 프로젝트 로컬 `.claude/memory/` 자동 동기화.

    영속성 앵커 #3-bis (FAIL-017 해결) — Claude Code 가 전역 경로에만 자동 저장하는
    새 메모리를 세션 시작 시 로컬로 복사해 git 박제 대상에 포함시킨다.

    **이중 박제 원칙** (feedback_dual_persistence_required.md) 자동 집행.

    동작:
    - 단방향: 전역 → 로컬 (로컬 → 전역은 수동)
    - Idempotent: 내용 동일하면 touch 안 함 (git 노이즈 방지)
    - mtime 비교: 전역이 더 최근이거나 로컬에 없으면 복사
    - 로컬-only 파일 보존: 전역에 없는 로컬 파일은 건드리지 않음

    전역 경로 규칙 (Claude Code): `~/.claude/projects/<encoded-cwd>/memory/`
    - encoded-cwd 는 cwd 를 인코딩 (슬래시·콜론 → 하이픈).

    반환: {'copied': [...], 'unchanged': [...], 'skipped_newer_local': [...]}
    도입: FAIL-017 재발 방지 (2026-04-24 세션 #8 진입).
    """
    import os

    local_dir = studio_root / ".claude" / "memory"
    if not local_dir.exists():
        local_dir.mkdir(parents=True, exist_ok=True)

    # Claude Code 전역 경로 계산: ~/.claude/projects/<encoded-cwd>/memory/
    # Claude Code 인코딩 규칙 (실측 기반):
    # - 콜론(:) → 하이픈(-)
    # - 슬래시(/·\\) → 하이픈(-)
    # - 언더스코어(_) → 하이픈(-)  ⚠️ Claude Code 고유 규칙
    # 예: c:\Users\PC\Desktop\naberal_group\studios\game
    #  → c--Users-PC-Desktop-naberal-group-studios-game
    home = Path(os.environ.get("USERPROFILE") or os.environ.get("HOME") or "~").expanduser()
    cwd_str = (
        str(studio_root)
        .replace("\\", "/")
        .replace("/", "-")
        .replace(":", "-")
        .replace("_", "-")
    )
    global_dir = home / ".claude" / "projects" / cwd_str / "memory"

    result = {
        "copied": [],
        "unchanged": [],
        "skipped_newer_local": [],
        "global_exists": global_dir.exists(),
        "global_path": str(global_dir),
    }

    if not global_dir.exists():
        return result

    import shutil
    for global_md in global_dir.glob("*.md"):
        local_md = local_dir / global_md.name
        try:
            if not local_md.exists():
                shutil.copy2(global_md, local_md)
                result["copied"].append(global_md.name)
                continue
            # 내용 비교 (동일하면 skip)
            if global_md.read_bytes() == local_md.read_bytes():
                result["unchanged"].append(global_md.name)
                continue
            # mtime 비교: 전역이 더 최근이면 덮어씀
            if global_md.stat().st_mtime > local_md.stat().st_mtime:
                shutil.copy2(global_md, local_md)
                result["copied"].append(global_md.name)
            else:
                result["skipped_newer_local"].append(global_md.name)
        except Exception:
            pass

    return result


def load_critical_memories(studio_root: Path) -> str | None:
    """`priority: critical` 마커 있는 메모리 전체 로드.

    MEMORY.md 인덱스만으로는 부족한 최상위 Canon (나이트 Canon · 샘플링 금지 등)
    전체 주입. 세션 간 영속성 앵커 #3 — 샘플링 독서로 놓친 확정 사항이 재발하지
    않도록 매 세션 전체 내용 주입.

    도입: FAIL-016 재발 방지 (2026-04-23 세션 #7).
    """
    memory_dir = studio_root / ".claude" / "memory"
    if not memory_dir.exists():
        return None
    critical_contents = []
    for md in sorted(memory_dir.glob("*.md")):
        if md.name == "MEMORY.md":
            continue
        try:
            content = md.read_text(encoding="utf-8", errors="ignore")
            if content.startswith("---"):
                fm_end = content.find("---", 3)
                if fm_end > 0:
                    frontmatter = content[:fm_end]
                    if "priority: critical" in frontmatter:
                        critical_contents.append(
                            f"#### `{md.name}`\n\n{content}\n"
                        )
        except Exception:
            pass
    return "\n".join(critical_contents) if critical_contents else None


def check_obsidian_vault(studio_root: Path) -> dict:
    """Obsidian vault 건강 체크 — wiki/ 가 Obsidian vault 로 정상 작동하는지.

    영속성 앵커 #2 (Hook 강제). 세션마다 자동 검증되어 "설정이 풀렸을 때"
    즉시 감지됨. 체크 항목:
    - wiki/.obsidian/ 의 필수 설정 3종 (app.json, core-plugins.json, graph.json)
    - wiki/MOC.md (루트 허브) 존재
    - build_backlinks.py 스크립트 존재
    - 자동 백링크 적용 비율 (auto-generated-related 마커 있는 파일 / 전체 wiki .md)
    """
    wiki = studio_root / "wiki"
    if not wiki.exists():
        return {"applicable": False, "reason": "wiki/ 없음 (스튜디오가 wiki tier 미사용)"}

    obsidian = wiki / ".obsidian"
    required_configs = ["app.json", "core-plugins.json", "graph.json"]
    missing_configs = [c for c in required_configs if not (obsidian / c).exists()]

    wiki_moc = (wiki / "MOC.md").exists()
    builder = (studio_root / "scripts" / "obsidian" / "build_backlinks.py").exists()

    # 자동 백링크 적용 비율 (빠른 샘플링)
    total_md = 0
    with_marker = 0
    for md in wiki.rglob("*.md"):
        if ".obsidian" in md.parts:
            continue
        total_md += 1
        try:
            # 파일 끝 2KB 만 읽어 마커 존재 확인 (빠름)
            with md.open("rb") as f:
                f.seek(0, 2)
                size = f.tell()
                f.seek(max(0, size - 2048))
                tail = f.read().decode("utf-8", errors="ignore")
                if "auto-generated-related:start" in tail:
                    with_marker += 1
        except Exception:
            pass

    coverage_pct = (with_marker / total_md * 100) if total_md else 0

    return {
        "applicable": True,
        "obsidian_configs_missing": missing_configs,
        "wiki_moc_exists": wiki_moc,
        "builder_exists": builder,
        "total_md": total_md,
        "with_backlink_marker": with_marker,
        "coverage_pct": round(coverage_pct, 1),
    }


def check_navigator_coverage(studio_root: Path) -> dict:
    """Navigator coverage 검증 — scripts/validate/navigator_coverage.py 호출.

    CLAUDE.md Navigator 매트릭스가 .claude/agents/ + .claude/skills/ 전수를
    커버하는지 확인. 누락 자산이 있으면 warning (block 아님, 파이프라인 중단 금지).
    """
    script = studio_root / "scripts" / "validate" / "navigator_coverage.py"
    if not script.exists():
        return {"available": False}
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, str(script), "--warn-only"],
            cwd=str(studio_root),
            capture_output=True,
            text=True,
            timeout=15,
            encoding="utf-8",
            errors="ignore",
        )
        return {
            "available": True,
            "stdout": (result.stdout or "").strip(),
            "stderr": (result.stderr or "").strip(),
            "returncode": result.returncode,
        }
    except Exception as e:
        return {"available": True, "error": str(e)}


def scan_deprecated_patterns(studio_root: Path) -> list[str]:
    """deprecated_patterns.json에 정의된 패턴이 스튜디오 내 어느 파일에 잔존하는지."""
    config = studio_root / ".claude" / "deprecated_patterns.json"
    if not config.exists():
        return []
    try:
        data = json.loads(config.read_text(encoding="utf-8"))
        patterns = data.get("patterns", [])
    except Exception:
        return []

    found = []
    # .claude, scripts, config, longform, src 스캔 (비용 고려)
    scan_dirs = [
        studio_root / ".claude",
        studio_root / "scripts",
        studio_root / "config",
    ]
    for p in patterns:
        regex = p.get("regex", "")
        reason = p.get("reason", "")
        if not regex:
            continue
        try:
            rx = re.compile(regex, re.MULTILINE)
        except re.error:
            continue
        for scan_dir in scan_dirs:
            if not scan_dir.exists():
                continue
            for f in scan_dir.rglob("*"):
                if not f.is_file():
                    continue
                if f.suffix in (".pyc", ".jsonl", ".log"):
                    continue
                try:
                    txt = f.read_text(encoding="utf-8", errors="ignore")
                    if rx.search(txt):
                        rel = f.relative_to(studio_root)
                        found.append(f"{rel}: {reason}")
                        break  # 한 파일당 한 번만 보고
                except Exception:
                    pass
    return found


def main() -> int:
    try:
        _ = sys.stdin.read()  # SessionStart는 보통 input 없음
    except Exception:
        pass

    studio_root = find_studio_root(Path.cwd())
    if studio_root is None:
        # 스튜디오 밖 세션 — 감사 없이 통과
        print(json.dumps({"context": ""}))
        return 0

    lines = []
    lines.append(f"### 🧰 naberal_harness 세션 감사 — {studio_root.name}")
    lines.append("")

    # 1. CONFLICT_MAP 체크
    cm = check_conflict_map(studio_root)
    if cm["exists"]:
        total = cm.get("a_grade_total", 0)
        if total > 0:
            lines.append(f"⚠️ CONFLICT_MAP.md에 A급 충돌 {total}건 기록됨. 진행 전 확인.")
        else:
            lines.append("✅ CONFLICT_MAP.md 존재, A급 충돌 없음.")
    else:
        lines.append("ℹ️ CONFLICT_MAP.md 없음 (신규 스튜디오 정상).")

    # 2. SKILL.md 500줄 리밋
    long_skills = count_long_skills(studio_root, threshold=500)
    if long_skills:
        lines.append(f"⚠️ SKILL.md 500줄 초과 {len(long_skills)}건 (Lost-in-the-Middle 위험):")
        for path, n in long_skills[:5]:
            lines.append(f"   - {path}: {n}줄")
        if len(long_skills) > 5:
            lines.append(f"   ... 외 {len(long_skills) - 5}개")
        lines.append("   → references/ 분리 권장.")
    else:
        lines.append("✅ 모든 SKILL.md 500줄 이내.")

    # 3. Deprecated 패턴 스캔
    found = scan_deprecated_patterns(studio_root)
    if found:
        lines.append(f"🔴 Deprecated 패턴 잔존 {len(found)}곳:")
        for item in found[:5]:
            lines.append(f"   - {item}")
        if len(found) > 5:
            lines.append(f"   ... 외 {len(found) - 5}건")
    else:
        lines.append("✅ Deprecated 패턴 잔존 없음.")

    # 4. WORK_HANDOFF.md 첫 30줄 요약 (F-CTX-01 재발 방지)
    lines.append("")
    lines.append("### 📋 이전 세션 핸드오프 (WORK_HANDOFF.md 첫 30줄)")
    handoff_summary = summarize_work_handoff(studio_root, max_lines=30)
    if handoff_summary:
        lines.append("```")
        lines.append(handoff_summary)
        lines.append("```")
    else:
        lines.append("ℹ️ WORK_HANDOFF.md 없음 (신규 스튜디오 정상).")

    # 5. .env API key 이름 목록 (값 마스킹, F-CTX-01 재발 방지)
    lines.append("")
    lines.append("### 🔑 API Keys available in .env (값은 환경변수로만 접근, 재질문 금지)")
    env_keys = list_env_keys(studio_root)
    if env_keys:
        lines.append(f"**대표님께 API key 를 다시 묻지 말 것.** 다음 {len(env_keys)}개 key 가 이미 저장돼 있다:")
        for k in env_keys:
            lines.append(f"- `{k}`")
        lines.append("")
        lines.append("참조: `.claude/memory/reference_api_keys_location.md` (용도 매핑)")
    else:
        lines.append("⚠️ .env 파일 없음 또는 비어있음 — `.env.example` 을 복사해 값 채우기 필요.")

    # 6. 로컬 메모리 인덱스 전체 주입 (auto memory 규약)
    lines.append("")
    lines.append("### 🧠 Local Memory Index (.claude/memory/MEMORY.md)")
    memory_idx = load_memory_index(studio_root)
    if memory_idx:
        lines.append(memory_idx)
    else:
        lines.append("ℹ️ `.claude/memory/MEMORY.md` 없음 — 메모리 시스템 미초기화 (신규 스튜디오).")

    # 6.5 Critical memories 전체 주입 (priority: critical 마커 · FAIL-016 재발 방지 · 세션 #7 도입)
    # 선행: 전역 → 로컬 동기화 (FAIL-017 재발 방지 · 세션 #8 추가 · 이중 박제 원칙)
    sync_result = sync_global_to_local_memory(studio_root)
    lines.append("")
    lines.append("### 🔁 Memory Dual-Persistence Sync (전역 auto-memory → 로컬 git)")
    if not sync_result.get("global_exists"):
        lines.append(
            f"ℹ️ Claude Code 전역 auto-memory 경로 없음 (신규 PC / 첫 세션 정상). "
            f"기대 경로: `{sync_result.get('global_path', '?')}`"
        )
    else:
        copied = sync_result.get("copied", [])
        unchanged = sync_result.get("unchanged", [])
        skipped = sync_result.get("skipped_newer_local", [])
        total = len(copied) + len(unchanged) + len(skipped)
        if copied:
            lines.append(f"📥 전역 → 로컬 복사 {len(copied)}건 (git commit 대상 자동 추가):")
            for name in copied[:5]:
                lines.append(f"   - {name}")
            if len(copied) > 5:
                lines.append(f"   ... 외 {len(copied) - 5}건")
        if skipped:
            lines.append(f"⚠️ 로컬이 더 최근 {len(skipped)}건 (전역 수동 동기화 필요 가능):")
            for name in skipped[:3]:
                lines.append(f"   - {name}")
        lines.append(f"✅ Sync 완료: 복사 {len(copied)} / 동일 {len(unchanged)} / 로컬 최신 {len(skipped)} (총 {total})")

    lines.append("")
    lines.append("### 🔒 Critical Memories (priority: critical · 전체 내용 자동 주입)")
    lines.append("> 이 메모리들은 대표님 반복 지적 사항이라 **전체 내용** 주입됨. 세션 중 반드시 준수.")
    critical = load_critical_memories(studio_root)
    if critical:
        lines.append("")
        lines.append(critical)
    else:
        lines.append("ℹ️ Critical memory 없음 (priority: critical 마커 메모리 미존재).")

    # 6c. Obsidian vault 건강 체크 — 3층 시너지(하네스+wiki+Obsidian) 영속성 앵커
    lines.append("")
    lines.append("### 🕸️ Obsidian Vault 건강 (하네스+wiki+Obsidian 3층 시너지)")
    ob = check_obsidian_vault(studio_root)
    if not ob.get("applicable"):
        lines.append(f"ℹ️ {ob.get('reason', 'wiki tier 미사용')}")
    else:
        missing = ob.get("obsidian_configs_missing", [])
        if missing:
            lines.append(
                f"🔴 **Obsidian vault 설정 누락**: `wiki/.obsidian/` 에 {missing} 없음. "
                f"대표님이 그래프뷰·백링크 사용 불가. 즉시 복구 필요."
            )
        else:
            lines.append("✅ Obsidian vault 설정 3종 (app.json · core-plugins.json · graph.json) 정상.")

        if not ob.get("wiki_moc_exists"):
            lines.append("🔴 `wiki/MOC.md` (루트 허브) 없음 — vault 진입점 상실.")
        else:
            lines.append("✅ `wiki/MOC.md` 루트 허브 존재.")

        if not ob.get("builder_exists"):
            lines.append("🔴 `scripts/obsidian/build_backlinks.py` 없음 — 자동 백링크 빌더 상실.")
        else:
            pct = ob.get("coverage_pct", 0)
            total = ob.get("total_md", 0)
            marked = ob.get("with_backlink_marker", 0)
            if pct >= 85:
                lines.append(f"✅ 자동 백링크 커버리지 {pct}% ({marked}/{total} 파일). 정상.")
            elif pct >= 50:
                lines.append(
                    f"⚠️ 자동 백링크 커버리지 {pct}% ({marked}/{total}). "
                    f"`python scripts/obsidian/build_backlinks.py` 재실행 권장."
                )
            else:
                lines.append(
                    f"🔴 자동 백링크 커버리지 {pct}% ({marked}/{total}) — 대량 고립 노드. "
                    f"`python scripts/obsidian/build_backlinks.py` 즉시 실행 필요."
                )

    # 6b. Navigator coverage check — 구현된 자산이 CLAUDE.md 에 등록됐는지 확인
    # (warning only, 파이프라인 차단 금지 — 하네스 Hook 원칙 "Fail Loud, Not Silent" 의
    #  균형: 검증은 strict 하지만 Hook 자체는 파이프라인 중단 금지)
    lines.append("")
    lines.append("### 🗺️ Navigator Coverage (CLAUDE.md 네비게이터 ↔ 구현 자산 동기화)")
    nav = check_navigator_coverage(studio_root)
    if not nav.get("available"):
        lines.append("ℹ️ `scripts/validate/navigator_coverage.py` 미설치 — Navigator 검증 건너뜀.")
    elif nav.get("error"):
        lines.append(f"⚠️ Navigator 검증 실행 실패: {nav['error']}")
    else:
        stdout = nav.get("stdout") or ""
        stderr = nav.get("stderr") or ""
        if nav.get("returncode") == 0 and "OK" in stdout:
            # 마지막 'total: N/M covered' 줄만 표시
            summary = next(
                (line for line in stdout.splitlines() if "total:" in line),
                "✅ Navigator 전수 커버",
            )
            lines.append(f"✅ {summary.replace('[navigator-coverage] ', '')}")
        else:
            lines.append("⚠️ Navigator 커버리지 누락 자산 존재 (CLAUDE.md 매트릭스에 등록 필요):")
            for line in (stdout + "\n" + stderr).splitlines():
                if line.strip() and not line.startswith("[navigator-coverage]"):
                    lines.append(f"   {line}")

    context_text = "\n".join(lines)

    # Claude Code SessionStart hook은 context를 반환하여 시스템 메시지로 주입
    print(json.dumps({"context": context_text}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
