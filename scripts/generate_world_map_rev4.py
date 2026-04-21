"""세계 지도 Rev.4 — 세트 B 네이밍 + 지리 전면 수정.

대표님 지시 (2026-04-21):
    - 네이밍: 세트 B 확정 (Elucia / Karzor / Solaris / Zarahim / Veilglass / Nomen)
    - 중앙섬(Nomen): 두 대륙보다 "위" 에 위치 · 얼음섬과 가까움
    - 북쪽 얼음섬(Veilglass): 두 대륙과 거리 벌림 (넓은 북쪽 해역)
    - "술탄" 용어 제거 → "성좌" 로 대체
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

PROMPT_WORLD_MAP_REV4 = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,

CRITICAL WORLD LAYOUT (vertical positioning is important):

TOP OF MAP: the NORTHERN FROZEN ISLAND "VEILGLASS" —
a very large irregular landmass with complex shape, multiple peninsulas, deep inlets,
covered in snow, glaciers, jagged frozen mountain peaks,
an ancient mysterious ruin icon at its center,
drifting icebergs in surrounding icy blue-white waters.

DIRECTLY BELOW Veilglass (still in the UPPER portion of the map, not the middle):
the small elongated HORIZONTAL ISLAND "NOMEN" (west-east oriented, long and narrow),
positioned CLOSE to Veilglass so a thin dashed trade route line connects Nomen's
north shore up to Veilglass — this is the ONLY viable northern approach.
Nomen has a prominent port town icon on its southern side.

BETWEEN Nomen and the two main continents below: a WIDE TREACHEROUS NORTHERN OCEAN
labeled "Veil Sea" (previously Sea of Fangs) —
filled with dangerous rocky shoals, reefs, sea monster illustrations,
making direct northern approach from the continents impossible.
This ocean must be visibly WIDE, clearly separating Nomen from the continents below.

LOWER HALF OF MAP: the two main continents sit in the southern two-thirds of the map,
positioned closer to the bottom than the top.

WESTERN CONTINENT "ELUCIA" (left side of the lower map) — Medieval European kingdoms:
- Lush green forests, rolling plains, many branching rivers
- Large northern peninsula reaching upward toward the Veil Sea
- Grand mountain range across the north-central area with snowy peaks
- Fjord-like northern coast with offshore islets
- Rugged southwestern coast
- ONE PROMINENT GRAND CAPITAL marked with a PURPLE CROWN symbol
  in the west-central area, labeled "Solaris"
- TEN SMALLER CASTLE/CROWN icons scattered representing ten kingdoms,
  each with faint colored border lines between them
- Road networks (thin dashed lines) connecting cities
- Small villages and farms along river valleys

EASTERN CONTINENT "KARZOR" (right side of the lower map) — desert realm:
- Dominant pale tan DESERT with undulating dune patterns
- Scattered green oasis patches
- A few thin short rivers not reaching deep inland
- Rugged coastal MOUNTAIN RANGE on east and southeast
- ONE PROMINENT CAPITAL marked with a BLACK DOMED PALACE symbol
  in the east-central area, labeled "Zarahim"
- FOURTEEN SMALLER DOMED/PALACE icons scattered representing direct districts
  (no independent borders — all under central rule, connected by trade roads)
- Rugged eastern coastline with offshore islands
- Sparse desert roads

BETWEEN THE TWO CONTINENTS: a narrow central strait labeled "Strait of Nomen"

THE TWO CONTINENTS TOUCH AT THE BOTTOM:
a narrow orange-brown LAND BRIDGE connecting their southern tips,
labeled "Azim Pass"

BOTH CONTINENTS HAVE HIGHLY IRREGULAR RUGGED organic coastlines with many
peninsulas, bays, and offshore islets (NOT smooth edges).

SCATTERED SMALL ISLANDS around both continents:
numerous offshore islands dotting the seas,
marked with tiny fortress, tower, or ruin icons (dungeons and hidden locations).

MAP LABELS (elegant fantasy serif font, English, large readable text):
- "Veilglass" on the northern ice island
- "Nomen" on the elongated central-upper island
- "Veil Sea" across the wide northern ocean
- "Elucia" large across the western continent
- "Karzor" large across the eastern continent
- "Solaris" under the western purple capital crown
- "Zarahim" under the eastern black dome capital
- "Strait of Nomen" in the central sea between the two continents
- "Azim Pass" at the southern land bridge

MAP DECORATIONS:
- Ornate decorative border around the entire map
- Compass rose in upper-right corner
- LEGEND BOX on the side listing:
  "Choir Capital (purple crown)",
  "Karzor Capital (black dome)",
  "Kingdom Seats (crown)",
  "Karzor Districts (dome)",
  "Ports (anchor)",
  "Ruins (tower)",
  "Dungeons (fortress)"
- Scale bar at the bottom
- Cloud and wind illustrations at ocean edges
- Ship illustrations in various seas
- Sea monsters in the Veil Sea

STYLE:
- Inkarnate-style painted fantasy cartography
- Aged parchment background with subtle wear marks
- Hand-painted texture with visible brushwork
- Muted warm earth tones for land, blue-teal for water,
  white for ice, pale tan for desert, rich green for forests,
  grey for mountains with white snow caps
- Very high level of detail — individual mountain peaks, river branches,
  forest tree clusters, desert dune lines, many settlement icons, roads
- Professional TTRPG / video game world map quality

4K masterpiece, fantasy cartography, top-down world map illustration,
CRITICAL: Nomen island is in the upper portion of the map close to Veilglass,
the two main continents are in the lower portion,
with a wide Veil Sea separating them — NOT a compressed layout"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev4_2026-04-21.png"

    print(f"[GEN] world map rev4 (set B + geography fixed) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP_REV4, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
