import pandas as pd
import os
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
import time
import random
import traceback

# 1. 환경변수 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. 모델 설정 (🏆 Best Pick: 무제한/초고속 모델 적용)
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash-lite') # 4K RPM (Highest limit)

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
        topic = str(row['topic']).strip()
        user_prompt = str(row['prompt']).strip()
        if not topic: continue

        print(f"📝 생성 중: {topic} ... ", end='')
        
        # 🚀 AI 글쓰기 요청 (Retry Logic Added)
        ai_text = ""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                full_prompt = f"주제: {topic}\n요청: {user_prompt}\n형식: 마크다운 블로그 글. 서론-본론-결론.\n조건: 풍부한 내용, 2000자 내외."
                response = model.generate_content(full_prompt)
                ai_text = response.text
                if ai_text: break
            except Exception as e:
                print(f"⚠️ 시도 {attempt+1}/{max_retries} 실패: {e}")
                if "429" in str(e):
                    time.sleep(10) # Wait 10s on Rate Limit
                else:
                    time.sleep(2)
        
        if not ai_text:
             print(f"❌ 최종 실패: {topic}. Fallback 사용.")
             ai_text = f"### {topic}\n\n*Content generation failed after multiple attempts.*\n\n**Category**: {row.get('category', 'General')}"
        
        # 요약 생성
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

        post_content = f"""---
title: "{topic}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
draft: false
summary: "{summary}"
categories: ["{category}"]
cover:
    image: "{image_url}"
    alt: "{topic}"
    relative: false
---
{ai_text}"""

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(post_content)
            print(f"✅ 완료: {shorten_path(filepath)}")
            time.sleep(2) # 2초 대기 (API 보호)
        except Exception as e:
            print(f"❌ 파일 저장 에러 ({topic}): {e}")
            traceback.print_exc()

def shorten_path(path):
    return os.path.basename(path)

if __name__ == "__main__":
    run_factory()