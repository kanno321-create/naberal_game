"""세계 지도 Rev.1 생성 — 대표님 손그림 + 참조 스타일 (Inkarnate-like).

대표님 지시 (2026-04-21):
    "손그림으로 그린 지도를가지고 나노바나나로 지도를 작성 /
     우리컨셉 넣어서 만들고 진짜 지도처럼 산맥, 강, 바다, 사막, 눈덮힌 지형,
     등등 아주 세밀한 길도 어느정도 넣어서 / 참조 이미지 스타일"

세계관 반영 (발언 5·6·19·24 등):
    - 2 대륙 끝자락 이어짐
    - 서쪽 대륙: 서구 중세 · 강 많음 · 풍요 · 보라 제국 + 작은 왕국들
    - 동쪽 대륙: 이슬람풍 · 사막 대부분 · 강 적음 · 수도 + 직할자치구
    - 북쪽 얼음섬: 무인 · 초고대 유산
    - 중간 작은 섬: 항구 (북쪽 유일 접근) · 여러 종족 공생 · 무법·해적
    - 하단 지협: 두 대륙 연결 길
    - 대륙 주변 작은 섬들: 숨은 보스·던전
    - 북쪽 해역: 험한 물길·암초·몬스터 (접근 불가)

지명:
    - 대표님 "이름 너무 많네 ㅡ.ㅡ" 상태로 고유명 미정
    - 영문 descriptive 일반명만 사용 (추후 한글 고유명으로 교체 가능)
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

PROMPT_WORLD_MAP = """A highly detailed hand-painted fantasy world map,
Inkarnate-style cartography rendered on aged parchment background,
horizontal landscape composition, top-down bird's-eye view,

WORLD LAYOUT (critical structure):
- Two large continents positioned left (west) and right (east) of the map,
  their southern tips connected by a narrow land bridge (isthmus) at the bottom center,
  forming a roughly horseshoe shape
- North above both continents: treacherous ocean with dangerous rocky shoals,
  scattered reefs, and sea monster illustrations (making northern approach impassable)
- Directly NORTH at the top center of the map: a large frozen ICE ISLAND,
  white snow-covered terrain, jagged glaciers, deep blue icy waters around it,
  a single visible harbor/port on its southern edge
- Between the two main continents, in the central sea (middle of map):
  a small but important island with a marked harbor town
  (this is the ONLY port that can reach the northern ice island)
- Around both continents, scattered SMALL ISLANDS dotting the surrounding sea
  (marked with tiny fortress or ruin icons representing hidden dungeons)

WESTERN CONTINENT (left side) — medieval European fantasy feel:
- Rich lush greenery, dense forests with tree cluster patches
- Many branching rivers flowing from inland mountains to the coast
- A grand mountain range along the northern coast
- Multiple small kingdoms marked with castle icons and thin colored borders
- One prominent PURPLE-MARKED capital city (the great empire) roughly in the central-west
- Smaller castle icons scattered (the minor kingdoms)
- Rolling plains, farmland patches, small towns
- Clear road/trail networks connecting cities (thin dashed lines)

EASTERN CONTINENT (right side) — Middle Eastern / desert feel:
- Dominant pale tan DESERT with undulating dune patterns
- Very few thin short rivers that don't reach far inland
- Scattered oasis green patches
- A single prominent BLACK-MARKED capital city (the sultanate)
  roughly in the central-east
- Smaller settlement dots labeled as direct-controlled districts (not separate kingdoms)
- Coastal mountains on the eastern edge
- Sparse road networks crossing the desert between oases

THE LAND BRIDGE (bottom center):
- A narrow orange-brown causeway connecting the two continents at their southern tips
- Marked with a clear trail/road line crossing the bridge

CENTRAL ISLAND (middle of map):
- A small circular island with a clear port icon (ship symbol) on its south side
- A label indicating it is the harbor isle
- A thin dashed trade route line going up to the northern ice island
- Small ship illustrations in the surrounding waters

NORTHERN ICE ISLAND (top):
- Large landmass covered in snow and ice
- Jagged frozen mountain peaks
- A mysterious ancient ruin icon at its center (the ancient crystal/relic)
- No roads, no settlements
- Surrounding icy waters with drifting icebergs

MAP DETAILS:
- Compass rose in a corner (upper right)
- A decorative legend box listing: Capitals, Ports, Ruins, Kingdoms
- Scale bar at the bottom (miles)
- Ornate decorative border around the whole map
- Cloud/wind illustrations at the far edges of the ocean
- Aged parchment texture across the entire map
- Hand-drawn ink linework with painted color fills
- Descriptive English labels only in elegant fantasy serif font:
  "Western Realms", "Eastern Sands", "Northern Frozen Isle",
  "Merchant's Isle", "Sea of Storms" (north), "Bridge of Passage" (south)
  NO specific proper nouns for individual kingdoms or cities (leave symbols only)

STYLE:
- Inkarnate-style rendered cartography, painted fantasy map
- Aged parchment background with subtle stains and wear
- Hand-painted texture with visible brushwork
- Muted warm earth tones for land, cool blue-teal for water,
  white for ice, pale tan for desert, rich green for forests,
  grey for mountains with white snow caps on northern peaks
- Very high detail level — visible individual mountain peaks,
  river branch patterns, forest tree clusters, desert dune lines,
  small settlement icons, road networks, ship illustrations
- Professional TTRPG / video game world map quality,
  reminiscent of Middle-earth, Westeros, and Azeroth cartography

4K masterpiece, fantasy cartography, top-down world map illustration"""


def main() -> int:
    if not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")):
        print("ERROR: API key not found", file=sys.stderr)
        return 1

    adapter = NanoBananaAdapter(output_dir=MAPS_DIR)
    out_path = MAPS_DIR / "world_map_fantasy_rev1_2026-04-21.png"

    print(f"[GEN] world map rev1 -> {out_path.name}", flush=True)
    try:
        saved = adapter.generate_scene(prompt=PROMPT_WORLD_MAP, output_path=out_path)
        print(f"  [OK] saved: {saved}", flush=True)
        return 0
    except Exception as err:
        print(f"  [FAIL] {err}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
