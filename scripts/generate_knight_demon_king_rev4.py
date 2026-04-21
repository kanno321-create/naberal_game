"""나이트 악마왕 Rev.4 — 악마이자 구원자 · 공허 보라빛 + 황금 후광.

대표님 지시 (2026-04-21 · 참고 이미지 제공):
    "위압감 헬름은 악마답게 무섭고 공허의 보라빛이 세어나오며,
     뒷부분 광채문양은 악마지만 구원자이로다"

수정 방향:
    - 헬름 얼굴 완전 가림 (하관 노출 X · 공포감 회복)
    - 헬름 슬릿·갑주 틈에서 "공허의 보라빛" 발광 (심연·공허 속성 · 발언 34)
    - 뒷배경에 "황금 광채 후광/만다라 문양" (구원자의 역설 · 엔딩 E 균형자=대립항)
    - 악마의 실루엣 + 성인의 후광 = 동시 공존
    - 참고 이미지의 painterly digital illustration 톤 (거친 브러시)
    - 녹-보라-검정-금색 복합 팔레트
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

PROMPT_DEMON_KING_REV4 = """Epic dark fantasy painted digital illustration,
vertical portrait composition of a tall solitary demon king figure standing frontally,
his face is completely hidden behind a menacing dark full-face helm —
the helm is sleek and terrifying, no horns but sharp angular forms,
from narrow eye slits in the helm, intense violet-purple void light leaks outward like cold flame,
the same violet void light seeps out from joints in his dark armor — at the shoulders, chest, gauntlets,
he wears heavy dark plate armor with flowing ragged cloth and a torn dark cloak,
a colossal two-handed sword held downward beside him, the blade dripping dark red essence
and glowing with violet void veins, faint red mist rising from the blade's edge,
long strands of silver-white hair escape from beneath the back of his helm, flowing down,
standing silently, no pose, no scream — only crushing dread,
BEHIND his head and shoulders, a massive intricate GOLDEN RADIANT HALO —
an ornate mandala of glowing golden rays and sacred geometric patterns spreading outward,
the halo is bright, holy, saintly — a dissonant contrast to his dark demonic form,
he is a demon king and yet a savior — both at once,
the sacred halo and the violet void light coexist in paradox,
atmosphere: dark green and black mist in the background, flickering red embers below,
cracked earth beneath his feet with red molten veins,
style: painterly digital illustration with visible textured brushwork,
reminiscent of Dave Rapoza, Jean Giraud's darker works, Yoshitaka Amano's darker paintings,
Berserk's Guts in the Berserker Armor but more regal,
FF14 Emet-Selch's tragic dignity,
NOT Warcraft Lich King, NOT cartoon, NOT cute anime,
dark fantasy masterpiece, cinematic atmospheric lighting,
color palette: deep black armor, violet-purple void glow, dark red mist, brilliant gold halo, muted green background,
dramatic vertical composition, 4K, highly detailed, heavy painterly texture,
noble corruption, paradoxical saviour-demon"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev4_2026-04-21.png"

    print(f"[GEN] demon king rev4 (demon-saviour paradox) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_REV4, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
