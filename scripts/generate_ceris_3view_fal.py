"""세리스 3뷰 시트 · 원본 v1 rev2 프롬프트 키워드 유지 · fal.ai (세션 #8 · 2026-04-23).

대표님 지시: OpenAI 와 동일 프롬프트로 fal 3뷰 1장 · 비교.
모델: fal-ai/flux-pro/v1.1-ultra

실행:
    python scripts/generate_ceris_3view_fal.py
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
OUT_PATH = ART_DIR / "ceris_3view_fal_2026-04-23.png"

# OpenAI 3view 와 완전 동일 프롬프트
PROMPT = """(masterpiece, best quality, official game concept art:1.2),
Japanese anime character design turnaround sheet of the same dark fantasy demon heroine,
three full views of the same character arranged horizontally in one image:
LEFT panel: full body front view from head to toe,
CENTER panel: full body back view showing long hair and dress back,
RIGHT panel: bust portrait close-up showing face details.

Heroine design (consistent across all three views, identical character):
1girl, dark fantasy demon heroine,
(mature adult woman in her mid-20s, tall slim graceful adult figure, perfect slim adult body proportions, 7.5-8 heads tall anime proportions, elongated feminine anatomy, NOT chibi, NOT short, NOT young girl, NOT lolita:1.5),
pale porcelain skin with gentle warmth, softly luminous complexion, delicate but alive,
glowing deep violet eyes with a hint of melancholy,
wearing an elegant but revealing gothic black dress with intricate silver embroidery,
(a glowing magical gemstone core embedded in the skin of her chest emitting soft purple light:1.3),
ancient blood-red runes floating around her,
long flowing dark hair reaching her waist,

Style:
muted colors, desaturated palette,
painterly anime style, JRPG character design,
watercolor and ink texture, detailed brush strokes,
somber and mysterious atmosphere,
in the style of dark fantasy concept art.

Layout: clean three-view turnaround sheet, plain neutral gray background,
small elegant serif labels under each panel: FRONT · BACK · PORTRAIT."""


def main() -> int:
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("ERROR: FAL_KEY not found", file=sys.stderr)
        return 1
    os.environ["FAL_KEY"] = fal_key

    print("[fal 3view] Model: fal-ai/flux-pro/v1.1-ultra · Aspect: 16:9 landscape")
    print(f"[fal 3view GEN] -> {OUT_PATH.name}", flush=True)

    try:
        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1-ultra",
            arguments={
                "prompt": PROMPT,
                "num_images": 1,
                "enable_safety_checker": False,
                "aspect_ratio": "16:9",
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
