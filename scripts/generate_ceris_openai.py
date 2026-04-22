"""세리스 (마족 히로인) 초상 생성 — OpenAI Images API (세션 #7/#8 · 2026-04-23).

대표님 지시:
    버전 1: 파멸의 룬어를 다루는 진지한 세리스 (나이트 원화 스타일 맞춤)
    버전 2: 부끄러워하는 세리스 (갭 모에 · 나이트 원화 스타일 유지)

모델: gpt-image-1 (OpenAI 2025-04 출시 · 대표님이 "ducktape" 로 지칭하신 것과 동일 추정)
     - 환경 변수 `OPENAI_IMAGE_MODEL` 설정 시 해당 모델로 대체 (ducktape 별 ID 있으면 override)

세리스 Canon (케릭 컨셉 및 프로필.md · 2026-04-23):
    - 마족 히로인 · 마법 폭격기 · 파멸의 룬어
    - 창백 흰 피부 + 보랏빛 눈 + 흉부 마력 핵
    - 검은 드레스 · 뿔 제거 옵션 (이번 프롬프트)
    - 갭 모에: 유혹 척 → 진심에 새빨개짐

실행:
    python scripts/generate_ceris_openai.py
"""
from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

# --- .env 로드 (shorts/.env 에서 OPENAI_API_KEY 확보) ---
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

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai package not installed. Run: pip install openai", file=sys.stderr)
    sys.exit(1)

# --- 출력 디렉토리 ---
GAME_ROOT = Path(r"C:\Users\PC\Desktop\naberal_group\studios\game")
ART_DIR = GAME_ROOT / "wiki" / "design" / "art"
ART_DIR.mkdir(parents=True, exist_ok=True)

# --- 모델 선택 ---
MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
IMAGE_SIZE = os.environ.get("OPENAI_IMAGE_SIZE", "1024x1536")  # 세로 캐릭터 비율
IMAGE_QUALITY = os.environ.get("OPENAI_IMAGE_QUALITY", "high")

# --- 프롬프트 v1: 파멸의 룬어 진지 (나이트 원화 스타일) ---
PROMPT_V1_SERIOUS = """(masterpiece, best quality, official game concept art:1.2),
1girl, dark fantasy demon heroine,
extremely pale translucent skin,
glowing deep violet eyes with a hint of melancholy,
wearing an elegant but revealing gothic black dress with intricate silver embroidery,
(a glowing magical gemstone core embedded in the skin of her chest emitting soft purple light:1.3),
ancient blood-red runes floating,
long flowing dark hair,
muted colors, desaturated palette,
painterly anime style, JRPG character design,
watercolor and ink texture, detailed brush strokes,
somber and mysterious atmosphere,
in the style of dark fantasy concept art"""

# --- 프롬프트 v2: 부끄러워하는 갭 모에 (나이트 원화 스타일 유지) ---
PROMPT_V2_BLUSH = """(masterpiece, best quality, official game concept art:1.2),
1girl, dark fantasy demon heroine,
extremely pale skin,
beautiful violet eyes,
long dark hair,
wearing an elegant revealing black dress,
(glowing magical gemstone core on her chest:1.2),
looking at viewer with a shy expression,
intensely blushing cheeks, flustered and embarrassed,
holding her hands together nervously,
muted colors, desaturated palette,
painterly anime style, JRPG character design,
watercolor and ink texture, detailed brush strokes,
somber yet charming atmosphere,
dark fantasy concept art"""


def save_image(data_b64: str, out_path: Path) -> None:
    img_bytes = base64.b64decode(data_b64)
    out_path.write_bytes(img_bytes)


def generate_one(client: OpenAI, prompt: str, out_path: Path, label: str) -> tuple[str, str]:
    print(f"[GEN] {label} -> {out_path.name}", flush=True)
    try:
        resp = client.images.generate(
            model=MODEL,
            prompt=prompt,
            size=IMAGE_SIZE,
            quality=IMAGE_QUALITY,
            n=1,
        )
        # gpt-image-1 은 b64_json 반환 (url 없음)
        item = resp.data[0]
        if getattr(item, "b64_json", None):
            save_image(item.b64_json, out_path)
        elif getattr(item, "url", None):
            # DALL-E 3 fallback: url 다운로드
            import urllib.request
            urllib.request.urlretrieve(item.url, str(out_path))
        else:
            return (label, "FAIL: no image data in response")
        print(f"  [OK] saved: {out_path}", flush=True)
        return (label, "OK")
    except Exception as err:
        msg = f"FAIL: {type(err).__name__}: {err}"
        print(f"  [FAIL] {msg}", file=sys.stderr, flush=True)
        return (label, msg)


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found (expected in shorts/.env)", file=sys.stderr)
        return 1

    client = OpenAI()

    print(f"Model: {MODEL} · Size: {IMAGE_SIZE} · Quality: {IMAGE_QUALITY}", flush=True)
    print()

    jobs = [
        (
            ART_DIR / "ceris_v1_openai_2026-04-23.png",
            PROMPT_V1_SERIOUS,
            "버전 1 · 파멸의 룬어 진지",
        ),
        (
            ART_DIR / "ceris_v2_openai_2026-04-23.png",
            PROMPT_V2_BLUSH,
            "버전 2 · 부끄러워하는 갭 모에",
        ),
    ]

    results = []
    for out_path, prompt, label in jobs:
        results.append(generate_one(client, prompt, out_path, label))

    print("\n=== SUMMARY ===")
    for label, status in results:
        print(f"  [{status}] {label}")

    return 0 if all(s == "OK" for _, s in results) else 2


if __name__ == "__main__":
    sys.exit(main())
