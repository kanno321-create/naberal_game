#!/usr/bin/env python3
"""
gpt_image_seris.py — OpenAI gpt-image-1 으로 마족 히로인 세리스 초안 2종 생성

세션 #7 · 2026-04-23 · 대표님 요청
- 버전 1: 파멸의 룬어를 다루는 세리스 (다크 판타지 · 뿔 제거)
- 버전 2: 부끄러워하는 세리스 (갭 모에 · 뿔 제거)

API 키 출처: shorts 스튜디오 .env (OPENAI_API_KEY)
저장 위치: wiki/design/art/reference/characters/seris/
"""
from __future__ import annotations

import base64
import json
import os
import sys
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError

# ---------------------------------------------------------------------
# API 키 로드 (shorts 스튜디오 .env)
# ---------------------------------------------------------------------
SHORTS_ENV = Path(r"C:\Users\PC\Desktop\naberal_group\studios\shorts\.env")


def load_openai_key() -> str:
    if not SHORTS_ENV.exists():
        raise SystemExit(f"shorts .env 없음: {SHORTS_ENV}")
    for line in SHORTS_ENV.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("OPENAI_API_KEY="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            return value
    raise SystemExit("OPENAI_API_KEY 미발견")


# ---------------------------------------------------------------------
# 프롬프트 2종 (대표님 지정 · 원문 보존)
# ---------------------------------------------------------------------
PROMPTS = {
    "seris_v1_dark_fantasy": (
        "(masterpiece, best quality, official game concept art:1.2), 1girl, dark "
        "fantasy demon heroine, extremely pale translucent skin, glowing deep violet "
        "eyes with a hint of melancholy, wearing an elegant but revealing gothic "
        "black dress with intricate silver embroidery, (a glowing magical gemstone "
        "core embedded in the skin of her chest emitting soft purple light:1.3), "
        "ancient blood-red runes floating, long flowing dark hair, muted colors, "
        "desaturated palette, painterly anime style, JRPG character design, "
        "watercolor and ink texture, detailed brush strokes, somber and mysterious "
        "atmosphere, in the style of dark fantasy concept art."
    ),
    "seris_v2_shy_blushing": (
        "(masterpiece, best quality, official game concept art:1.2), 1girl, dark "
        "fantasy demon heroine, extremely pale skin, beautiful violet eyes, long "
        "dark hair, wearing an elegant revealing black dress, (glowing magical "
        "gemstone core on her chest:1.2), looking at viewer with a shy expression, "
        "intensely blushing cheeks, flustered and embarrassed, holding her hands "
        "together nervously, muted colors, desaturated palette, painterly anime "
        "style, JRPG character design, watercolor and ink texture, detailed brush "
        "strokes, somber yet charming atmosphere, dark fantasy concept art."
    ),
}


# ---------------------------------------------------------------------
# OpenAI gpt-image-1 호출
# ---------------------------------------------------------------------
API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
SIZE = "1024x1536"  # 캐릭터 초상용 세로 비율


def generate_image(api_key: str, prompt: str) -> bytes:
    """gpt-image-1 호출 → PNG 바이트 반환."""
    payload = json.dumps(
        {
            "model": MODEL,
            "prompt": prompt,
            "n": 1,
            "size": SIZE,
            "quality": "high",  # gpt-image-1: low / medium / high / auto
        }
    ).encode("utf-8")

    req = urlrequest.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlrequest.urlopen(req, timeout=180) as resp:
            body = resp.read()
    except HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        raise SystemExit(f"HTTP {e.code} · {err_body}") from e
    except URLError as e:
        raise SystemExit(f"네트워크 오류: {e}") from e

    data = json.loads(body)
    if "data" not in data or not data["data"]:
        raise SystemExit(f"응답 이상: {data}")

    item = data["data"][0]
    if "b64_json" in item:
        return base64.b64decode(item["b64_json"])
    if "url" in item:
        with urlrequest.urlopen(item["url"], timeout=60) as img_resp:
            return img_resp.read()
    raise SystemExit(f"이미지 데이터 없음: {item}")


# ---------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------
def main() -> int:
    api_key = load_openai_key()
    print(f"[gpt-image-1] API key loaded · ...{api_key[-6:]}")
    print(f"[gpt-image-1] size={SIZE} · quality=high · n=2 prompts")

    out_dir = Path(__file__).resolve().parents[2] / "wiki" / "design" / "art" / "reference" / "characters" / "seris"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[gpt-image-1] output dir: {out_dir}")

    for name, prompt in PROMPTS.items():
        print(f"\n[gpt-image-1] generating · {name} ...")
        try:
            png_bytes = generate_image(api_key, prompt)
        except SystemExit as e:
            print(f"[gpt-image-1] FAIL · {name}: {e}")
            continue

        out_path = out_dir / f"{name}.png"
        out_path.write_bytes(png_bytes)
        size_kb = len(png_bytes) / 1024
        print(f"[gpt-image-1] saved · {out_path} ({size_kb:.1f} KB)")

    # 메모 문서 동반 생성
    memo_path = out_dir / "_generation_memo.md"
    memo_path.write_text(
        "---\n"
        "title: 세리스(마족 히로인) 초안 이미지 생성 메모\n"
        "created: 2026-04-23\n"
        "session: \"#7\"\n"
        "model: gpt-image-1\n"
        f"size: {SIZE}\n"
        "quality: high\n"
        "---\n\n"
        "# 세리스 초안 이미지 생성 · 2026-04-23 세션 #7\n\n"
        "## 생성 배경\n"
        "- 대표님 프롬프트 2종 제시 (v1 다크 판타지 · v2 갭 모에 부끄러워함)\n"
        "- API 출처: shorts 스튜디오 .env OPENAI_API_KEY\n"
        "- 모델: OpenAI gpt-image-1 (2025-04 출시)\n\n"
        "## 생성 결과\n\n"
        "### v1 · 파멸의 룬어 세리스 (다크 판타지 · 뿔 제거)\n"
        "- 파일: `seris_v1_dark_fantasy.png`\n"
        "- 특성: 핵심은 **흉부 마력 핵 (피부 박힌 보석형 코어 · 보라빛)** · Q-CORE 1 마족 "
        "선천 생명체 정합 · a-47-C 의지결 메커니즘 반영\n\n"
        "### v2 · 부끄러워하는 세리스 (갭 모에 · 뿔 제거)\n"
        "- 파일: `seris_v2_shy_blushing.png`\n"
        "- 특성: 썸·애간장 정서 구현 · a-15 로맨스 비대칭 화합 루트 정합\n\n"
        "## 후속 작업\n"
        "- 대표님 초안 검토 → 컨셉 확정 → Ch.11 첫 조우 · Ch.14 룬어 각성 씬 삽화 기반\n"
        "- 이름 확정 시 파일명 rename\n"
        "- 표준 캐릭터 시트 생성 (정면·측면·후면 · 감정 변주 4종 · 무장 포즈)\n",
        encoding="utf-8",
    )
    print(f"\n[gpt-image-1] memo: {memo_path}")
    print("\n✅ 생성 완료")
    return 0


if __name__ == "__main__":
    sys.exit(main())
