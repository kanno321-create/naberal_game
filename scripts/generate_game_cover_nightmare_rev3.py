"""게임 표지 NIGHTMARE rev3 · 일본 애니풍 복원 + 얼굴 레퍼런스 엄격 유지 (세션 #8 · 2026-04-23).

대표님 rev2 피드백 4건:
    1. "세리스 머리큰 난쟁이처럼" → rev2 에서 비율은 보정됨
    2. "ceris_v1_rev2 얼굴이 어떻게 저렇게 변하노" → 얼굴 손상
    3. "나이트도 얼굴이 더 멋있는데 못생겨졌노" → 얼굴 손상
    4. "일본애니풍이 없어져버렸네" → 핵심 문제

rev3 전략:
    - "Japanese 2D anime cel-shaded illustration" 최상위 · NOT 부정 프롬프트 강화
    - 참조 아티스트 명시 (Kentaro Miura · Yoshitaka Amano · Takeshi Obata · Akihiko Yoshida)
    - "EXACTLY preserve anime facial features · DO NOT westernize" 얼굴 락업
    - Knight = Griffith/Sephiroth 비숑넨 · Ceris = 마족 히로인 비쇼조 명시
    - 비율 유지 (rev2 성과)

실행:
    python scripts/generate_game_cover_nightmare_rev3.py
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

REF_KNIGHT = ART_DIR / "knight_fullbody_rev1_2026-04-21.png"
REF_CERIS = ART_DIR / "ceris_v1_rev2_openai_2026-04-23.png"
OUT_PATH = ART_DIR / "game_cover_nightmare_rev3_2026-04-23.png"

MODEL = "gpt-image-1"
IMAGE_SIZE = "1024x1536"
IMAGE_QUALITY = "high"

PROMPT = """JAPANESE 2D ANIME ILLUSTRATION, cel-shaded dark fantasy light novel game cover art, title "NIGHTMARE".

STYLE LOCK (CRITICAL — DO NOT DEVIATE):
Pure Japanese anime 2D cel-shaded illustration ONLY.
NOT photorealistic. NOT 3D CGI render. NOT western oil painting. NOT cinematic live-action. NOT realistic portrait painting.
In the exact artistic style of Kentaro Miura (Berserk cover art), Yoshitaka Amano (Final Fantasy illustration), Takeshi Obata (Death Note), and Akihiko Yoshida (Bravely Default / Final Fantasy XII character design).
Clean anime line art with cel-shading, Japanese seinen manga cover illustration aesthetic.
Flat anime colors with dramatic shadows, NOT smooth painterly gradients.
Large expressive anime eyes, bishounen and bishoujo anime facial features.

FACE LOCK (CRITICAL — PRESERVE REFERENCES):
EXACTLY preserve the anime facial features from both reference images.
Knight's face: bishounen anime boy face exactly like the first reference image — same eye shape, same nose, same jaw, same sharp androgynous beauty.
Ceris's face: bishoujo anime girl face exactly like the second reference image — same large violet eyes, same delicate features, same expression.
DO NOT westernize the faces. DO NOT make them realistic. KEEP them anime.

COMPOSITION:
Full body two-character poster, both adult humanoids standing side by side at center, complete head-to-toe view.
Both 7.5-8 heads tall realistic anime adult proportions, NOT chibi, NOT super-deformed.
Knight 178cm on the left, Ceris 170cm on the right — same height range with Ceris only slightly shorter.

LEFT — Knight (male protagonist, anime bishounen):
long silver-white hair flowing to shoulders, piercing cold blue anime eyes with melancholy, pale skin, sharp androgynous bishounen face.
Wearing long dark guardian's formal coat reaching below knees with silver embroidery and fitted leather armor underneath.
Standing straight neutral pose, cold solemn anime expression.
Holding a longsword point-down vertically at his right side with right hand.
Style: Griffith (Berserk) × Sephiroth (FFVII) bishounen aesthetic.

RIGHT — Ceris (female demon heroine, anime bishoujo):
tall slim adult anime girl, long flowing jet-black hair reaching waist.
Pale porcelain skin with gentle warmth softly luminous.
Large glowing deep violet anime eyes with profound melancholy.
Pitch-black curved demon horns on head, pointed anime elf-like ears.
Wearing long elegant revealing gothic black dress with intricate silver embroidery, dress reaching ankles.
Glowing purple magical gemstone core embedded in her chest emitting soft purple light.
Holding an ornate long wizard staff vertically with both hands clasped together in front of her chest, staff her full body length.
Quiet resigned anime expression.

BACKGROUND (anime style matte painting, keep subtle):
Foreground: cracked marble ruins, dark ancient throne partially visible behind them, scattered broken guardian statues, swirling anime-style mist at their feet.
Middle: faint anime silhouettes of tall cathedral spires far left, distant jagged frozen island peaks far right, blood-red floating ancient runes scattered in mid-air around them.
Sky: violet stormy void with cracks of dimensional rift, distant ethereal galaxy swirl with faint golden sigils.
Symbol: massive dark anime silhouette of towering magical crystal behind them glowing deep purple.

TITLE "NIGHTMARE" at top center in elegant dark fantasy anime serif typography, silver-violet metallic embossed, edges dissolving into void mist.

PALETTE:
Muted desaturated anime palette dominated by deep blacks, cold purple-magenta accents, crimson rune glow, subtle golden rim highlights.
Dramatic anime rim lighting on both characters with volumetric fog.

FINAL STYLE REMINDER:
This is a JAPANESE ANIME LIGHT NOVEL COVER, NOT a western realistic painting.
Keep it 2D anime cel-shaded art, masterpiece anime illustration quality, somber tragic dark fantasy atmosphere."""


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[GEN] NIGHTMARE cover rev3 (일본애니풍 복원) -> {OUT_PATH.name}", flush=True)

    try:
        with open(REF_KNIGHT, "rb") as f1, open(REF_CERIS, "rb") as f2:
            resp = client.images.edit(
                model=MODEL,
                image=[f1, f2],
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
