"""나이트 악마왕 Rev.6 — 회색조 암울 + 뿔 살짝 짧게 + 후광 얇게.

대표님 피드백 통합 (2026-04-21):
    Rev.5 평가: "뿔이 좀길고 분위기가 조금 밝지만 그나마 좋네"
    인터럽트 교정: "뿔이 너무 길다고 살짝짧게"
    추가 요청: "진짜 암울한분위기의 컬러지만 흑백처럼 느껴지는
               황량하고 재빛세상의 악마 / 갑옷도 이미지랑 비슷하게 /
               보라색공허 빛이 세어나오며 광채가있는모양 /
               광채는 너무 강조안되게 얇게"

수정 방향 (Rev.5 → Rev.6):
    - 뿔: 살짝 짧게 (너무 길지 않게 · moderate · balanced)
    - 팔레트: 회색조 · 거의 흑백 · ashen wasteland tone
    - 갑주: 참조 이미지의 비늘 판금 · 흉갑 엠블럼 · 무광 마감
    - 후광: 얇은 반지형 · 주변에 세부 룬 · 크기/강도 줄임
    - 보라 공허 빛: 악센트로만 (팔레트 지배 X)
    - 검은 천사 날개 유지
    - 황량한 재빛 평원 유지
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

PROMPT_DEMON_KING_REV6 = """Epic dark fantasy painted digital illustration,
vertical composition, a tall solitary dark demon king figure standing frontally,
imposing commanding stance on an ashen grey wasteland,
distant crows circling in a oppressive ashen grey sky behind him,
the whole scene is desaturated — almost monochromatic grey and black,
a bleak world drained of color, only faint ember glow in the distance,

his face completely hidden behind a menacing dark helm with TWO MODERATELY SHORT CURVED HORNS,
the horns are balanced in proportion — noticeable but not excessive, elegant restraint,
from narrow eye slits in the helm, cold violet-purple void light leaks outward like thin cold flame,
the same violet void light seeps subtly from gaps in armor joints,
BUT the violet glow is an ACCENT ONLY — it does not dominate the palette,

he wears heavy dark layered scaled plate armor —
matte dark steel with sharp angular scale-like panels,
a central embossed emblem on the chestplate,
articulated pauldrons, gauntlets, heavy sabatons,
a torn dark tabard hanging at his waist,
long strands of silver-white hair escape from beneath the back of his helm flowing down past his shoulders,

MASSIVE BLACK FEATHERED ANGEL WINGS spread wide on both sides behind him,
the wings are tattered corrupted angelic wings made of black feathers,
individual black feathers drifting in the cold dead air,

a colossal two-handed dark longsword held down at his right side,
the blade is long straight obsidian-black steel with faint subtle violet void veins,

DIRECTLY BEHIND his head, a THIN ELEGANT GOLDEN HALO RING —
a delicate circular line of faint golden light with fine sacred rune patterns,
IMPORTANT: the halo is UNDERSTATED, restrained, thin — not a massive burst of rays,
not a large mandala, just a subtle ring of sacred geometry behind his head,
warm gold tones muted, small scale, dignified restraint,
the halo suggests divinity without overwhelming the dark composition,

atmosphere: ashen cold mist rolling over grey cracked ground, distant grey mountains in fog,
drifting black feathers and occasional faint amber embers,
oppressive silence, solemn dread,
COLOR PALETTE: dominant ashen greys, charcoal blacks, muted iron tones,
violet accents only from helm slits, armor joints, and sword veins — thin and subtle,
a small amount of muted gold from the thin halo ring,
very minimal warm amber embers,
the overall feeling is almost black and white, a bleak grey world with just a hint of cold violet and faint gold,

style: painterly digital illustration with rich visible brushwork,
dark fantasy concept art rendering,
inspired by the tragic regality of Berserk's Femto-form Griffith
and Final Fantasy XIV's Emet-Selch's ancient dignity,
Dave Rapoza and Yoshitaka Amano painterly texture influence,

IMPORTANT: NOT Warcraft Lich King, NOT cartoon bright,
desaturated grim ashen world aesthetic,
this is the silver-haired guardian knight transformed — demon-saint paradox,

dramatic chiaroscuro lighting, vertical composition, 4K masterpiece,
epic solitary ominous presence, bleak grey palette with subtle violet and faint gold accents"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev6_2026-04-21.png"

    print(f"[GEN] demon king rev6 (ashen grey + shorter horns + thin halo) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_REV6, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
