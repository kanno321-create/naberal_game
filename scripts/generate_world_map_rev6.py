"""세계 지도 Rev.6 — 모든 왕국·자치구 위치 + 이름 라벨.

대표님 지시 (2026-04-21):
    "왕국과 제국위치라던지, 우측대륙도 수도와 자치구 내가 말한 수량대로
     위치선정하고 이름도 가따붙혀라 지도에,,
     그리고 수도만 크게 그려넣으니까 맵이 엄청좁아보이네"
    "지명은 영문으로만"

수정:
    - Rev.5 지리·스타일 유지
    - Elucia: 11 정치 단위 모두 위치 + 영문 라벨
      (Solaris 수도 + Vaelin·Moran·Ilaris·Ceren·Thaloss·Oryn·Maerith·Sylren·Novas·Aldric 10 왕국)
    - Karzor: 15 정치 단위 모두 위치 + 영문 라벨
      (Zarahim 수도 + 14 자치구)
    - 수도는 크게, 나머지는 작은 심볼 + 작은 이름 라벨
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

PROMPT_WORLD_MAP_REV6 = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,
map is densely populated with settlement labels, NOT sparse.

WORLD LAYOUT (keep Rev.5 geography):

TOP: NORTHERN FROZEN ISLAND labeled "VEILGLASS" — large irregular landmass,
snow and ice, jagged peaks, ancient ruin icon at center, drifting icebergs.

UPPER: elongated west-east ISLAND labeled "NOMEN" close to Veilglass,
prominent port icon on its south side, dashed route up to Veilglass.

MIDDLE: wide ocean labeled "VEIL SEA" with reefs, shoals, sea monsters,
clearly separating Nomen from the continents below.

LOWER TWO-THIRDS: two main continents MOSTLY SEPARATE,
connected only at the southernmost tips by a thin narrow land bridge "AZIM PASS",
with a central sea channel labeled "STRAIT OF NOMEN" running down between them.

WESTERN CONTINENT labeled large "ELUCIA" — medieval European kingdoms realm:
- Lush green forests, rolling plains, many branching rivers
- Grand mountain range across north-central with snow caps
- Rugged irregular coastline
- POLITICAL SEATS (all with English labels next to small crown/castle icons):
  * "Solaris" — LARGE PURPLE CROWN (Sacred Empire capital) in the west-central area
  * "Vaelin" — small crown icon, northern plains area
  * "Moran" — small crown icon, northwest coast
  * "Ilaris" — small crown icon, western coastal area
  * "Ceren" — small crown icon, southwest wetlands
  * "Thaloss" — small crown icon, northern mountains
  * "Oryn" — small crown icon, eastern forest
  * "Maerith" — small crown icon, northeastern highlands
  * "Sylren" — small crown icon, south-central plains
  * "Novas" — small crown icon, southeast border
  * "Aldric" — small crown icon, southwest lake area
- Faint colored border lines between kingdoms
- Road networks (thin dashed lines) connecting towns
- Small village and farm icons along river valleys

EASTERN CONTINENT labeled large "KARZOR" — desert realm:
- Dominant pale tan desert with dune patterns, scattered oasis patches
- A few short rivers, rugged coastal mountains on east and southeast
- POLITICAL SEATS (all with English labels next to small dome/palace icons):
  * "Zarahim" — LARGE BLACK DOMED PALACE (Karzor Dynasty capital) in east-central
  * "Amash" — small dome icon, northern oasis
  * "Qorath" — small dome icon, northeastern harbor
  * "Serak" — small dome icon, central desert
  * "Nahir" — small dome icon, eastern area
  * "Izar" — small dome icon, southeast
  * "Thari" — small dome icon, southwest desert
  * "Morak" — small dome icon, southern oasis
  * "Jalim" — small dome icon, northwestern mountains
  * "Azim" — small dome icon, eastern coast
  * "Tilnar" — small dome icon, central desert area
  * "Vashir" — small dome icon, southern harbor
  * "Rakhel" — small dome icon, northern trade route
  * "Omari" — small dome icon, central-east
  * "Sabin" — small dome icon, western border near Azim Pass
- All connected by sparse desert trade roads between oases (dashed lines)
- No independent borders (all under central rule)

MAIN REGION LABELS:
- "Veilglass" (ice island)
- "Nomen" (upper island)
- "Veil Sea" (northern ocean)
- "Elucia" (western continent)
- "Karzor" (eastern continent)
- "Strait of Nomen" (central sea)
- "Azim Pass" (southern bridge)

DECORATIONS:
- Ornate decorative border around the map
- Compass rose in upper-right corner
- Detailed LEGEND BOX side:
  Sacred Empire Capital (purple crown),
  Karzor Dynasty Capital (black dome),
  Kingdom Seats (crown),
  Karzor Districts (dome),
  Ports, Ruins, Dungeons, Trade Roads
- Scale bar at the bottom
- Ship illustrations, sea monsters in Veil Sea
- Small dungeons/ruins icons scattered on outlying small islands

STYLE:
- Inkarnate-style painted fantasy cartography
- Aged parchment background with hand-painted texture
- Muted warm earth tones, blue-teal water, white ice, pale tan desert,
  rich green forests, grey mountains with white snow caps
- Very high detail — densely populated with settlement labels,
  making the continents look FULL rather than empty
- Elegant fantasy serif font for all English labels
- Professional TTRPG / video game world map quality,
  reminiscent of Middle-earth, Westeros, Azeroth cartography

4K masterpiece, fantasy cartography,
KEY EMPHASIS: map densely populated with ALL eleven Elucia seats (1 capital + 10 kingdoms)
and ALL fifteen Karzor seats (1 capital + 14 districts), each clearly labeled with English name,
continents feel RICH and LIVED-IN, not sparse,
two continents mostly separate with thin Azim Pass bridge only at southernmost tips"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev6_2026-04-21.png"

    print(f"[GEN] world map rev6 (all 26 polities labeled) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP_REV6, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
