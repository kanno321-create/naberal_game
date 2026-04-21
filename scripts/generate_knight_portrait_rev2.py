"""나이트 반신 초상 Rev.2 — 베르세르크 톤 제거 · 세피로스 방향 강화.

대표님 피드백 (2026-04-21):
    "knight_portrait_rev1_2026-04-21.png 이건 너무 베르세르크고"

수정 방향:
    - "Kentaro Miura" / "Berserk Griffith" 키워드 제거
    - "Sephiroth FF7" 비중 강화 · Tetsuya Nomura / Yoshitaka Amano 추가
    - 모노크롬 → 컬러 (cool-toned · 은청 색조)
    - 차가운 크리스탈 블루 눈 강조 · 귀족적 우아함
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

PROMPT_PORTRAIT_REV2 = """Anime-style bust portrait of a young male warrior in full vibrant color,
long silver-white hair flowing past his shoulders with subtle cool blue sheen,
piercing crystalline blue eyes — cold, sharp, almost glowing from within,
androgynous bishounen beauty heavily inspired by Sephiroth from Final Fantasy VII,
cold handsome aristocratic face with refined sharp features,
pale skin with faint ethereal luminosity,
wearing an elegant dark high-collar guardian's attire with subtle silver filigree embroidery,
a hint of dark cloak on shoulders,
subtle cool-toned ethereal atmosphere, muted teal and silver color palette,
clean soft background with atmospheric light rays,
front three-quarter view, slight turn of the head,
art direction inspired by Tetsuya Nomura and Yoshitaka Amano,
Final Fantasy VII Remake illustration style meets Japanese seinen anime,
highly detailed luminous eyes, detailed flowing hair with individual strands,
cinematic soft lighting, volumetric glow, subtle bloom,
vibrant but cool color grading, masterpiece illustration, 4K"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=ART_DIR)
    out_path = ART_DIR / "knight_portrait_rev2_2026-04-21.png"

    print(f"[GEN] portrait rev2 -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_PORTRAIT_REV2, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
