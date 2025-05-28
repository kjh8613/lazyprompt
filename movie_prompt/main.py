import tkinter as tk
from tkinter import ttk
import random


# ------------------------------ 🎬 장르/톤 ------------------------------
selected_nationalities = set()
nationality_description = {
    "한국인": "Korean woman",
    "일본인": "Japanese woman",
    "중국인": "Chinese woman with elegant features and poised posture, often embodying traditional grace and modern style",
    "서양인": "Western woman with diverse features, typically taller build and expressive facial structure, ranging from classic European to modern cosmopolitan"
}




genre_tone = {
    "드라마": "a realistic emotional scene with strong character focus",
    "공포": "a dark, unsettling scene filled with fear and tension",
    "명상": "a peaceful, slow-paced scene with gentle visuals and sound",
    "액션": "a fast-paced, high-energy scene with dynamic motion",
    "포스트 아포칼립스": "a bleak, ruined world after a global catastrophe",
    "사이버펑크": "a neon-lit dystopian city filled with cybernetic life",
    "로우파이 감성": "a nostalgic, cozy scene with soft colors and ambient noise",
    "뮤직비디오 스타일": "a highly stylized, rhythmic scene with performance elements",
    "몽환적 분위기": "a dreamlike, surreal setting with soft light and blurred edges",
    "비현실적인 유토피아": "a bright, idealized world with perfect harmony and nature",
    "레트로 VHS 스타일": "a grainy 80s/90s tape aesthetic with color bleed and noise",
    "실험 영화": "a non-narrative, visually abstract scene with unconventional flow",
    "영웅 서사시": "an epic, large-scale scene with legendary characters and grand stakes",
    "중세 판타지": "a gritty, sword-and-magic world inspired by medieval Europe",
    "요괴/귀신물": "a traditional folklore horror scene with spirits or supernatural beings",
    "고독한 탐험자": "a silent scene of a lone wanderer in a vast unknown landscape",
    "심리 스릴러": "a tense, mind-bending scene with inner conflict and mental tension",
    "시네마 베리떼": "a raw, handheld-camera style scene with documentary realism",
    "무드필름": "a stylized mood piece focusing on visuals and emotions over story",
    "잔잔한 일상": "a quiet slice-of-life moment with soft pacing",
    "초현실주의": "a surreal visual world with dream logic and impossible geometry",
    "필름 누아르": "a shadowy noir scene with high contrast and vintage aesthetics",
    "북유럽 감성": "a minimalistic Scandinavian mood with cold lighting and slow rhythm",
    "고전 시대극": "a period drama with historical costumes and atmospheric tone",
    "흑백 아트 필름": "an artistic black-and-white film with silent emotion",
    "네오 느와르": "a modern noir with neon lights, rain, and psychological depth",
    "아시아 미니멀리즘": "a meditative, spatially restrained Asian cinematic style",
    "텍사스 웨스턴": "a dust-filled, heatwave-infused western scene with standoffs",
    "마녀/주술물": "a mystical setting with witches, sigils, and forest rituals",
    "로맨틱 판타지": "a dreamy fantasy world with soft magic and heartfelt gazes",
    "고스 어반": "a gothic urban scene with cathedral shadows and dark romance",
    "미로 구조": "a complex spatial tone with layered architecture and camera movement",
    "극단적 슬로우모션": "an ultra slow-motion scene highlighting every micro emotion",
    "긴장된 정적": "a still frame charged with suspense and invisible pressure",
    "인스타 감성": "a modern, polished aesthetic with lens flare and curated lifestyle",
    "틱톡 풍 뮤직쇼": "a punchy, rhythm-driven aesthetic with fast cuts and dance",
    "인디 감성": "a lo-fi, naturalistic tone with imperfect beauty and human warmth",
    "수묵화 스타일": "an East Asian ink painting-inspired motion with fading transitions",
    "밤의 하이라이트": "a nightlife-focused neon-filled, beat-driven nighttime visual",
    "숲속 몽환극": "a dreamy forest play with fog, fairy lights, and whimsy",
    "무성 영화 스타일": "a silent-era film with intertitles, film scratches, and piano",
    "디스토피아 감시사회": "a surveillance-heavy, cold dystopia filled with concrete and drones",
    "인물 초점 드라마": "a character-driven narrative with close psychological intensity",
    "아방가르드 실험극": "a non-linear, symbolic, abstract art piece with challenging visuals"
}


background = {
    "폐공장": "an abandoned factory with rusted steel beams and broken windows",
    "해변": "a tranquil beach with gentle waves and soft golden sand",
    "붉은 숲": "a dense forest with crimson foliage and filtered sunlight",
    "유리온실": "a glass greenhouse with lush plants and warm humidity",
    "낡은 체육관": "an old gymnasium with creaky floors and faded equipment",
    "도시 고가도로 아래": "under an urban overpass with flickering streetlights",
    "기차역 플랫폼": "a quiet train station platform with distant announcements",
    "안개 낀 묘지": "a foggy graveyard with moss-covered stones and eerie silence",
    "푸른 밀밭": "an expansive green wheat field swaying in the wind",
    "고속도로 휴게소": "a lonely rest stop along the highway at dusk",
    "전쟁터 폐허": "a ruined battlefield littered with broken armor and smoke",
    "기괴한 미술관 내부": "an uncanny art museum interior with distorted exhibits",
    "유령이 나올 것 같은 놀이공원": "an abandoned amusement park with creaking rides and eerie echoes",
    "전등 하나만 켜진 다락방": "an attic lit by a single bulb casting long shadows",
    "장마철 골목": "a rain-soaked alleyway with puddles and neon reflections",
    "바닷가 절벽 위": "atop a seaside cliff with crashing waves below",
    "사막 오아시스": "a desert oasis with palm trees and shimmering water",
    "밤의 골목길": "a narrow night alley glowing with scattered neon signs",
    "천장이 유리로 된 현대 미술관": "a modern art museum with a glass ceiling and soft gallery lighting",
    "무대 리허설장": "a theater rehearsal space with marked floors and stage lights",
    "컨테이너 창고": "a shipping container warehouse with stacked crates and dim lighting",
    "비상계단": "a metallic emergency staircase spiraling down a building",
    "가정집 거실 (90년대풍)": "a cozy 90s-style living room with warm tones and vintage decor",
    "공사 중인 빌딩 내부": "inside an unfinished building with scaffolding and exposed wiring",
    "수몰된 도시": "a submerged cityscape with partially visible rooftops",
    "종이등불이 날리는 축제 거리": "a festive street with floating paper lanterns and colorful banners",
    "고층 빌딩의 유리 엘리베이터 안": "inside a high-rise glass elevator overlooking a city",
    "네온사인으로 가득한 전자상가": "an electronics district filled with colorful neon lights",
    "비어 있는 학교 교실": "an empty school classroom with sunlight through blinds",
    "병원 수술실": "a sterile hospital surgery room with cold lighting",
    "도서관 옥상": "a quiet library rooftop with a view of the city skyline",
    "무대 뒤 백스테이지": "a cluttered backstage with curtains, props, and hushed voices",
    "낮은 천장의 지하 벙커": "a low-ceiling underground bunker with flickering lights and concrete walls",
    "지붕 없는 버려진 성당": "a roofless abandoned cathedral with ivy-covered walls and scattered pews",
    "우주 정거장 내부": "inside a futuristic space station with metallic corridors and floating lights",
    "침몰 직전의 유람선 내부": "inside a sinking cruise ship with tilted floors and leaking walls",
    "거대한 식물 뿌리에 둘러싸인 동굴": "a hidden cave wrapped in giant roots with glowing moss",
    "인형으로 가득 찬 빈 방": "an empty room filled with antique dolls and silence",
    "불타고 있는 숲속 오두막": "a forest cabin engulfed in flames, casting dancing shadows",
    "겨울철 눈덮인 기차길": "a snow-covered railway track disappearing into a white horizon",
    "창고형 클럽의 댄스플로어": "a warehouse-style club with flashing lights and pounding bass",
    "버려진 군사 기지": "a deserted military base with sandbags and broken fences",
    "로마 유적지 안": "inside Roman ruins with crumbling pillars and marble dust",
    "고대 신전 내부": "inside an ancient temple with flickering torches and sacred carvings",
    "사막의 풍력 발전기 지역": "a desert field filled with towering wind turbines and dust trails",
    "거대한 시계탑 내부": "inside a towering clocktower with moving gears and echoing ticks",
    "심해 해저 연구소": "an underwater lab deep in the ocean with glowing panels and silence",
    "폭설 내리는 거리": "a snow-covered street during heavy snowfall, with muffled sounds and glowing windows",
    "달빛 비추는 폐교 운동장": "an abandoned schoolyard under moonlight with rusting swings and silence",
    "지하철역 끝 승강장": "the far end of a dimly lit subway platform with flickering lights",
    "불타고 있는 도서관 내부": "the interior of a burning library with collapsing shelves and smoke",
    "하이테크 기업 로비": "a sleek corporate lobby with holograms and reflective marble floors",
    "과거형 시골 기차역": "a rural train station from the past, with wooden benches and analog clocks",
    "무성한 수풀 속 오두막": "a hidden cabin deep in overgrown woods, with moss on the walls",
    "천장이 유리로 된 열대 식물원": "a tropical greenhouse with cascading vines and humid air",
    "우주선 조종실": "inside a spacecraft cockpit with glowing controls and cosmic views",
    "폐쇄된 지하 주차장": "an abandoned underground parking lot with oil stains and silence",
    "낙엽 가득한 공원 산책로": "a park trail covered in autumn leaves with gentle breeze",
    "고요한 호숫가": "a tranquil lakeside with still water and faint ripples",
    "해무가 자욱한 부두": "a fog-covered dockyard with creaking ropes and distant horns",
    "폭풍우 치는 옥상": "a rooftop during a storm with flashing lightning and whipping wind",
    "고대 신전 폐허": "ruins of an ancient temple overtaken by nature",
    "지붕이 뚫린 지하철 터널": "a broken subway tunnel with shafts of sunlight leaking through",
    "폐가 거실": "a decaying living room of a forgotten house with torn wallpaper",
    "공항 활주로 끝": "the far end of an airport runway at sunrise with heat haze",
    "빙판길 위": "on a frozen road with slippery reflections and chilly air",
    "한밤의 숲속 캠프파이어 주변": "around a campfire deep in a midnight forest, surrounded by darkness"
}



time = {
    "새벽": "pre-dawn twilight with a faint bluish glow",
    "아침": "early morning light casting long soft shadows",
    "정오": "high noon with bright, overhead sunlight",
    "오후": "gentle afternoon warmth with a golden hue",
    "황혼": "twilight with orange and purple tones on the horizon",
    "저녁": "early evening light dimming into blue tones",
    "밤": "deep night with scattered artificial lighting",
    "심야": "midnight darkness with sparse illumination and silence",

}


character_count_dict = {
    "1명": "a single character, fully isolated in the frame",
    "2명": "two people interacting or positioned with visible distance",
    "3~5명": "a small group with dynamic composition",
    "군중": "a large crowd filling the scene with motion and noise",
    "보이지 않음": "no visible characters, focus on environment and atmosphere"
}



character_action = {
    "걷는다": "the character is walking slowly, footsteps echoing in the space",
    "달린다": "the character is running with urgency, breath visible in the air",
    "춤춘다": "the character dances freely, body moving in fluid rhythm",
    "하늘을 본다": "the character looks up at the sky in contemplation",
    "앉아 있다": "the character sits calmly, hands resting on their knees",
    "서성인다": "the character paces around, lost in thought",
    "바닥을 바라본다": "the character stares at the ground, expression unreadable",
    "팔을 벌린다": "the character spreads their arms wide as if embracing something unseen",
    "포옹한다": "two characters embrace in a quiet moment of connection",
    "멍하니 선다": "the character stands motionless, absorbed in silence",
    "창밖을 응시한다": "the character gazes out the window, detached from the world",
    "거울을 바라본다": "the character looks into a mirror, examining themselves",
    "노래한다": "the character sings softly, voice blending into the air",
    "울고 있다": "the character is crying silently, tears catching the light",
    "웃는다": "the character smiles subtly, barely noticeable but sincere",
    "소리친다": "the character yells into the void, voice raw with emotion",
    "춤추듯 걷는다": "the character moves forward in a dance-like rhythm, surreal and elegant",
    "무언가를 쥐고 있다": "the character is holding something tightly, knuckles pale",
    "벽에 기대어 선다": "the character leans against a wall, shoulders tense",
    "천천히 돌고 있다": "the character spins slowly in place, lost in thought",
    "손으로 얼굴을 가린다": "the character covers their face with trembling hands",
    "손끝을 바라본다": "the character inspects their fingertips with quiet curiosity",
    "바닥에 주저앉는다": "the character sinks to the floor, overwhelmed",
    "빛을 향해 걷는다": "the character walks toward the light in the distance",
    "허공을 바라본다": "the character stares into empty space, unblinking",
    "자신을 껴안는다": "the character hugs themselves tightly, seeking comfort",
    "옷깃을 만지작거린다": "the character fiddles with their collar, anxious",
    "창문을 두드린다": "the character taps gently on a windowpane",
    "발끝으로 선다": "the character rises on tiptoes, reaching upward",
    "주변을 경계한다": "the character scans their surroundings cautiously",
    "무대 위에 선다": "the character stands under a spotlight, exposed and still",
    "문틈을 들여다본다": "the character peeks through a slightly open door",
    "하늘을 향해 손을 뻗는다": "the character reaches up toward the sky",
    "걸음을 멈춘다": "the character stops abruptly, as if frozen in realization",
    "가슴을 움켜쥔다": "the character presses their hand to their chest, as if containing an overwhelming feeling",
    "무너진다": "the character collapses to their knees, overwhelmed by emotion",
    "손을 떨고 있다": "the character’s hands tremble as they struggle to stay composed",
    "심호흡한다": "the character takes a deep breath, trying to steady themselves",
    "눈을 감는다": "the character closes their eyes, retreating inward",
    "가슴을 누른다": "the character presses a hand to their chest, as if to contain something within",
    "허공을 응시한다": "the character stares into empty space, thoughts adrift",
    "고개를 숙인다": "the character bows their head slightly, in reflection or guilt",
    "팔짱을 낀다": "the character crosses their arms, guarded and tense",
    "손을 뻗는다": "the character reaches out into the void, grasping for something intangible",
    "등을 돌린다": "the character turns their back slowly, disengaging from the scene",
    "벽에 기대선다": "the character leans against the wall, drained and silent",
    "자신의 얼굴을 만진다": "the character gently touches their face, unsure of who they are",
    "물건을 꼭 쥔다": "the character tightly grips a small object, holding onto memory",
    "유리를 두드린다": "the character taps lightly on a glass surface, seeking attention or escape",
    "가만히 숨을 멈춘다": "the character holds their breath, as if time has stopped",
    "고개를 천천히 돌린다": "the character slowly turns their head, reacting to something off-screen",
    "몸을 떨고 있다": "the character’s body trembles involuntarily, overwhelmed",
    "팔을 움켜쥔다": "the character clenches their arms tightly, trying to hold themselves together",
    "주변을 두리번거린다": "the character looks around cautiously, scanning their surroundings",
    "가슴을 두드린다": "the character pounds their chest with a fist, as if awakening pain or courage",
    "앞으로 무너진다": "the character collapses forward onto their knees, defeated",
    "뒷걸음질 친다": "the character takes hesitant steps backward, afraid or unsure",
    "손끝으로 무언가를 만진다": "the character gently traces an object with their fingertips, lost in memory",
    "무언가를 품에 안는다": "the character holds something to their chest, as if it’s precious or sacred",
    "어깨를 떨군다": "the character lets their shoulders fall, giving in to emotional fatigue",
    "주먹을 쥔다": "the character clenches their fist, silently holding back emotion",
    "뒤돌아선다": "the character turns away, leaving something behind",
    "양손을 치켜든다": "the character raises both hands, in surrender or plea",
    "벽에 등을 기대고 미끄러진다": "the character slides down a wall, ending up seated on the ground in silence",
    "바닥에 앉은 자세": "sitting cross-legged on the floor",
    "소파에 다리 꼬고 앉은 자세": "sitting with one thigh crossed over the other on a sofa",
    "소파에 양반다리 앉은 자세": "sitting cross-legged on a sofa",
    "엎드려 누운 자세": "lying face down, supported on her elbows",
    "한쪽 다리만 구부린 자세": "lying down with one knee raised while the other leg remains extended",
    "의자에 바른 자세로 앉은 자세": "sitting upright on a chair with both feet on the floor",
    "바닥에 다리를 앞으로 뻗은 자세": "sitting on the floor with her legs stretched straight forward",
    "서있는 자세": "standing upright with a relaxed posture",
    "쪼그려 앉은 자세": "squatting low with knees bent and feet flat on the ground",
    "소파에 비스듬히 기대어 앉은 자세": "reclining sideways on a sofa, supported by one arm",
    "무릎을 세우고 바닥에 앉은 자세": "sitting on the floor with knees drawn up to the chest",
    "소파에 눕다시피 앉은 자세": "half-lying on the sofa with her legs extended along the cushions",
    "의자 등받이에 깊게 기대 앉은 자세": "slouching back deeply into a chair with a relaxed posture",
    "다리를 한쪽으로 모으고 앉은 자세": "sitting with both legs folded to one side",
    "의자에 턱을 괴고 앉은 자세": "sitting on a chair with her chin resting on her hand",
    "벽에 기대어 앉은 자세": "sitting with her back leaning against the wall",
    "침대 위에 웅크리고 앉은 자세": "sitting curled up on the bed",
    "의자에 다리를 올리고 앉은 자세": "sitting on a chair with one or both legs raised",
    "침대에 옆으로 누운 자세": "lying on her side on the bed",
    "소파에 뒤집혀 누운 자세": "lying upside down on the sofa",
    "바닥에 고개를 숙이고 웅크린 자세": "sitting curled up on the floor with head down",
    "발가락을 꼼지락 거린다": "wiggling her toes slightly",
    "다리를 교차하면서 꼰다": "crossing and twisting her legs together",
    "다리를 천천히 들어올린다": "slowly lifting her leg",


}


emotion = {
    "슬픔": "the character's eyes glisten with sadness, movements slow and heavy",
    "기쁨": "the character radiates joy, with bright eyes and an open expression",
    "무표정": "the character shows no emotion, face calm and unreadable",
    "긴장": "the character appears tense, muscles slightly rigid and breath held",
    "평온": "the character is serene and composed, exuding calmness",
    "분노": "the character trembles slightly, fists clenched, with an intense glare",
    "그리움": "the character looks distant, as if recalling a memory with soft sorrow",
    "환희": "the character appears overjoyed, movements buoyant and energetic",
    "불안": "the character’s gaze flickers, hands fidgeting slightly in nervousness",
    "냉소": "the character smirks faintly, eyes filled with ironic detachment",
    "감격": "the character holds back tears of gratitude, lip trembling",
    "허무": "the character stares blankly, drained of emotion or purpose",
    "애절": "the character seems on the verge of tears, struggling to hold composure",
    "몰입": "the character is entirely focused, unaware of their surroundings",
    "경이": "the character's eyes widen in wonder, mouth slightly agape",
    "수치심": "the character looks down, avoiding eye contact with visible shame",
    "경멸": "the character's lips curl with contempt, eyes narrowed in disdain",
    "자책": "the character clenches their jaw, clearly blaming themselves",
    "기대감": "the character leans forward slightly, eyes sparkling with hope",
    "죄책감": "the character winces inwardly, unable to face what they've done",
    "자신감": "the character stands tall, chin slightly raised with quiet confidence",
    "흥미로움": "the character tilts their head with curiosity, lips pursed in thought",
    "낙담": "the character slumps slightly, shoulders heavy with disappointment",
    "긴장 속의 차분함": "the character remains composed, but a slight tremble betrays inner tension",
    "감정 억제": "the character fights to suppress emotions, lips pressed tight",
    "불굴": "the character stands firm, eyes set with unwavering determination",
    "두려움": "the character backs away slightly, breath shallow and eyes darting",
    "외로움": "the character seems isolated, as if forgotten by the world",
    "안도": "the character exhales slowly, shoulders lowering with relief",
    "냉담": "the character appears emotionally distant, gaze cold and indifferent",
    "혼란": "the character glances around with uncertainty, lips parted as if lost",
    "상실감": "the character holds something close, as if clinging to a fading presence",
}


camera_view = {
    "정면 시점": "a front-facing shot with the subject looking directly at the camera",
    "측면 시점": "a profile view showing the subject from the side",
    "등 뒤 시점": "a back-facing shot with the subject seen from behind",
    "로우 앵글": "a low-angle shot looking up at the subject, emphasizing power or awe",
    "하이 앵글": "a high-angle shot looking down, creating a sense of vulnerability",
    "오버더숄더": "an over-the-shoulder shot showing what the character sees",
    "탑다운": "a top-down shot directly above the scene, almost diagrammatic",
    "클로즈업": "a close-up framing only the face or a specific detail",
    "롱샷": "a wide long shot showing the subject within a vast environment",
    "핸드헬드": "a handheld camera feel, slightly shaky and personal",
    "POV": "a point-of-view shot from the character's eyes",
    "드론 샷": "an aerial drone shot soaring above the scene",
    "정면": "a front-facing perspective, directly capturing the subject’s face",
    "측면 (오른쪽)": "a right-side profile view, capturing the subject's side profile",
    "측면 (왼쪽)": "a left-side profile view, capturing the subject's side profile",
    "뒤에서 (어깨 위)": "an over-the-shoulder perspective from behind",
    "뒤에서 (머리 위)": "a top-down angle from behind, focusing on the subject's head",
    "아래에서 올려다봄": "a low-angle shot looking upward, highlighting the subject’s stature",
    "위에서 내려다봄": "a high-angle shot looking down, providing a sense of dominance over the subject",
    "정수리 시점": "a shot starting from the top of the head, focusing on the head and upper body",
    "발끝 시점": "a shot starting from the toes, focusing on the lower body with the upper body slightly included",
    "허리 아래 시점": "a shot starting from the lower back or buttocks, focusing on the back and upper body",
    "앞에서 아래를 향함": "a downward angle from the front, looking down slightly on the subject",
    "뒤에서 아래를 향함": "a downward shot from behind, showing the back and surroundings",
    "정면 클로즈업": "an extreme close-up of the face from the front, capturing minute facial details",
    "발밑에서 대각선 위로": "a diagonal low-angle shot starting from the floor, tilting upward, emphasizing stature",
    "정면 클로즈업 (눈 중심)": "an extreme close-up of the eyes, emphasizing subtle emotions or tension",
    "하늘에서 내려다보는 시점": "a bird's eye view, capturing the scene from directly above, offering a complete overview",
    "비스듬히 위에서 바라보는 시점": "a diagonal top-down shot, showing a dynamic perspective from an elevated angle",
    "물속에서 바라보는 시점": "an underwater perspective, with the subject partially or fully submerged in water",
    "거울 반사 시점": "a reflection of the subject viewed through a mirror, creating a layered visual experience",
    "통로 시점": "a shot looking through a narrow space or doorway, framing the subject partially within the space",
    "뒤에서 (슬쩍 돌아보는 시점)": "a behind-the-back shot, where the subject turns slightly towards the camera, revealing their back and side",
    "미세한 움직임 강조 시점": "a subtle, intimate close-up focusing on minute movements like a hand, finger, or slight gesture",
    "일그러진 렌즈 시점": "a distorted lens perspective, warping the image and creating a surreal or dreamlike atmosphere",
    "가까운 초점 시점": "a close-focus shot on a specific detail, object, or feature, while the rest of the frame is blurred",
    "포커스 아웃 시점": "a slow zoom-out, starting from a specific subject and gradually pulling back to reveal the context",
    "스카이라인 시점": "a perspective that emphasizes a city’s skyline, often at dusk or dawn, with lights fading or appearing",
    "입체감 강조 시점": "a perspective that enhances the sense of depth, using foreground elements to create layers",
    "회전 시점": "a spinning or rotating camera, often used to disorient or intensify a moment, revealing surroundings",
    "슬로우 포커스 전환 시점": "a slow shift in focus, gradually blurring and then revealing a new point of interest in the frame",
    "손끝 시점": "a shot starting from the tips of the fingers, following the hand's movement with a focus on the action",
    "배경과 인물 분리 시점": "a shot that separates the background and foreground sharply, creating a contrast in focus",
    "돌아서가는 시점": "a perspective where the character turns and walks away, leaving the camera behind",
    "빛과 그림자의 교차": "a shot where light and shadow intersect dramatically across the subject, creating tension",
    "디테일 클로즈업": "an extreme close-up on an object or part of the subject, like a hand or a facial feature",
    "굴곡진 거리 시점": "a shot from a winding road or path, with the camera following the curvature",
    "시선 따라가기 시점": "a point of view where the camera follows the subject’s gaze, drawing focus to the object or scene they are looking at",
    "구멍을 통해 바라보는 시점": "a view through a small hole or crack, like a keyhole, giving a restricted perspective",
    "불빛 속 실루엣": "a shot where the character’s silhouette is emphasized by a harsh light source behind them",
    "흔들리는 카메라": "a handheld, shaking camera effect often used to convey a sense of chaos or panic",
    "구름 속에서 내려다보는 시점": "a high-altitude shot from within the clouds, looking down on the world below",
    "불꽃 속에서 바라보는 시점": "a shot from within a fire, emphasizing flickering flames around the subject",
    "미로 속 시점": "a disorienting camera angle moving through a labyrinth or maze, with shifting corridors",
    "강한 초점 변화": "a shot where the focus rapidly changes between two elements in the frame, creating a dynamic shift",
    "역동적인 카메라 줌": "an intense zoom-in or zoom-out effect, creating a sense of surprise or focus",
    "카메라로 인물 추적": "a shot that tracks the character as they move through a scene, maintaining focus on them at all times",
    "지평선 위 시점": "a low angle shot looking toward the horizon, often used to show vastness or infinity",
    "다리 사이로 보는 시점": "a shot framed through the legs of the subject, looking up at the world around them",
    "비정상적인 비율 시점": "a fisheye or wide-angle perspective that distorts the proportions of the environment",
    "의자 뒤에서 바라보는 시점": "a view from behind a chair, with the subject’s figure slightly obscured by the backrest",
    "흐린 카메라": "a deliberately blurred or out-of-focus shot, used to create a dreamy or hazy effect",
    "천천히 다가오는 시점": "a slow approach from a distance, with the subject becoming clearer as the camera moves forward",
    "카메라 회전 속도 변화": "a shot where the camera rotates at varying speeds, creating visual tension or surprise",
    "눈 속에서의 시점": "a perspective where the camera is framed by snowflakes or fog, adding a cold or surreal atmosphere"

}

camera_movement = {
    "위로 올리기": "camera moves upwards, revealing the subject or a broader scene",
    "아래로 내리기": "camera moves downwards, emphasizing the subject or surroundings below",
    "왼쪽으로 돌리기": "camera pans to the left, shifting focus to the left side of the frame",
    "오른쪽으로 돌리기": "camera pans to the right, shifting focus to the right side of the frame",
    "가까이 다가가기": "camera zooms in, getting closer to the subject or specific detail",
    "멀리 물러나기": "camera zooms out, revealing more of the surrounding environment",
    "빙글 돌리기": "camera rolls, creating a disorienting effect, often used for dramatic scenes",
    "따라가기": "camera follows a moving subject, maintaining focus on them while they move",
    "급하게 아래로 뛰어내리기": "camera dives downward, often used for dramatic or rapid descent effects",
    "옆으로 움직이기": "camera moves horizontally along a fixed plane, creating a side-to-side effect",
    "위에서 따라가기": "camera moves directly overhead, following the subject or scene from above",
    "천천히 위로 올리기": "camera moves upwards on a crane, elevating the perspective",
    "천천히 아래로 내리기": "camera moves downward on a crane, often used to descend into a scene",
    "부드럽게 따라가기": "camera follows the subject while remaining steady, minimizing motion shake",
    "공중에서 보여주기": "camera is mounted on a helicopter, providing sweeping aerial views",
    "좁은 공간 옆으로 이동": "camera moves horizontally through a confined space, often used to follow a subject in tight spaces",
    "바닥 가까이 옆으로 이동": "camera moves horizontally at floor level, creating a sense of movement close to the ground",
    "빙글빙글 회전": "camera spins around a central point, capturing the scene from every angle",
    "가로로 움직이며 배경 바꾸기": "camera moves along a horizontal axis, keeping the subject in focus while shifting the background",
    "지그재그로 흔들기": "camera moves in a zigzag pattern, creating a dynamic and unpredictable movement",
    "틀어지게 돌리기": "camera twists or turns during a shot, creating a disorienting and dramatic effect"
}



lighting = {
    "아침 햇살": "soft, cool bluish morning light that brings a calm and fresh atmosphere",
    "점심빛": "bright and golden midday light that creates sharp shadows and highlights",
    "저녁 노을": "warm and soft sunset light, casting long, golden rays across the scene",
    "새벽 빛": "dim, muted bluish-gray dawn light, creating a quiet, still atmosphere",
    "황혼의 빛": "burnt orange twilight light that enhances the mysterious and dreamlike quality of a scene",
    "달빛": "soft, cold moonlight that brings a tranquil, ethereal atmosphere",
    "촛불 빛": "flickering warm candlelight, adding intimacy and a sense of calm to the scene",
    "형광등 조명": "cool white artificial light from fluorescent tubes, providing a clinical and harsh feel",
    "비 오는 날 흐림": "diffused gray daylight from a rainy window, giving the scene a melancholic and moody atmosphere",
    "아케이드 불빛": "bright, colorful neon lights of an arcade, enhancing the energetic and vibrant mood",
    "스포트라이트": "focused dramatic spotlight that isolates the subject from the background",
    "빛 한 줄기": "a single shaft of sunlight cutting through a dark space, emphasizing a moment of focus or enlightenment",
    "빛의 반사": "light bouncing off reflective surfaces, creating a bright, lively ambiance",
    "불빛": "a soft, warm glow from a fire or light source, evoking coziness and warmth",
    "실내 조명": "soft, ambient indoor lighting that creates a calm, neutral tone",
    "어두운 그림자": "harsh shadows cast by intense, direct lighting, creating a high-contrast effect",
    "몽환적인 빛": "dreamy, soft light that blurs edges and adds a surreal touch to the scene",
    "얼음처럼 차가운 빛": "cold, harsh lighting that mimics the stark, clinical feel of ice or snow",
    "대비 강한 빛": "high-contrast lighting that creates deep shadows and stark highlights, evoking tension or mystery",
    "고요한 빛": "quiet, diffused light that gently fills the space, evoking tranquility and calm",
    "형광등 밑": "under fluorescent lights, giving the scene a sterile, uninviting atmosphere",
    "암흑 속 점등": "a faint light in a dark room, symbolizing hope, discovery, or quiet solitude",
}


face_shape = {
    "타원형": "oval",
    "둥근형": "round",
    "하트형": "heart-shaped",
    "사각형": "square",
    "긴형": "long",
    "다이아몬드형": "diamond-shaped",
    "정삼각형": "triangle-shaped",
    "역삼각형": "inverted triangle",
    "부드러운 턱선": "soft jawline",
    "날카로운 턱선": "sharp jawline",
    "조각같은 이목구비": "chiseled features",
    "높은 광대뼈": "high cheekbones",
    "동안형": "baby-faced fullness",
    "섬세한 브이라인": "delicate V-line",
    "입체적인 유선형": "sculpted U-line"
}


manicure_text = {
    "없음": "no polish",
    "파스텔": "pastel-colored polish on nails",
    "누드": "nude-colored polish on nails",
    "펄": "soft glitter polish on nails",
    "스팽글": "sparkling glitter polish on nails",
    "크림": "creamy finish polish on nails",
    "메탈릭": "metallic finish polish on nails",
    "그라데이션": "gradient polish on nails",
    "투명 광택": "clear glossy polish on nails",
    "프렌치팁": "classic French tip manicure",
    "네일 아트": "artistic nail designs with small patterns",
    "무광": "matte polish on nails",
    "네온": "vivid neon-colored polish on nails",
    "큐빅 포인트": "nails with tiny rhinestone or bead accents",
    "블랙": "solid black polish on nails",
    "하트 패턴": "nail polish with heart pattern",
    "유리광택": "iridescent glassy polish on nails",
}


foot_text = {
    "없음": "no footwear",
    "랜덤": "may or may not have footwear",
    "파스텔": "pastel-colored polish on toenails",
    "누드": "nude-colored polish on toenails",
    "펄": "soft glitter polish on toenails",
    "양말": "plain white socks",
    "스타킹": "black sheer stockings",
    "덧양말": "thick woolen socks",
    "체크무늬 양말": "checkered pattern socks",
    "무릎 양말": "knee-high socks",
    "하이힐 스타킹": "fishnet stockings with high heels",
    "운동화 양말": "ankle socks with sneakers",
    "슬리퍼": "flip-flops or slippers",
    "구두": "formal shoes with socks",
    "웨딩 스타킹": "bridal lace stockings",
    "레깅스": "leggings, comfortable and flexible",
    "고급 스타킹": "luxurious velvet stockings with a soft sheen",
    "캔디 스트라이프 양말": "candy stripe socks in bright colors",
    "펑크 양말": "punk style socks with studs or spikes",
    "스트랩 샌들": "strappy sandals with open toes",
    "부츠": "knee-high boots with thick soles",
    "운동화": "sports sneakers with breathable fabric",
    "나이트 스타킹": "nighttime stockings with glowing effects",
    "웨지힐": "wedge heels with ankle straps",
    "갈색 롱부츠": "brown long boots with a smooth leather finish",
    "메리 제인 슈즈": "Mary Jane shoes with socks",
    "오픈토 샌들": "open-toe sandals with a buckle design",
    "플랫폼 슈즈": "platform shoes with a thick sole",
    "털 부츠": "fuzzy boots lined with fur",
    "하이탑 스니커즈": "high-top sneakers with laces",
    "슬립온": "slip-on shoes with elastic sides",
    # 감성 & 상황 특화
    "투명 젤 네일": "clear glossy polish on toenails",
    "그라데이션 네일": "gradient polish on toenails",
    "프렌치 네일": "French tip polish on toenails",
    "하트 패턴 네일": "heart-patterned polish on toenails",
    "큐빅 네일": "toenails with rhinestone accents",

    # 계절 & 실내
    "털 실내화": "fuzzy indoor slippers with closed toes",
    "실내 슬리퍼": "indoor slippers with soft fabric",
    "기모 스타킹": "fleece-lined winter tights",
    "양털 부츠": "sherpa-lined snow boots",
    "비 오는 날 장화": "rain boots with glossy finish",
    "해변용 샌들": "beach sandals with sandy texture",

    # 문화 & 전통
    "고무신": "traditional Korean rubber shoes",
    "게타": "traditional Japanese wooden sandals (geta)",
    "짚신": "woven straw sandals",
    "토오크 샌들": "traditional Indian toe ring sandals",

    # 감성 연출용
    "곰돌이 슬리퍼": "bear-shaped fuzzy slippers",
    "하트 양말": "heart-patterned cute socks",
    "망사 스타킹": "mesh patterned stockings",
    "에나멜 힐": "glossy enamel high heels",
    "벗어둔 양말": "socks loosely thrown beside her on the floor",

    # 활동성 연출
    "요가 양말": "yoga grip socks with open toes",
    "러닝화": "running shoes with arch support",
    "하이킹 부츠": "hiking boots with rugged soles"

}


outfit = {
    "기본 옷": "a pastel summer tank top and short, lightweight summer shorts",
    "홈 원피스": "thin-strapped casual home dress",
    "회사원": "a fitted blouse and office skirt",
    "캐주얼": "an oversized t-shirt and shorts",
    "파자마": "a soft pajama set",
    "한복": "a traditional Korean hanbok with vibrant colors and flowing sleeves",
    "기모노": "a traditional Japanese kimono with elegant patterns and wide sash",
    "닌자 복장": "a traditional ninja outfit with sleek, dark matte fabric that absorbs light for ultimate stealth. The suit features intricate, flexible armor plating across the arms and legs, designed for fluid movement. It includes fingerless gloves for dexterity, lightweight arm guards for protection, and a minimalist forehead band with subtle engravings. The fabric is layered for comfort and mobility, perfect for silent movements. The suit’s practical design is enhanced by reflective accents that glow faintly in low-light conditions, making it ideal for night operations. The overall look merges ancient shinobi aesthetics with modern tactical features, giving it a timeless yet highly functional appeal.",
    "붉은 전투 파일럿 슈트": "a striking crimson pilot suit reminiscent of classic mecha anime, designed for high-speed maneuvers and intense control in combat situations. The suit features bold symmetrical lines and a high-gloss finish that accentuates the wearer's silhouette...",
    "화이트 바이오 슈트": "a minimalistic white and blue bio-suit often seen in futuristic space-themed animation, specifically designed for deep-space exploration and high-tech missions. The suit features soft, organic contours...",
    "군복계 파일럿": "a sleek, high-tech pilot uniform designed for both combat and tactical use. The suit’s glowing seams provide both visual appeal and a practical energy source, while the control panel belt allows for seamless interaction with the cockpit's systems. The fabric is a mix of smooth, flexible material and tough, armor-like panels, designed to protect while offering maximum agility. The high-tech look is enhanced by a matte black finish, which absorbs light and blends into shadows, making it ideal for stealthy operations.",
    "SF 간호복": "a biotech nurse suit designed to assist in high-pressure medical environments. The suit’s form-fitting silhouette is crafted from a flexible material that adapts to the body, while the glowing armband adjusts to the wearer’s vital signs. The material feels almost organic, with a smooth, breathable texture that keeps the wearer cool during long shifts. The subtle, futuristic design features soft, luminescent accents that indicate the suit’s advanced functionality, perfect for tending to patients in even the most sterile or hazardous conditions.",
    "스텔스 요원": "an urban infiltration suit designed for covert missions in high-tech environments. The hooded visor seamlessly integrates with the suit, providing a fully immersive tactical interface. The suit’s material is a lightweight, breathable mesh that contours to the body, offering full range of motion while maintaining a shadow-like appearance. The fabric is reinforced with specialized fibers that mask the wearer’s presence, allowing them to blend into any urban setting while remaining undetected. The minimalistic design is both functional and highly adaptable.",
    "메카걸": "an armored bodysuit with exposed mechanical joints and high-tech leg braces, designed for enhanced combat performance. The suit’s body is made of a durable, flexible material that allows for fluid movement, while the exposed joints showcase the intricate mechanics that power the wearer’s enhanced strength and agility. The metallic texture of the armor reflects light, giving the suit a polished, futuristic appearance. The mechanical braces allow for explosive movements, while the sleek design ensures that the wearer can maintain both defense and agility in battle.",
    "전투 메이드": "a combat-ready maid uniform that merges traditional elegance with tactical efficiency. The reinforced bodice is crafted from high-durability fabric, offering protection while maintaining a sleek silhouette. The concealed holster and utility belt provide easy access to weapons and tools, while the skirt’s flexible material allows for swift movements. The suit’s understated yet functional design is perfect for both domestic duties and high-intensity combat, with the classic maid aesthetic giving it a unique and intimidating edge in the field.",
    "아케이드 파일럿 슈트": "a tight, form-fitting combat suit inspired by arcade-style mech pilots, sleek and lightweight for maximum mobility. Bright modern accents and a dynamic visor complete the look...",
    "빛의 힐러 슈트": "a futuristic support uniform inspired by celestial-themed healers in popular games. White and gold armor with angelic wings and a utility belt filled with advanced healing gear...",
    "봉미선 스타일 의상": "A simple, casual outfit worn by Bong Mison (Shin-chan's mother). The outfit features a brightly colored t-shirt or blouse, often in pastel shades or floral prints, paired with comfortable pants or skirts. She often wears a simple cardigan or sweater over her clothes for a cozy, approachable look. Her look is practical yet warm, ideal for a busy mom, with comfortable shoes like flats or low heels. The outfit reflects her warm and nurturing personality, with a hint of femininity, perfect for her role as a loving mother and wife.",
    "베이직 티셔츠와 청바지": "a classic fitted t-shirt tucked into high-waisted jeans with sneakers",
    "후드티와 조거팬츠": "an oversized hoodie paired with soft jogger pants and casual slip-ons",
    "니트와 롱스커트": "a cozy knit sweater with a flowy ankle-length skirt and ankle boots",
    "반팔 티와 반바지": "a plain crew-neck tee with denim shorts and canvas shoes",
    "크롭티와 와이드팬츠": "a short crop top with wide-leg trousers and platform sandals",
    "체크셔츠와 레깅스": "a loose plaid shirt layered over a tank top with black leggings",
    "심플 셔츠와 슬랙스": "a crisp white shirt tucked into slim-fit slacks with loafers",
    "민소매 블라우스와 미디스커트": "a sleeveless blouse with a pleated midi skirt and ballet flats",
    "라운드넥 니트와 스키니진": "a round-neck sweater with skinny jeans and flat ankle boots",
    "심플 롱 원피스": "a monotone long dress with clean lines and minimalist sandals",
    "린넨 셔츠와 와이드팬츠": "a loose linen shirt with wide-leg eco-fabric pants and straw sandals",
    "자연톤 원피스": "a beige or olive-toned cotton dress with wooden-button accents",
    "수수한 앞치마 원피스": "a natural-fiber pinafore dress layered over a light top, barefoot or in clogs",
    "프릴 블라우스와 플레어스커트": "a ruffled blouse with a flared skirt and low heels",
    "슬립 드레스": "a satin slip dress with a lightweight cardigan and strappy sandals",
    "하이넥 블라우스와 H라인 스커트": "a high-neck blouse tucked into a form-fitting skirt with pumps",
    "셔츠 원피스": "a belted shirt dress with long sleeves and pointed-toe flats",
    "요가복": "a stretchable yoga set with a sleeveless top and high-waisted leggings, designed for flexibility and breathability",
    "겨울 캐주얼": "a padded parka layered over a knit sweater, with thermal leggings and fur-lined boots",
    "봄 데이트룩": "a floral chiffon dress with puffed sleeves and white ballet flats",
    "댄서 스타일": "a cropped hoodie over a sports bra with jogger pants and chunky sneakers, embodying a confident street dance vibe",
    "빈티지 롱드레스": "a vintage-inspired long dress with lace trim, puff sleeves, and soft neutral tones, evoking classic elegance",
    "카페 알바룩": "a white button-up tucked into a khaki apron skirt, paired with canvas sneakers and a headband",
    "프렌치 시크룩": "a striped boat-neck top with high-waisted trousers, a silk scarf tied at the neck, and loafers",
    "비 오는 날 외출복": "a waterproof trench coat with a hood, layered over cropped jeans and rain boots",
    "모던 미니멀룩": "a solid-tone blouse tucked into wide slacks with sharp lines and leather loafers, accessorized with a clean tote bag",
    "아이돌 무대의상": "a shimmering crop top with a pleated mini skirt, thigh-high socks, and platform heels, stage-ready and attention-grabbing",
    "핑크 매지컬걸 의상": "a classic magical girl costume evoking the 90s cherry blossom aesthetic, with a short bell-shaped dress, oversized ribbon accents, and a star-topped magical staff...",
    "달빛 전사 매지컬 복장": "a sailor-style magical battle uniform inspired by lunar protectors, featuring a white leotard with a navy mini skirt, red bows, crescent motifs, and twin tails tied in buns...",
    "아테나 스타일 의상": "a vibrant idol-style combat costume with pink accents, pleated skirt, and sparkly fabric, reflecting a youthful fighter who blends music and psychic energy...",
    "플레어 격투복": "a modified martial arts outfit with purple capris, red sash, and sporty gloves, worn by a cheerful yet fierce female fighter from a retro-style fighting game...",
    "불꽃 마법 전사 의상": "a fantasy-themed red sorceress outfit inspired by adventurous magic-wielders from 90s anime, featuring shoulder armor, black cape, and enchanted accessories..."

}


body_shape = {
    "슬림형": "slim body type with a slender silhouette and minimal curves",
    "균형형": "balanced body with even proportions between shoulders, waist, and hips",
    "글래머러스": "curvy body type with pronounced bust and hips, and a narrow waist",
    "운동형": "athletic body type with defined muscle tone and firm structure",
    "작고 아담한": "petite body type with shorter stature and compact proportions",
    "풍성한": "soft body type with gentle curves and a fuller silhouette",
    "길고 날씬한": "long-limbed body type with tall and graceful proportions",
    "자연형": "natural body type with relaxed, unstructured proportions",
    "둥근 실루엣": "rounded silhouette with soft transitions and subtle curves"
}



hairstyle = {
    "풀어짐 (내추럴)": "hair unbound in natural tones and textures",
    "단정하게 묶음": "hair neatly tied back in a simple ponytail",
    "헝클어진 듯 자연스러움": "hair loosely tousled with a casual elegance",
    "반묶음": "hair half-tied in a soft feminine style",
    "단발 (귀밑길이)": "short bob cut just below the ears",
    "긴 생머리": "long straight hair flowing naturally",
    "웨이브 펌": "soft wavy perm with a light bounce",
    "깔끔한 포니테일": "clean ponytail tied high at the back",
    "올림머리 (업두)": "an elegant updo",
    "가르마 내린 생머리": "long straight hair parted neatly down the center",
    "앞머리 있는 단발": "short bob with full bangs covering the forehead",
    "시스루 뱅": "straight hair with see-through bangs",
    "하프 번": "half-up hair tied into a small top bun",
    "양 갈래 묶음": "twin low ponytails tied loosely behind",
    "헐렁한 땋은 머리": "loosely braided hair draping over one shoulder",
    "귀 뒤로 넘긴 긴 머리": "long straight hair tucked behind both ears",
    "사이드 포니테일": "low side ponytail resting over one shoulder",
    "곱게 말린 C컬 단발": "soft C-curl bob with inward-curled ends",
    "단정한 땋은 머리": "tight single braid tied at the back"
}


fabric_response = {
    "몸 움직임에 따라 섬유가 반응함": "each fiber reacts to posture and motion",
    "옷이 공기 흐름에 부드럽게 흩날림": "clothing flows gently with ambient air",
    "주름과 텍스처가 사실적으로 변형됨": "fabric stretches and wrinkles with realism",
    "천이 몸의 곡선을 자연스럽게 따라감": "fabric drapes naturally along body curves",
    "옷자락이 중력과 움직임에 섬세하게 반응": "hems respond delicately to gravity and motion",
    "천의 질감이 조명에 따라 달라보임": "texture of fabric shifts subtly with lighting",
    "레이스나 얇은 천은 반투명하게 묘사됨": "sheer fabrics are rendered with semi-transparency",
    "보풀이나 실밥 같은 미세한 질감 표현": "micro-textures like pilling and frayed threads are visible",
    "섬유의 방향과 조직감이 정밀하게 드러남": "weave direction and fabric structure are precisely rendered",
    "바람에 흔들릴 때 천의 잔잔한 진동": "gentle oscillations of fabric in light breeze",
}


rendering_translation = {
    "8K 초고화질 리얼": "8K ultra-realistic rendering",
    "4K 실사 고화질": "4K photorealistic rendering",
    "HD 영화풍": "HD cinematic rendering",
    "애니메이션 셀 셰이딩": "anime-style cel shading",
    "디지털 페인팅 스타일": "digital painting style",
    "빈티지 필름 룩": "vintage film look",
    "극사실주의 그림체": "hyperrealistic illustration style",
    "로우파이 감성화질": "lo-fi emotional tone",
    "페인터리 오일화": "painterly oil painting style",
    "수채화 느낌": "watercolor painting texture",
    "블렌더 스타일 3D": "Blender-style 3D rendering",
    "게임 트레일러 느낌": "game cinematic trailer style",
    "패션 잡지 스타일": "editorial fashion photography style",
    "소프트 라이트 몽환풍": "dreamy soft light atmosphere",
    "필름 그레인 아날로그": "analog film grain aesthetic",
}


# ------------------------------ 전역 변수 ------------------------------
input_vars = {}


# ------------------------------ 함수 정의 ------------------------------
def check_logical_warnings(genre, background_val, time_val, character_count, action_val, emotion_val,
                            camera_view_val, camera_movement_val, lighting_val, outfit_val,
                            body_shape_val, hairstyle_val):
    warnings = []

    # 1. 등장 인물 수 제약
    if character_count == "군중" and genre == "고독한 탐험자":
        warnings.append("⚠️ '고독한 탐험자' 장르에는 '군중' 설정이 어울리지 않습니다. 등장 인물 수를 줄이세요.")

    # 2. 실내 배경에서 드론샷/헬리캠
    indoor_background_keywords = ["실내", "도서관", "병원", "박물관", "엘리베이터", "로비", "교실", "백스테이지", "주차장", "지하", "폐가", "거실"]
    if any(kw in background_val for kw in indoor_background_keywords) and camera_view_val in ["드론 샷", "헬리캠"]:
        warnings.append("⚠️ 실내 배경에서는 '드론 샷'이나 '헬리캠'이 비현실적일 수 있습니다.")

    # 3. 감정과 행동 간 모순
    conflict_actions = {
        "울고 있다": ["자신감", "기쁨"],
        "소리친다": ["평온", "무표정"],
        "가만히 숨을 멈춘다": ["흥미로움", "활기찬 감정"]
    }
    for act, invalid_emotions in conflict_actions.items():
        if action_val == act and emotion_val in invalid_emotions:
            warnings.append(f"⚠️ '{act}' 행동은 '{emotion_val}' 감정과 충돌할 수 있습니다.")

    # 4. 카메라 무빙과 시점 간 충돌
    if camera_view_val in ["정면 클로즈업", "디테일 클로즈업"] and camera_movement_val in ["줌아웃", "크레인 업"]:
        warnings.append("⚠️ 극단적인 클로즈업에는 줌아웃/크레인 무빙이 어울리지 않을 수 있습니다.")

    # 5. 헤어스타일 + 시점 충돌
    if hairstyle_val in ["올림머리 (업두)", "하프 번"] and "뒤에서" in camera_view_val:
        warnings.append("⚠️ 뒤에서 보는 시점은 올림머리보다 풀어진 스타일이 더 어울릴 수 있습니다.")

    # 6. 감정 + 조명 충돌
    if emotion_val == "환희" and lighting_val in ["달빛", "형광등 조명", "어두운 그림자", "암흑 속 점등"]:
        warnings.append("⚠️ '환희' 감정은 어두운 조명과 어울리지 않을 수 있습니다.")

    # 7. 체형 + 행동 충돌
    if body_shape_val == "길고 날씬한" and action_val == "바닥에 주저앉는다":
        warnings.append("⚠️ '길고 날씬한' 체형은 '바닥에 주저앉는' 포즈에서 어색해 보일 수 있습니다.")

    # 8. 배경 + 장르 충돌
    if genre == "사이버펑크" and "숲" in background_val:
        warnings.append("⚠️ '사이버펑크' 장르는 자연 배경과 어울리지 않을 수 있습니다.")

    # 9. 행동 + 카메라 무빙 충돌
    if action_val == "가만히 숨을 멈춘다" and camera_movement_val in ["줌인", "크레인 업", "트래킹"]:
        warnings.append("⚠️ 고정적인 행동에는 과한 카메라 무빙이 자연스럽지 않을 수 있습니다.")

    # 10. 감정 + 배경 충돌
    dark_background_keywords = ["묘지", "불타", "지하", "폐가", "벙커"]
    if emotion_val == "기쁨" and any(kw in background_val for kw in dark_background_keywords):
        warnings.append("⚠️ '기쁨' 감정은 어두운 배경과 충돌할 수 있습니다.")

    # 11. 행동 + 장르 충돌
    if action_val == "하늘을 본다" and genre in ["심리 스릴러", "공포"]:
        warnings.append("⚠️ '하늘을 보는' 동작은 현재 장르와 감정이 다소 부조화될 수 있습니다.")

    return warnings




def generate_prompt():
    # ✅ 커스텀 노트 입력 처리
    custom_note = input_vars["custom_note_var"].get().strip()
    custom_note_text = f"This instruction overrides all other rules: {custom_note}.\n" if custom_note else ""

    # ✅ 각 입력값 수집
    genre = input_vars["genre_var"].get()
    background_val = input_vars["background_var"].get()
    time_val = input_vars["time_var"].get()
    character_count = input_vars["character_count_var"].get()
    action_val = input_vars["action_var"].get()
    emotion_val = input_vars["emotion_var"].get()
    camera_view_val = input_vars["camera_view_var"].get()
    camera_movement_val = input_vars["camera_move_var"].get()
    lighting_val = input_vars["lighting_dict_var"].get()
    outfit_val = input_vars["outfit_var"].get()
    body_shape_val = input_vars["body_shape_var"].get()
    hairstyle_val = input_vars["hairstyle_var"].get()
    fabric_response_val = input_vars["fabric_response_var"].get()
    rendering_val = input_vars["rendering_var"].get()
    face_shape_val = input_vars["face_shape_var"].get()
    manicure_val = input_vars["manicure_var"].get()
    foot_val = input_vars["foot_var"].get()

    # ✅ 선택된 국적 텍스트
    nationality_text = ", ".join(nationality_description[n] for n in selected_nationalities) or "a woman of unspecified origin"

    # ✅ 사전에서 영어 스타일 텍스트 추출
    genre_text = genre_tone.get(genre, "")
    background_text = background.get(background_val, "")
    time_text = time.get(time_val, "")
    character_count_text = character_count_dict.get(character_count, "")
    action_text = character_action.get(action_val, "")
    emotion_text = emotion.get(emotion_val, "")
    camera_view_text = camera_view.get(camera_view_val, "")
    camera_movement_text = camera_movement.get(camera_movement_val, "")
    lighting_text = lighting.get(lighting_val, "")
    outfit_text = outfit.get(outfit_val, "")
    body_shape_text = body_shape.get(body_shape_val, "")
    hairstyle_text = hairstyle.get(hairstyle_val, "")
    fabric_response_text = fabric_response.get(fabric_response_val, "")
    rendering_text = rendering_translation.get(rendering_val, "")
    face_shape_text = face_shape.get(face_shape_val, "")
    manicure_text_val = manicure_text.get(manicure_val, "")
    foot_text_val = foot_text.get(foot_val, "")

    # ✅ appearance 상세 문장
    appearance_text = (
        f"A {body_shape_text.lower()} figure "
        "with soft-glow skin randomized between porcelain white and fair beige, "
        "face within conventionally attractive East Asian types, eyes always open, "
        f"{hairstyle_text.lower()}, "
        f"dressed in {outfit_text.lower()}. "
        f"As they {action_text.lower()}, "
        f"their expression conveys {emotion_text.lower()}. "
        f"The fabric of the clothing {fabric_response_text.lower()}. "
        f"Rendered in {rendering_text.lower()}. "
        f"Face shape appears as {face_shape_text.lower()}, "
        f"nails styled with {manicure_text_val.lower()}, "
        f"and toenails feature {foot_text_val.lower()}. "
        "Nails and toenails may or may not be polished (if so, pastel/nude/glitter)."
    )

    full_appearance_text = f"{nationality_text}. {appearance_text}"

    # ✅ 프롬프트 조합
    prompt = f"""{custom_note_text}{genre_text}.
Scene takes place in {background_text} during {time_text}.
There are {character_count_text}.
The camera is {camera_view_text} with {camera_movement_text}.
Lighting is described as: {lighting_text}.

The main character is wearing {outfit_text},
with a {body_shape_text}, and hairstyle: {hairstyle_text}.
The fabric {fabric_response_text}.

Action: {action_text}
Emotion: {emotion_text}

{full_appearance_text}"""

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, prompt.strip())

    # 논리 제약 경고 추가
    warnings = check_logical_warnings(
        genre, background_val, time_val, character_count, action_val,
        emotion_val, camera_view_val, camera_movement_val,
        lighting_val, outfit_val, body_shape_val, hairstyle_val
    )
    if warnings:
        output_text.insert(tk.END, "\n\n⚠️ Logic Warnings:\n" + "\n".join(warnings))


def set_random_values():
    input_vars["genre_var"].set(random.choice(list(genre_tone)))
    input_vars["background_var"].set(random.choice(list(background)))
    input_vars["time_var"].set(random.choice(list(time)))
    input_vars["character_count_var"].set(random.choice(list(character_count_dict)))
    input_vars["action_var"].set(random.choice(list(character_action)))
    input_vars["emotion_var"].set(random.choice(list(emotion)))
    input_vars["camera_view_var"].set(random.choice(list(camera_view)))
    input_vars["camera_move_var"].set(random.choice(list(camera_movement)))
    input_vars["lighting_dict_var"].set(random.choice(list(lighting)))
    input_vars["outfit_var"].set(random.choice(list(outfit)))
    input_vars["body_shape_var"].set(random.choice(list(body_shape)))
    input_vars["hairstyle_var"].set(random.choice(list(hairstyle)))
    input_vars["fabric_response_var"].set(random.choice(list(fabric_response)))
    input_vars["rendering_var"].set(random.choice(list(rendering_translation)))
    input_vars["face_shape_var"].set(random.choice(list(face_shape)))
    input_vars["manicure_var"].set(random.choice(list(manicure_text)))
    input_vars["foot_var"].set(random.choice(list(foot_text)))

    # ✅ 국적 랜덤 적용
    if selected_nationalities:
        base_pool = list(selected_nationalities)
    else:
        base_pool = list(nationality_description.keys())
    if len(base_pool) == len(nationality_description):
        base_pool = list(nationality_description.keys())

    selected_nationalities.clear()
    # 가능한 최대 샘플 수를 base_pool 크기로 제한
    k = min(len(base_pool), random.randint(1, 2))
    for nat in random.sample(base_pool, k=k):
        selected_nationalities.add(nat)

    # 모든 체크박스 초기화
    for nat in nationality_description:
        nationality_vars[nat].set(0)

    # 랜덤 선택 후 체크박스 UI 반영
    for nat in selected_nationalities:
        nationality_vars[nat].set(1)

    generate_prompt()


def toggle_nationality(nat):
    if nationality_vars[nat].get():
        selected_nationalities.add(nat)
    else:
        selected_nationalities.discard(nat)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    root.update()


# 리셋 함수
def reset_text():
    output_text.delete("1.0", tk.END)




# ------------------------------ UI ------------------------------
root = tk.Tk()
root.title("🎬 동영상 프롬프트 생성기 디럭스 버전")
style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding=10)
frame.grid()


# ✅ 이제 IntVar 선언
nationality_vars = {nat: tk.IntVar(value=1) for nat in nationality_description}
selected_nationalities = set(nationality_description.keys())


# ✅ 국적 선택 Frame
nationality_frame = ttk.LabelFrame(frame, text="국적 선택")
nationality_frame.grid(row=0, column=0, columnspan=2, pady=(5, 0), sticky="ew")



## ✅ Checkbutton 반복 생성
for idx, nat in enumerate(nationality_description.keys()):
    cb = tk.Checkbutton(
        nationality_frame,
        text=nat,
        variable=nationality_vars[nat],
        command=lambda n=nat: toggle_nationality(n)
    )
    cb.grid(row=0, column=idx, padx=5)



# ✅ 커스텀 세부사항 입력 필드
ttk.Label(
    frame,
    text="원하는 영상 장면에 대한 세부사항을 자유롭게 적어보세요. (선택사항, 영어 권장)"
).grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=(5, 2))

custom_note_entry = tk.Entry(frame, width=60)
custom_note_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="ew")
input_vars["custom_note_var"] = custom_note_entry

# ✅ 필드 목록
fields = [
    ("장르/톤", list(genre_tone), "genre_var"),
    ("배경", list(background), "background_var"),
    ("시간대", list(time), "time_var"),
    ("등장 인물 수", list(character_count_dict.keys()), "character_count_var"),
    ("행동", list(character_action), "action_var"),
    ("감정", list(emotion), "emotion_var"),
    ("카메라 시점", list(camera_view), "camera_view_var"),
    ("카메라 무빙", list(camera_movement), "camera_move_var"),
    ("조명", list(lighting), "lighting_dict_var"),
    ("의상 스타일", list(outfit), "outfit_var"),
    ("체형", list(body_shape), "body_shape_var"),
    ("헤어스타일", list(hairstyle), "hairstyle_var"),
    ("옷감 반응", list(fabric_response), "fabric_response_var"),
    ("렌더링 스타일", list(rendering_translation), "rendering_var"),
    ("얼굴형", list(face_shape), "face_shape_var"),  # ✅ 이게 꼭 있어야 합니다
    ("네일 스타일", list(manicure_text), "manicure_var"),
    ("발 스타일", list(foot_text), "foot_var"), # ✅ 반드시 있어야 함

]

start_row = 3
for i, (label, values, varname) in enumerate(fields):
    ttk.Label(frame, text=label).grid(row=start_row + i, column=0, sticky="e", padx=3, pady=2)
    box = ttk.Combobox(frame, values=values, width=50)
    box.set(values[0])
    box.grid(row=start_row + i, column=1, padx=3, pady=2)
    input_vars[varname] = box

btn_row = start_row + len(fields) + 1
btn_frame = ttk.Frame(frame)
btn_frame.grid(row=btn_row, column=0, columnspan=2, sticky="ew", pady=10)

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)

ttk.Button(btn_frame, text="🎯 프롬프트 생성", command=generate_prompt).grid(row=0, column=0, padx=3, sticky="ew")
ttk.Button(btn_frame, text="🎲 랜덤 생성", command=set_random_values).grid(row=0, column=1, padx=3, sticky="ew")
ttk.Button(btn_frame, text="📋 복사하기", command=copy_to_clipboard).grid(row=0, column=2, padx=3, sticky="ew")
ttk.Button(btn_frame, text="🔄 리셋", command=reset_text).grid(row=1, column=1, padx=3, pady=(5, 0), sticky="ew")

# 안내 문구들
ttk.Label(frame, text="| *랜덤 생성시 일부 항목 조합이 비논리적일 수 있습니다.", foreground="black").grid(
    row=btn_row+3, column=0, columnspan=2, sticky="ew", padx=5, pady=(0, 2))
ttk.Label(frame, text="| *행동과 감정, 배경의 논리적 연결을 고려해 수정할 수 있습니다.", foreground="black").grid(
    row=btn_row+4, column=0, columnspan=2, sticky="ew", padx=5, pady=(0, 2))
ttk.Label(frame, text="| *생성된 프롬프트는 이미지/영상 생성 AI에서 직접 활용 가능합니다.", foreground="black").grid(
    row=btn_row+5, column=0, columnspan=2, sticky="ew", padx=5, pady=(0, 2))

# ✅ 출력 텍스트 박스
output_text = tk.Text(frame, height=50, width=60, wrap=tk.WORD)
output_text.grid(row=0, column=2, rowspan=btn_row+10, padx=(15, 0), sticky="n")

root.mainloop()
