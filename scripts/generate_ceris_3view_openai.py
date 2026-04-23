"""세리스 3뷰 시트 · 원본 v1 rev2 프롬프트 키워드 유지 · OpenAI (세션 #8 · 2026-04-23).

대표님 지시:
    원본 v1 rev2 프롬프트 그대로 사용 + 3뷰 (FRONT · BACK · PORTRAIT) 레이아웃 추가.

실행:
    python scripts/generate_ceris_3view_openai.py
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
OUT_PATH = ART_DIR / "ceris_3view_openai_2026-04-23.png"

MODEL = "gpt-image-1"
IMAGE_SIZE = "1536x1024"  # 가로 (3뷰)
IMAGE_QUALITY = "high"

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
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"[OpenAI 3view] Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[OpenAI 3view GEN] -> {OUT_PATH.name}", flush=True)

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
