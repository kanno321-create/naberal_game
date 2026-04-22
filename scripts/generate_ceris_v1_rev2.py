"""세리스 v1 rev2 · 피부 창백함 완화판 (세션 #8 · 2026-04-23).

대표님 피드백:
    "버전1이 참 이쁜데 버전2처럼 덜 창백하게 만들수없나?"

변경 지점 (v1 대비):
    - "extremely pale translucent skin" → "pale porcelain skin, softly luminous, delicate but alive"
    - "translucent" 제거 = 살 비치는 죽을상 완화
    - "porcelain" 도자기 느낌 = 매끄러운 창백함 유지
    - "gentle warmth · softly luminous · alive" 미세한 생기 추가
    - 나머지 구도·분위기·톤은 v1 그대로

실행:
    python scripts/generate_ceris_v1_rev2.py
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
ART_DIR.mkdir(parents=True, exist_ok=True)

MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
IMAGE_SIZE = os.environ.get("OPENAI_IMAGE_SIZE", "1024x1536")
IMAGE_QUALITY = os.environ.get("OPENAI_IMAGE_QUALITY", "high")

# --- v1 rev2: translucent 제거 + 도자기 + 미세 온기 ---
PROMPT_V1_REV2 = """(masterpiece, best quality, official game concept art:1.2),
1girl, dark fantasy demon heroine,
pale porcelain skin with gentle warmth, softly luminous complexion, delicate but alive,
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


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    out_path = ART_DIR / "ceris_v1_rev2_openai_2026-04-23.png"

    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[GEN] v1 rev2 (less pale) -> {out_path.name}", flush=True)

    try:
        resp = client.images.generate(
            model=MODEL,
            prompt=PROMPT_V1_REV2,
            size=IMAGE_SIZE,
            quality=IMAGE_QUALITY,
            n=1,
        )
        item = resp.data[0]
        if getattr(item, "b64_json", None):
            out_path.write_bytes(base64.b64decode(item.b64_json))
        elif getattr(item, "url", None):
            import urllib.request
            urllib.request.urlretrieve(item.url, str(out_path))
        else:
            print("FAIL: no image data in response", file=sys.stderr)
            return 2
        print(f"  [OK] saved: {out_path}")
        return 0
    except Exception as err:
        print(f"  [FAIL] {type(err).__name__}: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
