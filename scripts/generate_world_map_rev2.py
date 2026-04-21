"""세계 지도 Rev.2 — 손그림 외형 충실 + Inkarnate 스타일 유지.

대표님 피드백 (2026-04-21):
    Rev.1 평가:
    - "이런 디자인으로 우리지도 그려봐" (스타일 OK)
    - "외형은 내가 만든지도랑 최대한 비슷하게해야되" (외형 조정 필요)

손그림 대비 Rev.1 차이 (나베랄 감마 관찰):
    - 양 대륙 간격 너무 넓음 → 매우 근접 (좁은 중앙 해협)
    - 북쪽 얼음섬 단순 원형 → 복잡 불규칙 (반도·갈래·돌출)
    - 중간 섬 작은 원형 → 가로 길쭉 (west-east elongated)
    - 대륙 경계 매끈 → 울퉁불퉁
    - 서쪽 북부 반도 돌출 추가 필요
    - 대륙 주변 작은 섬들 분포 강화
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

PROMPT_WORLD_MAP_REV2 = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography rendered on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,

CRITICAL WORLD LAYOUT (must match exactly):

TWO LARGE CONTINENTS arranged left and right, very close to each other —
they nearly touch at the bottom center where a narrow land bridge (isthmus)
connects their southern tips. The gap between them is a NARROW central strait,
not a wide ocean.

The continents have HIGHLY IRREGULAR RUGGED COASTLINES with many
small peninsulas, bays, coves, and offshore islets.
Do NOT draw smooth clean continent edges — they must look hand-drawn,
organic, wandering, with many bumps and inlets.

WESTERN CONTINENT (left side of map) — Medieval European kingdoms:
- Rich lush greenery, dense forests with tree cluster patches,
  rolling plains, and many branching rivers forming an extensive network
- A LARGE NORTHERN PENINSULA jutting upward toward the top-left
- A grand mountain range across the northern-central area with snowy peaks
- The northern coast has several fjord-like inlets and offshore islets
- Multiple small kingdoms marked with tiny castle icons scattered across
  with faint colored border lines between them
- One prominent PURPLE-MARKED capital city (the great empire) positioned
  in the west-central area
- Many smaller rivers snaking from mountains to the sea
- Farm patches and small towns along river valleys
- Clear road/trail networks (thin dashed lines) connecting cities
- Rugged southwestern coast with small offshore islands

EASTERN CONTINENT (right side of map) — Middle Eastern desert realm:
- Dominant pale tan DESERT with undulating dune patterns
- Scattered green oasis patches
- A FEW thin short rivers that do not reach deep inland
- Rugged coastal MOUNTAIN RANGE along the east and southeast edges
- One prominent BLACK-MARKED capital city (the sultanate) in the
  east-central area, along a major river
- Smaller settlement dots scattered (labeled as direct-controlled districts,
  not independent kingdoms) — castle/palace icons
- Rugged eastern coastline with many offshore islands
- Sparse road networks crossing the desert between oases

NARROW CENTRAL STRAIT (middle of map, between continents):
- The two continents are separated only by a narrow sea channel
- In the middle of this strait sits a LONG ELONGATED HORIZONTAL ISLAND
  (west-to-east oriented, like a long narrow bar)
- This island has a prominent PORT TOWN marked with a harbor/ship icon
  on its southern side
- A thin dashed trade route line goes up from this island's north shore
  reaching the northern frozen isle — this is the ONLY viable route north
- Small ship illustrations in the surrounding waters

NORTHERN FROZEN ISLAND (at the top of the map):
- A VERY LARGE landmass, much bigger than the central strait island
- Highly irregular complex shape — multiple peninsulas, deep inlets, jagged edges
- Covered in snow and ice, with jagged frozen mountain peaks
- An ancient mysterious ruin icon at its approximate center
- Drifting icebergs in surrounding icy blue-white waters
- No settlements, no roads — only the ancient ruin

NORTHERN OCEAN (top edge, above the two main continents):
- Treacherous waters with many rocky shoals, reefs, and dangerous rocks
- Sea monster illustrations scattered across
- No direct passage from the northern coasts of either main continent
  (these approaches are impossible)

THE LAND BRIDGE (bottom center):
- A narrow orange-brown isthmus connecting the southern tips of both continents
- Clear trail/road line crossing it
- Some small settlement icons along the bridge

SCATTERED SMALL ISLANDS around both continents:
- Numerous small offshore islands dotting the seas around both continents
- Many marked with tiny fortress, tower, or ruin icons representing dungeons
- Some with tree-cluster patches (untamed wilderness)

MAP DECORATIONS:
- Ornate decorative border around the entire map
- Compass rose in upper-right corner
- A decorative LEGEND BOX on the side listing:
  Capitals, Ports, Ruins, Kingdoms, Dungeons
- Scale bar at the bottom in miles
- Cloud/wind illustrations at far ocean edges
- Ship illustrations in various sea locations
- Sea monsters in the northern treacherous waters

LABELS (elegant fantasy serif font, English, descriptive only, NO proper nouns):
- "Western Realms" across the western continent
- "Eastern Sands" across the eastern continent
- "Northern Frozen Isle" at the top
- "Merchant's Isle" on the central island
- "Sea of Storms" labeled in the northern treacherous ocean
- "Bridge of Passage" at the land bridge

STYLE:
- Inkarnate-style rendered cartography, painted fantasy map aesthetic
- Aged parchment background with subtle stains and wear marks
- Hand-painted texture with visible brushwork
- Muted warm earth tones for land, cool blue-teal for water,
  white for ice, pale tan for desert, rich green for forests,
  grey for mountains with white snow caps on northern peaks
- Very high level of detail — individual mountain peaks visible,
  river branch patterns, forest tree clusters, desert dune lines,
  numerous small settlement icons, road networks, ship illustrations
- Professional TTRPG / video game world map quality,
  reminiscent of Middle-earth, Westeros, and Azeroth cartography

4K masterpiece, fantasy cartography, top-down world map illustration,
highly detailed rugged irregular coastlines, two continents close together with narrow strait"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev2_2026-04-21.png"

    print(f"[GEN] world map rev2 (faithful to hand drawing) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP_REV2, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
