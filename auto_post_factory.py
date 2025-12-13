import google.generativeai as genai
import pandas as pd # 엑셀 읽기용
import os
import time
from datetime import datetime

# ==========================================
# 1. 설정
# ==========================================
GEMINI_KEY = "AIzaSyCNK1EOdfsNyiZ_IyUB8_BT9vfUdYZ_jpc" # 키 입력 필수!
EXCEL_FILE = "keywords.xlsx"       # 방금 만든 엑셀 파일명
OUTPUT_DIR = "./content/posts"     # Hugo 글 저장 위치

# 쿠팡 파트너스 배너 (HTML 코드)
# 실제 파트너스에서 생성한 '다이내믹 배너'나 '상품 링크'를 넣으세요
COUPANG_BANNERS = {
    "tech": '<iframe src="https://ads-partners.coupang.com/widgets.html?..." width="100%" height="200" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>',
    "book": '<iframe src="https://ads-partners.coupang.com/widgets.html?..." width="100%" height="200" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>',
    "general": '<iframe src="https://ads-partners.coupang.com/widgets.html?..." width="100%" height="200" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>'
}

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# ==========================================
# 2. 글쓰기 로직
# ==========================================
def create_post_from_row(row):
    topic = row['주제']      # 엑셀 A열 헤더 이름
    category = row['카테고리'] # 엑셀 B열 헤더 이름
    banner_type = row['배너타입'] # 엑셀 C열 헤더 이름
    
    print(f"🏭 공장 가동 중... 주제: {topic}")

    # 해당 타입의 배너 HTML 가져오기 (없으면 general)
    selected_banner = COUPANG_BANNERS.get(banner_type, COUPANG_BANNERS["general"])

    prompt = f"""
    당신은 'AI 프롬프트 도서관'의 전문 사서이자 에디터입니다.
    주제: '{topic}'에 대한 블로그 포스트를 **Hugo Markdown** 형식으로 작성하세요.

    [형식 가이드]
    ---
    title: "{topic} - 1초 만에 복사해서 쓰는 AI 프롬프트"
    date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')}
    draft: false
    categories: [{category}]
    tags: [AI, 프롬프트, {topic}, Lazyprompt]
    ---

    ## 1. 개요
    이 프롬프트는 **{topic}** 작업을 자동화하거나 퀄리티를 높이고 싶은 분들을 위해 제작되었습니다.

    {{< adsense >}}

    ## 2. 프롬프트 (복사 가능)
    아래 박스의 내용을 복사해서 AI(ChatGPT, Midjourney 등)에 붙여넣으세요.

    ```text
    (여기에 {topic}에 최적화된 고퀄리티 영어/한글 프롬프트를 작성)
    ```

    ## 3. 사용 팁
    * (이 프롬프트를 더 잘 쓰기 위한 파라미터 조절 팁이나 변형 가이드 3가지)

    ---
    ### ⚡ 이 작업에 추천하는 장비/자료
    {selected_banner}
    
    > **더 많은 무료 프롬프트가 필요하신가요?**
    > 👉 [Lazyprompt.me 홈으로 가기](https://lazyprompt.me)
    """

    try:
        response = model.generate_content(prompt)
        return response.text.replace("```markdown", "").replace("```", "").strip()
    except Exception as e:
        print(f"❌ 생성 실패 ({topic}): {e}")
        return None

# ==========================================
# 3. 실행 (엑셀 읽기 -> 생성 -> 저장)
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 엑셀 파일 읽기
try:
    df = pd.read_excel(EXCEL_FILE)
    print(f"📂 엑셀 파일 로드 성공! 총 {len(df)}개의 주제를 발견했습니다.")
    
    for index, row in df.iterrows():
        content = create_post_from_row(row)
        
        if content:
            # 파일명: 2024-05-20-미드저니-고양이.md
            safe_title = str(row['주제']).replace(" ", "-").replace("/", "").replace("?", "")
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{safe_title}.md"
            save_path = os.path.join(OUTPUT_DIR, filename)
            
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"✅ 저장 완료 [{index+1}/{len(df)}]: {filename}")
            time.sleep(2) # 너무 빠르면 API 제한 걸릴 수 있음

    print("\n🎉 모든 작업이 끝났습니다! Hugo 서버를 실행해 확인해보세요.")

except Exception as e:
    print(f"🚫 엑셀 파일을 읽을 수 없습니다: {e}")
    print("엑셀 파일이 같은 폴더에 있는지, 열 이름이 '주제', '카테고리', '배너타입' 인지 확인해주세요.")