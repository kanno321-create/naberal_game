"""세리스 · 원본 v1 rev2 프롬프트 그대로 fal.ai 비교용 (세션 #8 · 2026-04-23).

대표님 지시: OpenAI 와 동일 프롬프트로 fal 1 장 · 비교.
모델: fal-ai/flux-pro/v1.1-ultra

실행:
    python scripts/generate_ceris_sheet_mature_fal.py
"""
from __future__ import annotations

import os
import sys
import urllib.request
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

import fal_client

GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"
OUT_PATH = ART_DIR / "ceris_v1_rev2_fal_2026-04-23.png"

# 원본 v1 rev2 프롬프트 (OpenAI 스크립트와 완전 동일)
PROMPT = """(masterpiece, best quality, official game concept art:1.2),
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
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("ERROR: FAL_KEY not found in shorts/.env", file=sys.stderr)
        return 1
    os.environ["FAL_KEY"] = fal_key

    print("[fal] Model: fal-ai/flux-pro/v1.1-ultra · Aspect: 9:16 (portrait)")
    print(f"[fal GEN] -> {OUT_PATH.name}", flush=True)

    try:
        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1-ultra",
            arguments={
                "prompt": PROMPT,
                "num_images": 1,
                "enable_safety_checker": False,
                "aspect_ratio": "9:16",
                "output_format": "png",
                "raw": False,
            },
            with_logs=False,
        )
        images = result.get("images", [])
        if not images:
            print(f"FAIL: no images. raw={result}", file=sys.stderr)
            return 2
        img_url = images[0].get("url")
        if not img_url:
            print(f"FAIL: no url. raw={images[0]}", file=sys.stderr)
            return 2

        print(f"  [DL] {img_url}")
        urllib.request.urlretrieve(img_url, str(OUT_PATH))
        print(f"  [OK] saved: {OUT_PATH}")
        print(f"  size: {OUT_PATH.stat().st_size:,} bytes")
        return 0
    except Exception as err:
        print(f"  [FAIL] {type(err).__name__}: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
