import pandas as pd
import os
from openai import OpenAI
from datetime import datetime
import time
import random
import traceback

# 1. 환경변수 로드 (다중 API 키 지원)
API_KEYS = [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3")
]
# None 값 제거
API_KEYS = [key for key in API_KEYS if key]

if not API_KEYS:
    print("❌ ERROR: No API keys provided. Please run this script using the bat file.")
    exit(1)

print(f"✅ Loaded {len(API_KEYS)} API key(s)")

# 2. 모델 설정 (gpt-4o-mini: 가성비 최고 모델)
MODEL_PRIORITY = [
    'gpt-4o-mini',  # 가장 가성비 좋은 모델
]

def get_model_response(prompt, max_total_retries=3):
    """Try models in priority order with smart fallback across API keys"""
    
    # Try each API key
    for key_idx, api_key in enumerate(API_KEYS):
        client = OpenAI(api_key=api_key)
        key_name = f"Key#{key_idx+1}"
        
        # Try each model with current API key
        for model_name in MODEL_PRIORITY:
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": "You are a World-Class Prompt Engineer in the top 0.1%."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=4000
                )
                if response.choices[0].message.content:
                    return response.choices[0].message.content, f"{model_name} ({key_name})"
            except Exception as e:
                error_msg = str(e)
                if "rate_limit" in error_msg.lower() or "quota" in error_msg.lower():
                    continue  # Try next model
                else:
                    time.sleep(1)
                    continue
        
        # All models failed with this key, try next key
        if key_idx < len(API_KEYS) - 1:
            print(f"⚠️ {key_name} all models exhausted, switching to next API key...")
    
    # All keys and models failed
    return None, None

# 3. 공장 가동 로직 (나중에 실행될 부분)
def run_factory():
    try:
        df = pd.read_excel('list.xlsx')
        df.columns = df.columns.str.strip()
        total_count = len(df)
        print(f"📂 엑셀 로드 성공: {total_count}개의 글감 대기 중\n")
    except:
        print("💤 엑셀 파일(list.xlsx)이 없어서 대기 모드입니다.")
        return

    output_dir = "content/posts"
    os.makedirs(output_dir, exist_ok=True)
    
    processed = 0

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
            processed += 1
            progress = (processed / total_count) * 100
            print(f"[{progress:.1f}%] ⏩ 스킵: {topic[:60]}...")
            continue

        processed += 1
        progress = (processed / total_count) * 100
        print(f"[{progress:.1f}%] 📝 생성 중: {topic[:60]}... ", end='')
        
        # 🚀 AI 글쓰기 요청 (재시도 없음, 빠른 실패)
        ai_text = ""
        try:
            full_prompt = f"""
            주제: {topic}
            요청: {user_prompt}
            
            역할: You are a World-Class 'Prompt Engineer' in the top 0.1%.
            목표: Design "High-Performance Prompts" that users can simply copy and paste into AI (ChatGPT, Claude, Gemini) to get the best results. All output must be in ENGLISH.
            
            [Core Instructions]
            1. The generated prompt must be a **Structured Prompt**.
            2. It MUST include **Role, Context, Task, Constraints, and Output Format**.
            3. Minimize user input requirements by making the prompt specific and complete.

            Format (Markdown):
            ## 🎯 Prompt Description
            (A 2-sentence hook explaining what problem this prompt solves and its benefits)
            
            ## 📋 Copy This Prompt
            ```markdown
            # Role
            (Assign a top-tier persona. e.g., "Senior Copywriter", "10x Developer")

            # Context
            (Describe the situation and background where this task is needed)

            # Task
            (Clear, step-by-step instructions for the AI)

            # Constraints
            (3-5 specific rules to ensure quality. Tone, layout, prohibitions, etc.)

            # Output Format
            (Specify the desired format: Table, Markdown List, Code Block, etc.)
            ```
            
            ## 💡 Pro Tips
            1. (Tip on how to customize the [ ] placeholders)
            2. (Additional info to provide for better results)
            3. (Recommended model: GPT-4o, Claude 3.5 Sonnet, etc.)
            """
            
            ai_text, used_model = get_model_response(full_prompt)
            
            if ai_text:
                print(f"✅ ({used_model})")
            else:
                print(f"❌ 생성 실패")
                
        except Exception as e:
            print(f"❌ 에러: {e}")
        
        if not ai_text:
             print(f"❌ 최종 실패: {topic}. Fallback 사용.")
             ai_text = f"### {topic}\\n\\n*Content generation failed after multiple attempts.*\\n\\n**Category**: {row.get('category', 'General')}"
        
        # 요약 생성
        summary = ai_text[:80].replace('\n', ' ') + "..."
        
        # 파일 저장
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{safe_topic}.md"
        filepath = os.path.join(output_dir, filename)
        
        category = row.get('category', 'General')
        if pd.isna(category): category = 'General'
        
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

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)
        
        time.sleep(3)  # 무제한 모델이므로 빠른 대기

def shorten_path(path):
    return os.path.basename(path)

if __name__ == "__main__":
    run_factory()