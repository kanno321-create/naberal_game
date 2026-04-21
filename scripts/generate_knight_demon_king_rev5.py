"""나이트 악마왕 Rev.5 — 검은 천사 날개 · 뿔 헬름 · 황금 후광 · 보라 공허.

대표님 지시 (2026-04-21 · 새 참조 이미지 제공):
    "딱 이런느낌인데 여기에 뒤에 광채문양이고
     헬름사이에서 보라색 공허의빛이 세어나오는느낌?"

수정 방향:
    - 참조 이미지 요소 추가:
      * 검은 천사의 큰 날개 (corrupted angel wings)
      * 뿔 달린 헬름 (2 horns curving upward)
      * 황량한 안개 평원 · 까마귀 배경
      * painterly digital 다크 판타지 톤
    - Rev.4 요소 유지:
      * 뒷배경 황금 만다라 후광
      * 헬름 슬릿 · 갑주 관절에서 보라 공허 빛 누출
      * 나이트 정체성 (순백 긴 머리 헬름 뒤로)
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

PROMPT_DEMON_KING_REV5 = """Epic dark fantasy painted digital illustration,
vertical composition, a tall solitary dark demon king figure standing frontally,
imposing commanding stance on the edge of a misty windswept rocky wasteland,
distant crows circling in a muted grey-green sky behind him,
subtle amber embers floating in the cold air,

his face is completely hidden behind a menacing dark helm with TWO HORNS CURVING UPWARD,
the helm is sharp and terrifying, angular design with vertical slits,
from within the helm's eye slits, intense violet-purple void light leaks outward like cold flame,
the same violet void light also seeps out from the gaps in his armor joints —
shoulders, chest, gauntlet knuckles, waist — as if his very essence is void energy contained,

he wears heavy dark plate armor, pitch-black metal with sharp angular layered panels,
articulated pauldrons, intricate chestplate with dark engravings,
armored gauntlets, heavy sabatons, a torn dark tabard hanging at his waist,
long strands of silver-white hair escape from beneath the back of his helm flowing down past his shoulders,

MASSIVE BLACK FEATHERED ANGEL WINGS spread wide on both sides behind him —
the wings are tattered corrupted angelic wings made of black feathers,
framing his silhouette from behind like a fallen dark angel,
individual black feathers scattered drifting in the cold air around him,

a colossal two-handed dark longsword held down at his right side,
the sword blade is long straight obsidian-black steel with faint violet void veins,
subtle violet mist trailing from the blade's edge,

DIRECTLY BEHIND his head and shoulders, centered between the black wings,
a massive GOLDEN RADIANT HALO — ornate sacred mandala of brilliant glowing golden rays,
intricate geometric patterns and sacred runes forming a circular emanation,
the holy golden halo sits in stark paradox against the black demonic wings,
he is both demon and saviour at once,

atmosphere: cold mist rolling over rocky ground, distant mountains in fog,
oppressive silence, solemn dread,

style: painterly digital illustration with rich visible brushwork,
dark fantasy concept art rendering, Midjourney-style dark fantasy aesthetic,
inspired by the tragic regality of characters like Berserk's Femto-form Griffith
and Final Fantasy XIV's Emet-Selch's ancient dignity,
Dave Rapoza and Yoshitaka Amano painterly texture influence,

IMPORTANT: NOT Warcraft Lich King, NOT directly copying any known character,
this is the silver-haired guardian knight transformed — his own design,
elegance twisted into noble dark-angel corruption,

color palette: deep black armor and wings, violet-purple void glow from helm and joints,
brilliant warm gold halo, muted grey-green misty sky, subtle amber ember particles,
dramatic high-contrast chiaroscuro lighting,
vertical composition, 4K masterpiece,
epic solitary ominous presence, demon-saint paradox, noble corruption"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev5_2026-04-21.png"

    print(f"[GEN] demon king rev5 (black wings + halo + void glow) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_REV5, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
