"""세계 지도 Rev.5 — 두 대륙 대부분 분리 · 최남단만 얇은 육교로 연결.

대표님 피드백 (2026-04-21):
    Rev.4 평가:
    "아 좋긴좋은데 살짝아쉽다 / 지도가 하단에 대륙두개가 끝만살짝 붙어있어야하는데,
     완전 붙어버렸네 / 나머지는 좋은데"

수정 핵심:
    - 두 대륙은 중앙 해협(Strait of Nomen) 이 북쪽부터 남쪽까지 쭉 분리
    - 최남단 끝만 얇은 Azim Pass 육교로 연결
    - 두 대륙은 fused 아님 — 거의 독립된 대륙
    - 나머지 요소 전부 Rev.4 와 동일 유지
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
MAPS_DIR = GAME_ROOT / "wiki" / "design" / "maps"
MAPS_DIR.mkdir(parents=True, exist_ok=True)

PROMPT_WORLD_MAP_REV5 = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,

WORLD LAYOUT:

TOP of map: NORTHERN FROZEN ISLAND "VEILGLASS" —
a very large irregular landmass with complex shape, multiple peninsulas, deep inlets,
covered in snow, glaciers, jagged frozen mountain peaks,
an ancient mysterious ruin icon at its center,
drifting icebergs in surrounding icy blue-white waters.

UPPER PORTION (just below Veilglass):
the small elongated HORIZONTAL ISLAND "NOMEN" (west-east oriented, long narrow bar),
positioned CLOSE to Veilglass with a thin dashed trade route line connecting them —
this is the ONLY viable northern approach.
Nomen has a prominent port town icon on its southern side.

MIDDLE PORTION: a WIDE TREACHEROUS OCEAN labeled "Veil Sea"
filled with rocky shoals, reefs, sea monster illustrations,
making direct northern approach from the continents impossible.
Clearly visible wide water body separating Nomen from the continents below.

LOWER TWO-THIRDS: the two main continents.

CRITICAL — CONTINENT SEPARATION (most important this revision):
- The two continents are MOSTLY SEPARATE — they are NOT fused or overlapping
- A clear SEA CHANNEL ("Strait of Nomen") runs from the Veil Sea at the top
  ALL THE WAY DOWN between the two continents, almost reaching the bottom of the map
- ONLY AT THE VERY BOTTOM TIPS, the two continents' southernmost points
  touch through a NARROW THIN LAND BRIDGE labeled "Azim Pass"
- The Azim Pass is a slim, narrow isthmus — visible as a thin causeway,
  NOT a wide connected landmass
- Think of it like a horseshoe: two continents descending southward,
  nearly separate, touching only at the very tips
- The central sea channel between them is wide and open for most of its length,
  narrowing only right before the Azim Pass at the bottom

WESTERN CONTINENT "ELUCIA" (left side of the lower map) — Medieval European kingdoms:
- Lush green forests, rolling plains, many branching rivers
- Large northern peninsula reaching upward toward the Veil Sea
- Grand mountain range across the north-central area with snowy peaks
- Fjord-like northern coast with offshore islets
- Rugged southwestern coast
- ONE PROMINENT GRAND CAPITAL with a PURPLE CROWN symbol in the west-central area,
  labeled "Solaris"
- TEN SMALLER CASTLE/CROWN icons scattered representing ten kingdoms
- Faint colored border lines between kingdoms
- Road networks (thin dashed lines) connecting cities
- Small villages and farms along river valleys
- Southern tip of Elucia reaches down toward the Azim Pass

EASTERN CONTINENT "KARZOR" (right side of the lower map) — desert realm:
- Dominant pale tan DESERT with undulating dune patterns
- Scattered green oasis patches
- A few thin short rivers not reaching deep inland
- Rugged coastal MOUNTAIN RANGE on east and southeast
- ONE PROMINENT CAPITAL with a BLACK DOMED PALACE symbol in the east-central area,
  labeled "Zarahim"
- FOURTEEN SMALLER DOMED/PALACE icons scattered representing direct districts
  (no independent borders — all under central rule, connected by trade roads)
- Rugged eastern coastline with offshore islands
- Sparse desert roads
- Southern tip of Karzor reaches down toward the Azim Pass

BOTH CONTINENTS HAVE HIGHLY IRREGULAR RUGGED organic coastlines (NOT smooth).

SCATTERED SMALL ISLANDS around both continents:
numerous offshore islands dotted across the seas,
marked with tiny fortress, tower, or ruin icons (dungeons).

MAP LABELS (elegant fantasy serif font, English):
- "Veilglass" on the northern ice island
- "Nomen" on the elongated upper island
- "Veil Sea" across the wide northern ocean
- "Elucia" large across the western continent
- "Karzor" large across the eastern continent
- "Solaris" under the western purple capital crown
- "Zarahim" under the eastern black dome capital
- "Strait of Nomen" labeled in the central sea between the two continents
- "Azim Pass" at the southern thin land bridge

MAP DECORATIONS:
- Ornate decorative border around the entire map
- Compass rose in upper-right corner
- LEGEND BOX on the side
- Scale bar at the bottom
- Cloud and wind illustrations at ocean edges
- Ship illustrations in various seas
- Sea monsters in the Veil Sea

STYLE:
- Inkarnate-style painted fantasy cartography
- Aged parchment background, hand-painted texture with visible brushwork
- Muted warm earth tones for land, blue-teal for water, white ice, pale tan desert,
  rich green forests, grey mountains with white snow caps
- Very high detail, professional TTRPG / video game world map quality

4K masterpiece, fantasy cartography, top-down world map illustration,
KEY EMPHASIS: two continents are mostly separate with a wide central strait running down,
touching ONLY at the very southernmost tips through a thin narrow Azim Pass land bridge,
horseshoe-shaped world layout"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev5_2026-04-21.png"

    print(f"[GEN] world map rev5 (continents mostly separate, thin bridge only) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP_REV5, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
