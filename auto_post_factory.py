import pandas as pd
import os
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
import time
import random

# 1. 환경변수 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. 모델 설정 (🏆 Best Pick: 무제한/초고속 모델 적용)
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash-lite') # 이걸로 고정!

# 3. 공장 가동 로직 (나중에 실행될 부분)
def run_factory():
    try:
        df = pd.read_excel('list.xlsx')
        df.columns = df.columns.str.strip()
        print(f"📂 엑셀 로드 성공: {len(df)}개의 글감 대기 중")
    except:
        print("💤 엑셀 파일(list.xlsx)이 없어서 대기 모드입니다.")
        return

    output_dir = "content/posts"
    os.makedirs(output_dir, exist_ok=True)

    for index, row in df.iterrows():
        try:
            topic = str(row['topic']).strip()
            user_prompt = str(row['prompt']).strip()
            if not topic: continue

            print(f"📝 생성 중: {topic} ... ", end='')
            
            # 🚀 AI 글쓰기 요청
            # 🚀 AI 글쓰기 요청
            ai_text = ""
            try:
                full_prompt = f"주제: {topic}\n요청: {user_prompt}\n형식: 마크다운 블로그 글. 서론-본론-결론."
                response = model.generate_content(full_prompt)
                ai_text = response.text
            except Exception as e:
                print(f"⚠️ API Limit/Error: {e}. Using fallback content.")
                ai_text = f"### {topic}\n\n*Content generation is pending due to high traffic.*\n\nThis prompt will be available shortly. Please check back later!\n\n**Category**: {row.get('category', 'General')}"
            
            summary = ai_text[:80].replace('\n', ' ') + "..."
            
            # 🎨 이미지 및 파일 저장 로직
            safe_topic = "".join([c if c.isalnum() or c in (' ', '-') else '' for c in topic]).strip().replace(' ', '-')
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{safe_topic}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 카테고리 처리 (없으면 'General')
            category = row.get('category', 'General')
            if pd.isna(category): category = 'General'
            
            # Picsum 랜덤 이미지 (무제한)
            image_url = f"https://picsum.photos/seed/{safe_topic}{random.randint(1,100)}/800/400"
            summary = response.text[:80].replace('\n', ' ') + "..."

            post_content = f"""---
title: "{topic}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
summary: "{summary}"
categories: ["{category}"]
cover:
    image: "{image_url}"
    alt: "{topic}"
    relative: false
---
cover:
    image: "{image_url}"
    alt: "{topic}"
    relative: false
---
{ai_text}"""

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(post_content)
            print(f"✅ 완료: {os.path.abspath(filepath)}")
            time.sleep(3)
        except Exception as e:
            print(f"❌ 에러 발생 ({topic}): {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    run_factory()