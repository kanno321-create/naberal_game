"""게임 표지 NIGHTMARE 생성 — OpenAI gpt-image-1 multi-reference edit (세션 #8 · 2026-04-23).

대표님 지시:
    - 나이트 레퍼런스: knight_fullbody_rev1_2026-04-21.png (중간 서 있는 컷 기준)
    - 세리스 레퍼런스: ceris_v1_rev2_openai_2026-04-23.png
    - 얼굴 일관성 반드시 유지
    - 두명 센터·전신 포즈
    - 나이트 = 칼 들고 서있음, 세리스 = 지팡이 들고 두 손 모음
    - 제목: "NIGHTMARE" (미정 가제)
    - 배경·세계관 상징: 나베랄 감마 판단
    - 다크 판타지 톤

세계관 요소 집약:
    - Q-CORE 1·3: 수정 2 (마왕 봉인) 거대 그림자 뒤
    - 설계 헌법 3조: 불완전성 · 영혼 평등 · 인간 비악
    - a-47-E: 모두 비악 · 우주 포식자 존재
    - y-3 테마: "신의 권능 = 저주"
    - 양 대륙 대비: Elucia 성당 첨탑 (좌) · Veilglass 얼음섬 (우)
    - 진엔딩 복선: 고대 왕좌 실루엣 · Warcraft 3 아서스 오마주
    - 순환 구조: 6 번의 균형 · 차원 균열 · 은하 수호자 집단

실행:
    python scripts/generate_game_cover_nightmare.py
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

REF_KNIGHT = ART_DIR / "knight_fullbody_rev1_2026-04-21.png"
REF_CERIS = ART_DIR / "ceris_v1_rev2_openai_2026-04-23.png"
OUT_PATH = ART_DIR / "game_cover_nightmare_2026-04-23.png"

MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
IMAGE_SIZE = os.environ.get("OPENAI_IMAGE_SIZE", "1024x1536")  # 세로 포스터
IMAGE_QUALITY = os.environ.get("OPENAI_IMAGE_QUALITY", "high")

PROMPT = """Dark fantasy JRPG video game cover art, title "NIGHTMARE",
cinematic full-body two-character poster composition centered, two figures standing close but separated by tragic fate,

LEFT CHARACTER — male protagonist Knight (preserve face from first reference image):
long silver-white hair slightly flowing to the shoulders,
piercing cold blue eyes with quiet melancholy,
sharp refined androgynous bishounen features, pale fair skin,
178cm balanced athletic build,
wearing dark guardian's long formal coat with silver embroidery and fitted leather armor underneath,
cold solemn expression, standing straight in neutral pose at center-left,
holding a one-handed longsword point-down at his side with one hand,
other arm relaxed, Griffith-Sephiroth fusion aesthetic,

RIGHT CHARACTER — female demon heroine Ceris (preserve face from second reference image):
long flowing jet-black hair,
pale porcelain skin with gentle warmth softly luminous,
glowing deep violet eyes with profound melancholy and longing,
pitch-black curved demon horns on her head, pointed ears,
elegant revealing gothic black dress with intricate silver embroidery,
glowing purple magical gemstone core embedded in her chest emitting soft purple light,
holding an ornate long wizard staff vertically with both hands clasped in front of her chest,
standing gracefully beside the Knight at center-right, quiet resigned expression,

BACKGROUND — layered symbolic worldbuilding:
foreground ground level: cracked marble ruins, ancient dark throne partially visible in deep shadow behind them (echo of Warcraft 3 Frozen Throne), scattered broken guardian statues at their feet, swirling ominous mist pooling on the floor,
middle depth: faint silhouettes of tall cathedral spires on the far left (Elucia church), distant frozen jagged island peaks on the far right (Veilglass northern isle), ancient blood-red glowing runes scattered floating in mid-air around both characters,
upper sky: violet stormy sky with visible cracks of dimensional void opening, distant ethereal galaxy swirl with faint golden guardian sigils far above,
symbolic mid-layer: massive dark shadow of a second towering magical crystal behind them glowing deep purple (Crystal 2 - the demon king's prison), faint almost-invisible silhouette of cosmic predator tendrils reaching from the edges of the upper sky,

TITLE "NIGHTMARE" rendered in elegant dark fantasy serif typography at the top of the composition, subtle silver-violet metallic embossed treatment, title edges partially dissolving into swirling void mist,

VISUAL PHILOSOPHY:
six-race world's human-demon axis visually represented on left and right,
theme "divine power has become curse not blessing" somber mood,
two characters bound by love yet destined to separate,
inevitable cycle of six broken balances echoing in the composition,

STYLE:
painterly anime JRPG AAA cover art fusion,
muted desaturated color palette dominated by deep blacks, cold purple-magenta accents, crimson rune glow, subtle golden rim highlights,
watercolor and ink textured brush strokes visible,
dramatic rim lighting on both characters with soft volumetric fog enveloping the scene,
Berserk meets Nier Automata meets Octopath Traveler HD-2D meets Final Fantasy XVI cover sensibility,
somber grand epic tragic atmosphere,
masterpiece, cinematic composition, extremely high detail, 4K poster quality"""


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found", file=sys.stderr)
        return 1
    if not REF_KNIGHT.exists():
        print(f"ERROR: 나이트 레퍼런스 없음 → {REF_KNIGHT}", file=sys.stderr)
        return 1
    if not REF_CERIS.exists():
        print(f"ERROR: 세리스 레퍼런스 없음 → {REF_CERIS}", file=sys.stderr)
        return 1

    client = OpenAI()
    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}")
    print(f"Refs: {REF_KNIGHT.name} + {REF_CERIS.name}")
    print(f"[GEN] NIGHTMARE cover -> {OUT_PATH.name}", flush=True)

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
            print("FAIL: no image data in response", file=sys.stderr)
            return 2
        print(f"  [OK] saved: {OUT_PATH}")
        print(f"  size: {OUT_PATH.stat().st_size:,} bytes")
        return 0
    except Exception as err:
        print(f"  [FAIL] {type(err).__name__}: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
