"""세계 지도 Rev.3 — 지명 + 11 + 15 정치 단위 심볼 반영.

대표님 지시 (2026-04-21):
    "대륙이름 섬들의 이름은 너가 좀 지어봐바 / 좌측대륙은 1 교황청 제국
     + 10 왕국, 우측은 1 수도 + 14 직할자치구"

추가 사항:
    - Rev.2 구조 유지 (양 대륙 근접 · 중간 섬 가로 길쭉 · 얼음섬 복잡)
    - 주요 지명 라벨 추가 (대륙·섬·해역)
    - 좌측: 11 왕관/성 심볼 (교황청 제국 1 + 10 왕국)
    - 우측: 15 돔/궁전 심볼 (수도 1 + 14 자치구)
    - 세부 왕국명·자치구명은 지도에 라벨 X (별도 문서 political_divisions.md)
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

PROMPT_WORLD_MAP_REV3 = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography rendered on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,

WORLD LAYOUT (must match exactly):

TWO LARGE CONTINENTS arranged left and right, VERY CLOSE together,
separated only by a narrow central sea channel,
their southern tips connected by a narrow land bridge (isthmus).
Both continents have HIGHLY IRREGULAR RUGGED organic coastlines
with many peninsulas, bays, coves, and offshore islets.

WESTERN CONTINENT "OSTVARIA" (left side) — Medieval European kingdoms:
- Lush green forests, rolling plains, many branching rivers forming a dense network
- Large northern peninsula jutting toward the top-left
- Grand mountain range across the north-central area with snowy peaks
- Fjord-like northern coast with offshore islets
- Rugged southwestern coast
- ONE PROMINENT GRAND CAPITAL CITY marked with a PURPLE CROWN symbol
  in the west-central area — this is the Sacred Empire's capital (label: "Aurelia")
- TEN SMALLER CASTLE/CROWN icons scattered across the continent
  representing ten kingdoms, each with faint colored border lines between them
- Roads (thin dashed lines) connecting cities
- Small villages and farms along river valleys

EASTERN CONTINENT "KHALEQAR" (right side) — Middle Eastern desert realm:
- Dominant pale tan DESERT with undulating dune patterns
- Scattered green oasis patches
- A few thin short rivers not reaching deep inland
- Rugged coastal mountains on the east
- ONE PROMINENT CAPITAL CITY marked with a BLACK DOMED PALACE symbol
  in the east-central area along a river (label: "Al-Kharaam")
- FOURTEEN SMALLER DOMED/PALACE icons scattered representing direct districts
  (no independent borders — all under central rule, connected by trade roads)
- Rugged eastern coastline with offshore islands
- Sparse desert roads between oases

CENTRAL STRAIT (between continents):
- Narrow sea channel
- LONG ELONGATED HORIZONTAL ISLAND in the middle (west-east oriented)
  with a prominent port town marked "Verra"
- A thin dashed trade route line going from Verra UP to the northern frozen isle
- Small ship illustrations in surrounding waters

NORTHERN FROZEN ISLAND at the top:
- VERY LARGE landmass with highly irregular complex shape,
  multiple peninsulas and deep inlets
- Covered in snow and ice, jagged frozen mountain peaks
- Ancient mysterious ruin icon at center
- Label: "Niferglas"
- Drifting icebergs in icy waters around it

NORTHERN OCEAN (top edge):
- Label: "Sea of Fangs"
- Treacherous waters with rocky shoals, reefs, and sea monster illustrations
- No direct passage from northern coasts of either continent

LAND BRIDGE (bottom center):
- Orange-brown narrow isthmus connecting southern tips
- Label: "Luth Causeway"
- Trail crossing with small settlement icons

SCATTERED SMALL ISLANDS around both continents:
- Numerous offshore islands with tiny fortress, tower, or ruin icons (dungeons)
- Some with wild forest patches

MAP LABELS (elegant fantasy serif font, English):
- "Ostvaria" large across the western continent
- "Khaleqar" large across the eastern continent
- "Aurelia" under the western purple capital
- "Al-Kharaam" under the eastern black capital
- "Niferglas" on the northern ice island
- "Verra" on the central elongated island
- "Sea of Fangs" in the northern ocean
- "Luth Causeway" at the southern land bridge
- "Strait of Verra" in the central sea

MAP DECORATIONS:
- Ornate decorative border around the entire map
- Compass rose in upper-right corner
- LEGEND BOX on the side listing:
  "Sacred Empire Capital (purple crown)",
  "Sultanate Capital (black dome)",
  "Kingdom Seats (crown)",
  "Sultanate Districts (dome)",
  "Ports (anchor)",
  "Ruins (tower)",
  "Dungeons (fortress)"
- Scale bar at the bottom
- Cloud and wind illustrations at ocean edges
- Ship illustrations in various seas
- Sea monsters in the northern waters

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
- Reminiscent of Middle-earth, Westeros, and Azeroth cartography

4K masterpiece, fantasy cartography, top-down world map illustration,
highly detailed rugged coastlines,
ELEVEN political symbols on the western continent (one prominent purple + ten smaller),
FIFTEEN political symbols on the eastern continent (one prominent black + fourteen smaller)"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev3_2026-04-21.png"

    print(f"[GEN] world map rev3 (names + 11+15 polities) -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP_REV3, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
