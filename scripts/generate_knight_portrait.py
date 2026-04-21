"""나이트 주인공 초상 생성 — Nano Banana Pro 호출 (세션 #2 · 2026-04-21).

대표님 지시 (발언 39):
    "주인공 나이트의 생김새는 순백색머리카락, 남자치곤 살짝긴머리스타일,
    파란눈, 178의 키, 좋은 밸런스의 몸. 베르세르크의 그리피스나
    파판7의 세피로스같은 스타일... 일본 애니풍"

실행:
    python scripts/generate_knight_portrait.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# --- .env 로드 (shorts .env 에서 API 키 확보) ---
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

# --- shorts NanoBananaAdapter 임포트 ---
SHORTS_SCRIPTS = Path(r"C:\Users\PC\Desktop\naberal_group\studios\shorts\scripts")
sys.path.insert(0, str(SHORTS_SCRIPTS))
from orchestrator.api.nanobanana import NanoBananaAdapter  # noqa: E402

# --- 출력 디렉토리 ---
GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"
ART_DIR.mkdir(parents=True, exist_ok=True)

# --- 프롬프트 (전신 캐릭터 시트) ---
PROMPT_FULL_BODY = """Anime-style full body character design sheet of a young male warrior,
pristine silver-white hair at shoulder length slightly flowing,
piercing cold blue eyes, sharp refined androgynous bishounen features,
178cm balanced athletic build — lean but powerful, not overly muscular,
wearing a dark guardian's formal attire inspired by high fantasy,
dark coat with subtle silver trims, fitted leather armor underneath,
a longsword sheathed on his back, a dagger at his left hip,
small magical pouch at waist belt,
mysterious solemn aura, cold handsome expression,
standing in neutral pose, front view, full body visible,
art style fusion inspired by Berserk's Griffith and Final Fantasy VII's Sephiroth,
dark fantasy atmosphere, cinematic lighting, soft volumetric light,
highly detailed character concept art, high quality Japanese seinen anime illustration,
masterpiece, 4K resolution"""

PROMPT_PORTRAIT = """Anime-style bust portrait of a young male warrior,
silver-white hair medium length slightly flowing to the shoulders,
cold piercing blue eyes with depth and quiet sorrow,
sharp refined face, pale skin, androgynous bishounen beauty,
subtle melancholy in expression, lips slightly pressed,
wearing dark high-collar guardian's attire visible at the shoulders,
clean dark background with soft atmospheric fog,
side lighting creating dramatic shadow on half the face,
inspired by Griffith from Berserk and Sephiroth from Final Fantasy VII,
Japanese seinen anime style, Kentaro Miura influence,
highly detailed eyes, detailed hair strands with silver sheen,
cinematic composition, dark fantasy atmosphere,
masterpiece illustration, 4K"""

PROMPT_CONCEPT = """Anime-style dark fantasy concept art, cinematic wide shot,
a young male warrior with silver-white hair at shoulder length,
piercing blue eyes, 178cm balanced athletic build,
standing alone in a misty ancient forest at dusk,
wearing dark guardian's formal attire, sword sheathed on his back,
dagger at his left hip, small pouch at waist,
looking toward distant smoke rising over tall trees,
mysterious solemn atmosphere, memory loss aura, quiet determination,
scattered dappled sunlight filtering through ancient trees, autumn leaves,
inspired by Berserk's Griffith, Sephiroth from Final Fantasy VII,
and the atmospheric composition of Nier Automata,
Japanese seinen anime illustration style,
highly detailed, cinematic composition, volumetric light,
dark fantasy, epic, masterpiece, 4K"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found in environment or shorts .env", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)

    jobs = [
        ("knight_fullbody_rev1_2026-04-21.png", PROMPT_FULL_BODY, "전신 캐릭터 시트"),
        ("knight_portrait_rev1_2026-04-21.png", PROMPT_PORTRAIT, "반신 초상"),
        ("knight_concept_rev1_2026-04-21.png", PROMPT_CONCEPT, "컨셉아트"),
    ]

    results = []
    for filename, prompt, label in jobs:
        out_path = ART_DIR / filename
        print(f"[GEN] {label} -> {filename}", flush=True)
        try:
            saved = adapter.generate_scene(prompt=prompt, output_path=out_path)
            print(f"  [OK] saved: {saved}", flush=True)
            results.append((label, str(saved), "OK"))
        except Exception as err:
            print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
            results.append((label, str(out_path), f"FAIL: {err}"))

    print("\n=== SUMMARY ===")
    for label, path, status in results:
        print(f"  [{status}] {label} -- {path}")

    return 0 if all(r[2] == "OK" for r in results) else 2


if __name__ == "__main__":
    sys.exit(main())
