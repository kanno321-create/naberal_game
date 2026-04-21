"""나이트 악마왕 대관 Rev.2 — 리치킹 톤 · 악의 고귀함 · 위압감.

대표님 피드백 (2026-04-21):
    "좀 유치하노 악마왕의 모습이 리치킹처럼 악으로 고귀하며 위압감이있어야지"

수정 방향:
    - "리치킹" 키워드 강화 (WoW Lich King Arthas)
    - "유치" 제거 — 과도한 불꽃·붉은 연기·소리지름 같은 애니 클리셰 빼고
      침묵·냉정·압도적 존재감 중심
    - "악으로 고귀" = 악하지만 위엄 있는 왕의 풍모 (타락한 귀족)
    - "위압감" = 정적 · 거대함 · 서늘함 · 공허의 아우라
    - 얼굴은 헬름 안 그림자 속 · 오직 발광 눈만 보임
    - 왕좌 + 얼어붙은 분위기 + 조용한 어둠
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

PROMPT_DEMON_KING_REV2 = """Epic dark fantasy cinematic illustration, a tall solitary figure
standing alone at the top of a black marble staircase before an enormous obsidian throne,
the figure is a fallen guardian who has become a demon king —
direct visual reference to the Lich King Arthas Menethil from Warcraft 3 and Wrath of the Lich King,
he wears an impossibly ornate pitch-black full plate armor with sharp angular pauldrons,
the armor is covered in baroque engravings, dark silver filigree, and subtle occult runes,
a crowned dark helm completely hides his face in shadow,
from within the helm's eye slits, two pale ice-blue lights burn coldly,
long strands of pristine silver-white hair flow out from beneath the helm's edges down his back,
a colossal two-handed dark sword rests point-down beside him or held at his side,
the sword radiates a quiet, still, void-black aura — not flames, not particles, but a silence of cold,
a tattered long dark cloak hangs behind him completely still, no wind,
he does not pose dramatically — he simply stands, utterly silent, weight of ages,
absolute silent authority, noble evil, regal and terrifying,
the throne behind him is carved from black stone with ancient glowing cold-blue runes,
the hall is vast and empty, blue-tinted torches in the far distance,
cold mist pooling around his feet, faint frost on the ground,
NO loud red flames, NO cartoon aura, NO screaming pose, NO overly flashy effects,
instead: stillness, silence, cold dignity, crushing presence,
art direction inspired by World of Warcraft Lich King cinematic, Dark Souls Gwyn, Sephiroth in the Northern Crater, Berserk's Griffith ascended,
painted concept art style, highly detailed, dramatic chiaroscuro,
cold muted color palette — blacks, deep silvers, pale cold blue,
Japanese seinen dark fantasy illustration meets Blizzard cinematic painting,
masterpiece, 4K, epic atmosphere of doom and regal corruption"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev2_2026-04-21.png"

    print(f"[GEN] demon king rev2 (Lich King tone) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_REV2, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
