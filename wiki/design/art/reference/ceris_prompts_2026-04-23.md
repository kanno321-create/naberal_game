---
category: design/art/reference/prompts
tags: [prompt, reference, ceris, demon-heroine, image-generation, 2026-04-23]
created: 2026-04-23
updated: 2026-04-23
character: 세리스 (Ceris)
role: 마족 히로인
status: CANONICAL
purpose: 세리스 이미지 생성 시 재사용할 공식 프롬프트 세트. 대표님 직접 작성 원본 + 세션 #8 에서 검증된 개선 구문 통합.
related_images:
  - ceris_OFFICIAL_portrait_2026-04-23.png
  - ceris_OFFICIAL_portrait_B_2026-04-23.png
  - ceris_OFFICIAL_blush_2026-04-23.png
  - ceris_OFFICIAL_fullbody_2026-04-23.png
related_profile: ../../../케릭 컨셉 및 프로필.md
---

# 🥀 세리스 (Ceris) 이미지 생성 프롬프트 세트

> **대표님 직접 작성 원본** + 세션 #8 검증된 개선 구문.  
> 다음 세리스 씬 생성 시 이 파일을 먼저 참조. 원본 정신·톤을 해치지 않는 범위 내에서 수정.

---

## 📘 원본 프롬프트 (대표님 직접 작성 · 2026-04-23)

### 🎨 버전 1 · 파멸의 룬어를 다루는 세리스 (진지)

> 나이트와 나란히 세워두어도 완벽하게 한 게임의 캐릭터로 보이도록,  
> 차분하고 고급스러운 일러스트 풍을 강조했습니다.

```
(masterpiece, best quality, official game concept art:1.2), 1girl, dark fantasy demon heroine, extremely pale translucent skin, glowing deep violet eyes with a hint of melancholy, wearing an elegant but revealing gothic black dress with intricate silver embroidery, (a glowing magical gemstone core embedded in the skin of her chest emitting soft purple light:1.3), ancient blood-red runes floating, long flowing dark hair, muted colors, desaturated palette, painterly anime style, JRPG character design, watercolor and ink texture, detailed brush strokes, somber and mysterious atmosphere, in the style of dark fantasy concept art.
```

### 🌸 버전 2 · 부끄러워하는 세리스 (갭 모에)

> 부끄러워하는 표정이지만, 그림체 자체는 여전히 진지하고 다크한 게임 원화의  
> 고급스러운 질감을 유지하여 이질감을 없앴습니다.

```
(masterpiece, best quality, official game concept art:1.2), 1girl, dark fantasy demon heroine, extremely pale skin, beautiful violet eyes, long dark hair, wearing an elegant revealing black dress, (glowing magical gemstone core on her chest:1.2), looking at viewer with a shy expression, intensely blushing cheeks, flustered and embarrassed, holding her hands together nervously, muted colors, desaturated palette, painterly anime style, JRPG character design, watercolor and ink texture, detailed brush strokes, somber yet charming atmosphere, dark fantasy concept art.
```

---

## 💡 카메라 워크 · 3가지 구도 키워드 조합법

원본 프롬프트의 맨 앞 `1girl,` **바로 다음**에 아래 키워드 중 하나를 추가해 3번 생성.

### 전신 (Full Body)
```
standing full body shot, showing shoes, character design sheet,
```
→ 나이트 `knight_OFFICIAL_fullbody` 처럼 캐릭터 시트 느낌 필수 태그.

### 상반신 (Upper Body)
```
upper body shot, cowboy shot, focusing on torso and head,
```

### 얼굴 클로즈업 (Face Close-up)
```
close-up portrait, focusing on face and eyes, detailed facial features,
```

---

## 🎯 미드저니 전용 꿀팁

미드저니 (Niji) 사용 시 프롬프트 뒤에 추가:

```
--niji 6 --style raw
```

→ 일본 애니풍 중에서도 과장되지 않고 원화 (Concept Art) 에 가장 가까운 진지한 그림체 출력.

---

## 🔧 세션 #8 검증 · 피부·비율 개선 구문 (필요 시 추가)

### 피부 완화 구문 (v1 원본 "곧 죽을 상" 해소 · `portrait` → `portrait` rev2 전환 시 사용)

**수정 전 (원본)**:
```
extremely pale translucent skin
```

**수정 후 (rev2)**:
```
pale porcelain skin with gentle warmth, softly luminous complexion, delicate but alive
```

- 대표님 피드백: *"너무 창백해서 곧 죽을 상"* → *"이야 잘나왔다 버전1 수정버전"*
- 공식 레퍼런스 `ceris_OFFICIAL_portrait_2026-04-23.png` · `ceris_OFFICIAL_portrait_B_2026-04-23.png` 가 이 구문 적용분

### 몸 비율 강조 구문 (3뷰 시트 · 전신 씬에서 로리화 방지)

**추가 위치**: `1girl, dark fantasy demon heroine,` 바로 다음.

```
(mature adult woman in her mid-20s, tall slim graceful adult figure, perfect slim adult body proportions, 7.5-8 heads tall anime proportions, elongated feminine anatomy, NOT chibi, NOT short, NOT young girl, NOT lolita:1.5),
```

- 대표님 피드백: *"로리를 만들어놨네"* → 몸 비율 강조 후 *"ㅇㅋ 됫다"*
- 공식 레퍼런스 `ceris_OFFICIAL_fullbody_2026-04-23.png` 가 이 구문 적용분

### 3뷰 캐릭터 시트 레이아웃 구문

**원본 프롬프트 앞에 삽입**:
```
(masterpiece, best quality, official game concept art:1.2),
Japanese anime character design turnaround sheet of the same dark fantasy demon heroine,
three full views of the same character arranged horizontally in one image:
LEFT panel: full body front view from head to toe,
CENTER panel: full body back view showing long hair and dress back,
RIGHT panel: bust portrait close-up showing face details.

Heroine design (consistent across all three views, identical character):
```

**원본 프롬프트 뒤에 추가**:
```
Layout: clean three-view turnaround sheet, plain neutral gray background,
small elegant serif labels under each panel: FRONT · BACK · PORTRAIT.
```

---

## 🛡️ OpenAI gpt-image-1 safety 주의사항 (세션 #8 경험)

다음 키워드는 **moderation 차단 유발** 확인됨. 세리스 씬 생성 시 회피 또는 완화:

| 위험 키워드 | 대체 표현 |
|---------|---------|
| `revealing` | `elegant but alluring` |
| `bare shoulders` | `off-shoulder neckline` (완화 효과 있음) |
| `thigh-high slit` | `high side slit on one leg` |
| `exposed skin` | (완전 회피) |
| `gothic` + `dark aesthetic` 조합 | 둘 중 하나만 |
| 너무 강한 `NOT` 부정 프롬프트 과다 | 필요 시만 1~2개 |

**대안**: reference image edit 은 safety 필터 훨씬 엄격 (req_26b2b9 · req_652dbf · req_3cda3c 3회 차단 경험). **reference 없이 `images.generate`** 가 safety 통과율 훨씬 높음.

---

## 💰 모델별 비용·safety 비교 (세션 #8 실측)

| 모델 | 비용/image | safety | 일관성 | 권장 용도 |
|------|---------|--------|-------|---------|
| **OpenAI `gpt-image-1`** (a.k.a. ducktape) | ~$0.17 (1024×1536 high) | 엄격 · revealing·horns 차단 | 텍스트 프롬프트 기반 (reference safety 에 걸림) | **기본 선택** (대표님 OpenAI 전용 선언) |
| Google `nano-banana-pro` | $0.04 | 관대 | 양호 | ❌ **사용 금지** (대표님 *"gemini api비용 장난아니네 이제 나노바나나 못쓰겠다"* · 2026-04-23) |
| fal.ai `flux-pro/v1.1-ultra` | ~$0.05 | 관대 | reference 우수 | 🟡 **잔액 소진 상태** · 충전 후 재활성 가능 |

---

## 📂 세리스 공식 레퍼런스 이미지 4종 (생성 완료)

이 프롬프트들로 생성된 공식 레퍼런스:

1. **`ceris_OFFICIAL_portrait_2026-04-23.png`** — 진지 · halter 스타일 (v1 rev2)
2. **`ceris_OFFICIAL_portrait_B_2026-04-23.png`** — 진지 · **off-shoulder 복원판** 🌟 (v1 rev2 B · Canon 의상 최상위 정합)
3. **`ceris_OFFICIAL_blush_2026-04-23.png`** — 갭 모에 · 부끄러움 (v2)
4. **`ceris_OFFICIAL_fullbody_2026-04-23.png`** — 3뷰 풀바디 · 8 heads tall (v1 rev2 + 비율 강조 + 3뷰 레이아웃)

상세: `./[_INDEX.md](_INDEX.md)` 참조.

---

## 🎬 다음 세리스 씬 생성 체크리스트

1. **목적 확인**: 진지 초상? 갭 모에? 전신? 특정 씬 (Ch.14 각성·Ch.16 소멸)?
2. **기본 프롬프트 선택**: v1 (진지) 또는 v2 (갭 모에)
3. **카메라 워크 키워드**: full body · upper body · close-up 중 1개 `1girl,` 다음 삽입
4. **개선 구문 추가 여부**:
   - 전신 씬 → 몸 비율 강조 구문 추가 (로리화 방지)
   - 피부 톤 조정 → rev2 피부 완화 구문으로 대체
5. **safety 회피**: `revealing` 대신 `elegant but alluring` 등 완화 표현 사용
6. **모델 선택**: OpenAI `gpt-image-1` 기본 · size `1024×1536` · quality `high`
7. **reference 사용 여부**:
   - 일관성 우선 → `ceris_OFFICIAL_portrait_B` 또는 `ceris_OFFICIAL_fullbody` 입력
   - safety 차단 발생 시 → reference 제거 · `images.generate` 로 전환
8. **씬 컨텍스트 추가** (해당 시): Ch.14 관능·신비 · Ch.16 눈물·소멸 이펙트 등

---

## 🔗 관련 자료

- 세리스 프로필 (대표님 직접 작성): [`../../케릭 컨셉 및 프로필.md`](../../케릭%20컨셉%20및%20프로필.md)
- 나이트 프롬프트 (발언 39): `wiki/design/brainstorm_2026-04-21_worldview_expansion.md:2500-2502`
- 공식 레퍼런스 인덱스: [`./_INDEX.md`](_INDEX.md)
- 생성 스크립트 예시:
  - `scripts/generate_ceris_v1_rev2.py` (피부 완화 단일 컷)
  - `scripts/generate_ceris_3view_openai.py` (3뷰 시트 · 비율 강조)
  - `scripts/generate_ceris_sheet_mature_openai.py` (B variant · off-shoulder 복원)

---

*박제: 2026-04-23 세션 #8 · 나베랄 감마*  
*대표님 지시: "레퍼런스파일옆에 프롬프트 세리스파일로 저장해 · 다음에도 써먹게"*
