"""세리스 캐릭터 시트 (정면·후면·초상 3컷) · reference 없이 generate (세션 #8 · 2026-04-23).

대표님 요구:
    "ceris_v1_rev2_openai_2026-04-23.png · ceris_v2_openai_2026-04-23.png
     이 모습들을 절대 놓치면 안 되 반드시 이 모습의 일관성을 100% 유지"

문제:
    gpt-image-1 images.edit 호출 시 reference image 의 어깨 노출·horns·검은 드레스 조합이
    OpenAI moderation 시스템에 지속 차단됨 (req_26b2b9, req_652dbf, req_3cda3c).

접근:
    reference 없이 images.generate 로 텍스트 프롬프트만 사용 →
    케릭 컨셉 및 프로필.md 의 세리스 외형 정확 묘사 +
    기존 v1 rev2·v2 프롬프트 키워드 그대로 재현 →
    비슷한 얼굴·스타일 유도.

실행:
    python scripts/generate_ceris_character_sheet_v2.py
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
OUT_PATH = ART_DIR / "ceris_fullbody_rev1_2026-04-23.png"

MODEL = "gpt-image-1"
IMAGE_SIZE = "1536x1024"
IMAGE_QUALITY = "high"

# 세리스 기존 v1 rev2 프롬프트 키워드 최대한 보존 + 3-view 추가
PROMPT = """(masterpiece, best quality, official game concept art:1.2),
Japanese anime character design turnaround sheet of one heroine, three full views arranged horizontally:
LEFT panel: full body front view from head to toe,
CENTER panel: full body back view,
RIGHT panel: bust portrait close-up.

Heroine design (consistent across all three views):
1girl, JRPG fantasy mage,
pale porcelain skin with gentle warmth, softly luminous complexion, delicate but alive,
glowing deep violet eyes with a hint of melancholy,
long flowing black hair reaching waist,
two small curved horns on her head, delicate pointed ears,
wearing an elegant flowing black dress with intricate silver embroidery reaching ankles,
a subtle glowing magical gemstone pendant on her collar emitting soft purple light,
holding an ornate long wooden wizard staff vertically with both hands clasped in front of her chest,
tall slim adult figure, 7.5 heads tall anime proportions,
quiet resigned expression with gentle melancholy.

Style:
painterly anime illustration, JRPG character design,
watercolor and ink texture, detailed brush strokes,
dark fantasy concept art aesthetic,
muted colors, desaturated palette,
somber and mysterious atmosphere,
in the exact style of the game cover art for NIGHTMARE.

Layout:
three views in one clean sheet,
plain light neutral gray background, no environment,
small elegant serif labels under each panel: FRONT · BACK · PORTRAIT.

Quality: masterpiece anime character design sheet, highly detailed clean reference art."""


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[GEN] 세리스 캐릭터 시트 v2 (reference 없이 generate) -> {OUT_PATH.name}", flush=True)

    try:
        resp = client.images.generate(
            model=MODEL,
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
