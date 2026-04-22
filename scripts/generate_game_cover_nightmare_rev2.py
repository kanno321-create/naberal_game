"""게임 표지 NIGHTMARE rev2 · 세리스 비율 보정 (세션 #8 · 2026-04-23).

대표님 rev1 피드백:
    "나이트는 어느정도 잘됐는데 세리스는 뭐 머리큰 난쟁이처럼 구현이 이상하노"

원인:
    세리스 레퍼런스 (ceris_v1_rev2_openai_2026-04-23.png) 가 반신 초상 기반 →
    AI 가 전신 추정 시 머리 크게 / 몸 작게 왜곡 (chibi 경향).

rev2 개선:
    - 프롬프트에 "7-8 heads tall adult proportions" 명시
    - "Ceris: tall slim elegant adult woman, 170cm, similar height range as Knight"
    - 명시적 "avoid chibi, avoid oversized head, avoid shortened body"
    - "BOTH characters same realistic adult human body ratio"
    - 포즈 재강조: 세리스가 나이트와 나란히 같은 지면에 서서 **비슷한 키** 로 보이도록

실행:
    python scripts/generate_game_cover_nightmare_rev2.py
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
OUT_PATH = ART_DIR / "game_cover_nightmare_rev2_2026-04-23.png"

MODEL = "gpt-image-1"
IMAGE_SIZE = "1024x1536"
IMAGE_QUALITY = "high"

# rev2: 비율 보정 강화
PROMPT = """Dark fantasy JRPG video game cover art, title "NIGHTMARE",
cinematic full-body two-character poster, two elegant adult humanoid figures standing side by side at center, both shown in complete full body view from head to toe,

CRITICAL BODY PROPORTIONS (MUST FOLLOW):
BOTH characters are tall slim elegant adult humanoids with realistic 7.5-8 heads tall body proportion,
Knight is 178cm tall and Ceris is 170cm tall — approximately same height range with Ceris only slightly shorter,
NOT chibi, NOT super-deformed, NOT oversized head with small body, NOT child-like proportions,
long elongated slender adult figures filling the vertical frame from their feet to their shoulders,

LEFT CHARACTER — male protagonist Knight (preserve face from first reference image):
tall slim adult male, 178cm, long silver-white hair flowing to shoulders,
piercing cold blue eyes with melancholy, sharp refined androgynous bishounen features, pale skin,
wearing long dark guardian's coat reaching below knees with silver embroidery,
cold solemn expression, standing straight in neutral pose,
holding a longsword point-down vertically at his right side with right hand, left arm relaxed,
Griffith-Sephiroth aesthetic,

RIGHT CHARACTER — female demon heroine Ceris (preserve face from second reference image):
tall slender adult woman, 170cm, with elegant long legs and graceful adult body posture,
long flowing jet-black hair reaching her waist,
pale porcelain skin with gentle warmth softly luminous,
glowing deep violet eyes with profound melancholy,
pitch-black curved demon horns on head, pointed ears,
wearing long elegant revealing gothic black dress with intricate silver embroidery, dress reaching her ankles flowing,
glowing purple magical gemstone core embedded in her chest emitting soft purple light,
holding an ornate long wizard staff vertically with both hands clasped together in front of her chest, staff nearly her full body length,
standing gracefully beside the Knight, quiet resigned expression,
Ceris's head top should be slightly below Knight's head top because she is 8cm shorter but NOT massively shorter,

BACKGROUND — layered symbolic worldbuilding (keep subtle, don't overwhelm figures):
ground: cracked marble ruins, ancient dark throne partially visible in deep shadow behind them, scattered broken guardian statues, swirling mist pooling at their feet,
middle: faint silhouettes of tall cathedral spires far left (Elucia church), distant jagged frozen island peaks far right (Veilglass), blood-red floating runes scattered in mid-air around them,
sky: violet stormy void with cracks of dimensional rift opening, distant ethereal galaxy swirl with faint golden sigils,
mid-layer symbol: massive dark silhouette of a towering magical crystal behind the characters glowing deep purple,

TITLE "NIGHTMARE" at top center in elegant dark fantasy serif typography, silver-violet metallic embossed treatment, edges dissolving into void mist,

STYLE:
painterly anime JRPG AAA cover art fusion,
muted desaturated palette dominated by deep blacks, cold purple-magenta accents, crimson rune glow, subtle golden rim highlights,
watercolor and ink textured brush strokes,
dramatic rim lighting on both characters with volumetric fog,
Berserk meets Nier Automata meets Final Fantasy XVI cover sensibility,
somber grand tragic atmosphere,
masterpiece, cinematic composition, extremely high detail, 4K poster quality,
full body realistic adult humanoid proportions"""


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"[GEN] NIGHTMARE cover rev2 (비율 보정) -> {OUT_PATH.name}", flush=True)

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
