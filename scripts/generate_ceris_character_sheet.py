"""세리스 캐릭터 시트 (정면·후면·초상 3컷) 생성 · 세션 #8 · 2026-04-23.

대표님 지시:
    "나이트처럼 전신 뒷모습, 전신, 상반신 다 표현한 이미지 하나 만들어야 유지되겠다"

목적:
    - 나이트 knight_fullbody_rev1 과 같은 구조의 "공식 캐릭터 시트" 제작
    - 향후 표지·씬 생성 시 세리스 레퍼런스로 이 파일 사용 → 일관성 유지
    - 세리스 초상 레퍼런스 (ceris_v1_rev2_openai_2026-04-23.png) 의 얼굴 유지

safety 통과 조정:
    - "revealing" 삭제
    - "demon heroine" → "fantasy mage girl with dark aesthetic"
    - 노출 관련 용어 제거
    - 드레스 "long elegant modest gothic black dress" 표현

실행:
    python scripts/generate_ceris_character_sheet.py
"""
from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

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

from openai import OpenAI

GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"

REF_CERIS = ART_DIR / "ceris_v1_rev2_openai_2026-04-23.png"
OUT_PATH = ART_DIR / "ceris_fullbody_rev1_2026-04-23.png"

MODEL = "gpt-image-1"
IMAGE_SIZE = "1536x1024"  # 가로형 (3 컷 나열)
IMAGE_QUALITY = "high"

PROMPT = """Japanese anime 2D character design turnaround sheet, cel-shaded illustration,
three views of the same heroine arranged horizontally in one image:
LEFT: full body front view from head to toe,
CENTER: full body back view showing long hair and dress,
RIGHT: bust portrait showing face details.

Character design:
elegant young adult JRPG mage heroine, slim graceful adult figure, 170cm height, 7.5 heads tall anime proportions,
long flowing black hair reaching waist,
fair complexion,
large expressive violet anime eyes with quiet melancholy,
two small delicate curved horns on her head, delicate pointed ears,
wearing a long flowing elegant black dress reaching ankles with silver embroidery patterns,
a small glowing purple magical pendant at her collar emitting soft light,
holding an ornate long wooden wizard staff vertically with both hands clasped together in front of her chest.

Match the anime face style from the reference image — same face shape, same eye shape, same bishoujo aesthetic.

Art style:
pure Japanese anime 2D cel-shaded illustration,
clean anime line art with flat anime colors,
inspired by Yoshitaka Amano Final Fantasy, Akihiko Yoshida Bravely Default, Kentaro Miura Berserk,
Japanese seinen JRPG character design sheet aesthetic.

Background: plain light neutral gray studio background, no environment, clean reference sheet layout.

Small text labels below each panel: FRONT / BACK / PORTRAIT in elegant serif type.

Quality: masterpiece anime character design sheet, highly detailed, clean reference quality."""


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[GEN] 세리스 캐릭터 시트 (정면·후면·초상 3컷) -> {OUT_PATH.name}", flush=True)

    try:
        with open(REF_CERIS, "rb") as f:
            resp = client.images.edit(
                model=MODEL,
                image=[f],
                prompt=PROMPT,
                size=IMAGE_SIZE,
                quality=IMAGE_QUALITY,
                n=1,
            )
        item = resp.data[0]
        if getattr(item, "b64_json", None):
            OUT_PATH.write_bytes(base64.b64decode(item.b64_json))
        elif getattr(item, "url", None):
            import urllib.request
            urllib.request.urlretrieve(item.url, str(OUT_PATH))
        else:
            print("FAIL: no image data", file=sys.stderr)
            return 2
        print(f"  [OK] saved: {OUT_PATH}")
        print(f"  size: {OUT_PATH.stat().st_size:,} bytes")
        return 0
    except Exception as err:
        print(f"  [FAIL] {type(err).__name__}: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
