"""세리스 (마족 히로인) 초상 생성 — Nano Banana Pro 호출 (세션 #7 · 2026-04-23).

대표님 지시:
    버전 1: 파멸의 룬어를 다루는 진지한 세리스 (나이트 원화 스타일 맞춤)
    버전 2: 부끄러워하는 세리스 (갭 모에 · 나이트 원화 스타일 유지)

세리스 Canon (케릭 컨셉 및 프로필.md · 2026-04-23):
    - 마족 히로인 · 마법 폭격기 · 파멸의 룬어
    - 창백할 정도로 하얀 피부 + 칠흑 같은 뿔 (프로필 원문 · 이번 프롬프트에선 뿔 제거 옵션)
    - 매혹적인 보랏빛 눈 · 노출 있지만 기품 있는 검은 드레스
    - 흉부 빛나는 마력 핵 (Core)
    - 갭 모에: 요염하게 유혹하다가 진심에 새빨개짐

실행:
    python scripts/generate_ceris_portrait.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# --- .env 로드 (shorts .env 에서 API 키 확보) ---
SHORTS_ENV = Path(r"C:\Users\PC\Desktop\naberal_group\studios\shorts\.env")
if SHORTS_ENV.exists():
    for line in SHORTS_ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and v and k not in os.environ:
            os.environ[k] = v

# --- shorts NanoBananaAdapter 임포트 ---
SHORTS_SCRIPTS = Path(r"C:\Users\PC\Desktop\naberal_group\studios\shorts\scripts")
sys.path.insert(0, str(SHORTS_SCRIPTS))
from orchestrator.api.nanobanana import NanoBananaAdapter  # noqa: E402

# --- 출력 디렉토리 ---
GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"
ART_DIR.mkdir(parents=True, exist_ok=True)

# --- 프롬프트 v1: 파멸의 룬어 세리스 (나이트 원화 스타일 맞춤) ---
PROMPT_V1_SERIOUS = """(masterpiece, best quality, official game concept art:1.2),
1girl, dark fantasy demon heroine,
extremely pale translucent skin,
glowing deep violet eyes with a hint of melancholy,
wearing an elegant but revealing gothic black dress with intricate silver embroidery,
(a glowing magical gemstone core embedded in the skin of her chest emitting soft purple light:1.3),
ancient blood-red runes floating,
long flowing dark hair,
muted colors, desaturated palette,
painterly anime style, JRPG character design,
watercolor and ink texture, detailed brush strokes,
somber and mysterious atmosphere,
in the style of dark fantasy concept art"""

# --- 프롬프트 v2: 부끄러워하는 세리스 (갭 모에 · 나이트 원화 스타일 유지) ---
PROMPT_V2_BLUSH = """(masterpiece, best quality, official game concept art:1.2),
1girl, dark fantasy demon heroine,
extremely pale skin,
beautiful violet eyes,
long dark hair,
wearing an elegant revealing black dress,
(glowing magical gemstone core on her chest:1.2),
looking at viewer with a shy expression,
intensely blushing cheeks, flustered and embarrassed,
holding her hands together nervously,
muted colors, desaturated palette,
painterly anime style, JRPG character design,
watercolor and ink texture, detailed brush strokes,
somber yet charming atmosphere,
dark fantasy concept art"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found in environment or shorts .env", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)

    jobs = [
        (
            "ceris_v1_nano_banana_2026-04-23.png",
            PROMPT_V1_SERIOUS,
            "버전 1 · 파멸의 룬어 진지",
        ),
        (
            "ceris_v2_nano_banana_2026-04-23.png",
            PROMPT_V2_BLUSH,
            "버전 2 · 부끄러워하는 갭 모에",
        ),
    ]

    results = []
    for filename, prompt, label in jobs:
        out_path = ART_DIR / filename
        print(f"[GEN] {label} -> {filename}", flush=True)
        try:
            saved = adapter.generate_scene(prompt=prompt, output_path=out_path)
            print(f"  [OK] saved: {saved}", flush=True)
            results.append((label, str(saved), "OK"))
        except Exception as err:
            print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
            results.append((label, str(out_path), f"FAIL: {err}"))

    print("\n=== SUMMARY ===")
    for label, path, status in results:
        print(f"  [{status}] {label} -- {path}")

    return 0 if all(r[2] == "OK" for r in results) else 2


if __name__ == "__main__":
    sys.exit(main())
