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
    model = genai.GenerativeModel('gemini-2.0-flash-exp') # Switching to Experimental Model for quota

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

        # 🔍 중복 방지 로직 (파일명 기반 체크)
        safe_topic = "".join([c if c.isalnum() or c in (' ', '-') else '' for c in topic]).strip().replace(' ', '-')
        existing_files = os.listdir(output_dir)
        is_duplicate = False
        for f in existing_files:
            if f.endswith(f"-{safe_topic}.md"):
                is_duplicate = True
                break
        
        if is_duplicate:
            print(f"⏩ 스킵 (이미 있음): {topic}")
            continue

        print(f"📝 생성 중: {topic} ... ", end='')
        
        # 🚀 AI 글쓰기 요청 (Retry Logic Added)
        ai_text = ""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                full_prompt = f"""
                주제: {topic}
                요청: {user_prompt}
                
                역할: 당신은 세계 상위 0.1% 수준의 '프롬프트 엔지니어'입니다.
                목표: 사용자가 복사해서 AI(ChatGPT, Gemini)에 붙여넣기만 하면 최고의 결과를 얻을 수 있는 "고성능 프롬프트"를 설계하세요.
                
                [핵심 지침]
                1. 생성되는 프롬프트는 단순한 문장이 아니라, **구조화된 프롬프트(Structured Prompt)** 양식을 갖춰야 합니다.
                2. 프롬프트 내부에는 반드시 **Role(역할), Context(배경), Task(지시사항), Constraints(제약조건), Output(출력형식)**이 포함되어야 합니다.
                3. 사용자가 추가 입력을 최소화하도록 내용을 구체적으로 완성해서 작성하세요.

                형식 (마크다운):
                ## 🎯 프롬프트 설명
                (이 프롬프트가 해결해주는 문제와 기대 효과를 2문장으로 매력적으로 요약)
                
                ## 📋 프롬프트 내용 (복사해서 사용하세요)
                ```markdown
                # Role
                (주제에 딱 맞는 최고의 전문가 페르소나 부여. 예: 10년차 카피라이터, 시니어 개발자 등)

                # Context
                (이 작업이 필요한 상황과 배경을 구체적으로 서술)

                # Task
                (AI가 수행해야 할 미션을 단계별로 명확하게 지시)

                # Constraints
                (결과물의 퀄리티를 높이기 위한 구체적인 제약 조건 3~5가지. 어조, 금지사항 등)

                # Output Format
                (표, 리스트, 코드 블록 등 원하는 결과물의 형식을 지정)
                ```
                
                ## 💡 사용 팁
                1. (이 프롬프트를 활용할 때 [ ] 변수 부분만 바꿔서 응용하는 꿀팁)
                2. (더 좋은 결과를 얻기 위해 추가로 제공하면 좋은 정보)
                3. (이 프롬프트가 가장 효과적인 모델 추천)
                """
                
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
title: "{topic.replace('"', '\\"')}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
draft: false
summary: "{summary.replace('"', '\\"')}"
categories: ["{category}"]
cover:
    image: "{image_url}"
    alt: "{topic.replace('"', '\\"')}"
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