"""나이트의 악마왕 대관 장면 생성 — outline Ch.30 Scene 4.

대표님 지시 (2026-04-21):
    "knight_fullbody_rev1 이외형의 나이트가 악마왕이 되려고
    악마왕의 갑주가 입혀졌고, 헬름을 쓰고있는장면도"

레퍼런스:
    - outline Ch.30 "왕좌의 길" Scene 3~4 (계단 + 대관)
    - Warcraft 3 Arthas Lich King (아서스 오마주 · style_bible 명시)
    - Sephiroth FF7 · Berserk Guts berserker armor
    - 세계관: 심연·공허 속성 (발언 34)
"""
from __future__ import annotations

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

SHORTS_SCRIPTS = Path(r"C:\Users\PC\Desktop\naberal_group\studios\shorts\scripts")
sys.path.insert(0, str(SHORTS_SCRIPTS))
from orchestrator.api.nanobanana import NanoBananaAdapter  # noqa: E402

GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"
ART_DIR.mkdir(parents=True, exist_ok=True)

PROMPT_DEMON_KING_CORONATION = """Anime-style full body cinematic shot of a young male warrior
at the moment of becoming a demon king,
the same character as the previous guardian knight design —
long silver-white hair flowing from beneath a dark ornate helm down to his back,
piercing cold blue eyes glowing from the helm's eye slits,
wearing ornate dark demon king's full plate armor,
the armor is pitch-black metal with intricate occult silver engravings,
jagged spiked pauldrons, sharp gauntlets, high dark collar,
subtle abyss-void energy wisps emanating from the armor joints,
a massive dark longsword held in one hand — the sword radiating purple-black void energy,
torn black cape billowing behind him with dark mist,
standing on the top of an ascending stone staircase before a throne of blackened iron,
the throne behind him carved with ancient runes,
dark fantasy coronation moment,
art style inspired by Warcraft 3 Arthas Lich King transformation scene,
Sephiroth's descent from Final Fantasy VII,
Berserk's Guts berserker armor aesthetic,
character design consistent with a silver-haired androgynous bishounen warrior,
Japanese seinen anime illustration style,
Tetsuya Nomura and Yoshitaka Amano influence,
dramatic cinematic backlight, volumetric smoke, ember particles floating,
crimson and purple atmospheric glow, dark hall with distant torches,
epic dark fantasy, masterpiece, 4K, highly detailed armor textures,
cool dark color palette with crimson accents"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev1_2026-04-21.png"

    print(f"[GEN] demon king coronation -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_CORONATION, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
