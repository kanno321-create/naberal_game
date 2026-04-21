"""나이트 악마왕 대관 Rev.3 — 리치킹 복제 탈피 · 나이트 고유 외형 유지.

대표님 피드백 (2026-04-21):
    Rev.2: "그냥 리치킹을 만들어왔노 ㅋㅋㅋ"
    = 리치킹 복제품이 되어버림

수정 방향:
    - "Lich King", "Arthas", "Warcraft" 키워드 완전 제거
    - 나이트 고유 외형 최우선 (순백 긴 머리·파란 눈·178cm·knight_fullbody_rev1 의 가디언 코트 변이)
    - 원본 가디언 코트가 "심연 부식 · 어둠으로 진화" 한 컨셉
    - 헬름: 얼굴 절반 노출 (하관 보임) · 왕관형이되 과한 스파이크 없음
    - 스타일: Dark Souls Gwyn, FF14 Emet-Selch, Bloodborne Ludwig, Sephiroth Northern Crater
    - 톤 유지: 침묵·고귀한 악·위압감
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

PROMPT_DEMON_KING_REV3 = """Epic dark fantasy illustration, a tall solitary young male figure
standing alone before a black obsidian throne in a vast empty hall,
he is the same character from the previous guardian knight design sheet —
long silver-white hair flowing freely past his shoulders (NOT fully covered by helm),
his face is partially visible — the lower half exposed showing his refined pale androgynous features,
cold piercing blue eyes glowing faintly from the shadow of the upper helm,
a slender elegant dark half-helm crowns his head — it covers the top of his skull and forehead
but leaves his face open from the nose down, the helm has a small dark diadem shape, no large horns,
the helm's design is sleek, ornate, restrained — noble craftsmanship, not monstrous,
he wears an evolved version of his original guardian's coat —
the dark coat has grown heavier and darker, fused with pieces of dark plate armor,
subtle silver filigree now tinted with violet-black corruption runes,
the armor feels like his original clothes corrupted and transformed, not foreign gear,
a single massive dark sword held point-down at his side,
the sword blade is obsidian-black with faint violet-blue void veins,
no flames, no cartoon aura, no screaming pose,
tattered long dark cloak hangs still behind him,
he stands in complete silence, weight of countless deaths upon him,
expression solemn, neither triumphant nor anguished — resigned nobility,
the throne behind him is elegant black obsidian with pale violet rune lines,
vast silent hall with distant cold blue ember lights,
thin cold mist at the floor,
style references: Dark Souls Gwyn Lord of Sunlight (late), FF14 Emet-Selch's regal presence,
Sephiroth's entrance in the Northern Crater,
Bloodborne's Ludwig the Holy Blade,
Berserk's Guts after donning the berserker armor (but more elegant, less monstrous),
IMPORTANT: this is NOT a Warcraft Lich King / Arthas, NOT plate juggernaut, NOT horned skull helm,
character identity is the silver-haired androgynous guardian turned demon king —
elegance preserved, corrupted into regal darkness,
Japanese seinen anime dark fantasy illustration,
Tetsuya Nomura and Yoshitaka Amano aesthetic,
painted concept art, highly detailed, dramatic chiaroscuro,
cold muted palette — blacks, deep silvers, pale violet-blue accents,
masterpiece, 4K, stillness and noble corruption"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_demon_king_coronation_rev3_2026-04-21.png"

    print(f"[GEN] demon king rev3 (identity preserved) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_DEMON_KING_REV3, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
