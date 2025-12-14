import pandas as pd
import os
from openai import OpenAI
import time
import json

# Load API keys from environment variables (set by bat file)
API_KEYS = [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3")
]
# Remove None values
API_KEYS = [key for key in API_KEYS if key]

if not API_KEYS:
    print("❌ ERROR: No API keys provided. Please run this script using the bat file.")
    exit(1)

print(f"✅ Loaded {len(API_KEYS)} API key(s)")

# Use gpt-4o-mini (가성비 최고 모델: 저렴하면서 정확도 높음)
MODEL_PRIORITY = [
    'gpt-4o-mini',  # 가장 가성비 좋은 모델
]

def generate_topics_batch(batch_size=5, existing_topics=None):
    """Generate a batch of blog topics using OpenAI API with multi-API-key fallback"""
    
    if existing_topics is None:
        existing_topics = []
    
    prompt = f"""
You are a 'Global Blog Automation Data Expert'. Generate exactly {batch_size} unique blog topic ideas.

**CRITICAL RULES**:
1. Topics must be deeply rooted in **Western culture, lifestyle, and economy**
2. Focus on highly **niche** subjects (not generic topics)
3. Target **high demand, low supply** areas (frequently searched but scarce content)
4. Emphasize **economic benefits, lifestyle improvements, or tangible advantages**
5. Categories must be **progressively diverse** (don't repeat the same category)
6. All content must be in **ENGLISH** (SEO-optimized for Google.com)

**OUTPUT FORMAT** (Return ONLY valid JSON, no markdown):
[
  {{
    "topic": "SEO-friendly catchy title targeting high-traffic keywords",
    "prompt": "Detailed instruction in English for the AI writer. Must explicitly state to write the blog post in English. Include specific requirements like code snippets, examples, or actionable tips.",
    "category": "Single English word (e.g., Finance, Health, Business, Tech, Lifestyle)"
  }},
  ...
]

**EXAMPLES OF GOOD TOPICS**:
- "How to Legally Reduce Property Taxes in California: 7 Proven Strategies"
- "Side Hustles for Retirees: Top 10 Income Streams After 65"
- "401(k) vs Roth IRA: Which Retirement Plan Saves You More in 2025?"

**EXISTING TOPICS TO AVOID**:
{json.dumps(existing_topics[-20:]) if existing_topics else "None"}

Generate {batch_size} completely NEW topics following all rules above.
"""

    # Try each API key
    for key_idx, api_key in enumerate(API_KEYS):
        client = OpenAI(api_key=api_key)
        key_name = f"Key#{key_idx+1}"
        
        # Try models in priority order with current API key
        for model_name in MODEL_PRIORITY:
            max_retries = 2
            for attempt in range(max_retries):
                try:
                    response = client.chat.completions.create(
                        model=model_name,
                        messages=[
                            {"role": "system", "content": "You are a helpful AI assistant specialized in generating blog topics."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.8,
                        max_tokens=2000
                    )
                    
                    text = response.choices[0].message.content.strip()
                    
                    # Remove markdown code blocks if present
                    if text.startswith("```"):
                        text = text.split("```")[1]
                        if text.startswith("json"):
                            text = text[4:]
                        text = text.strip()
                    
                    # Parse JSON
                    topics = json.loads(text)
                    
                    # Validate structure
                    if isinstance(topics, list) and len(topics) > 0:
                        valid_topics = []
                        for t in topics:
                            if all(key in t for key in ['topic', 'prompt', 'category']):
                                valid_topics.append(t)
                        
                        if valid_topics:
                            print(f"✓ {model_name} ({key_name})")
                            return valid_topics
                    
                except json.JSONDecodeError as e:
                    if attempt < max_retries - 1:
                        time.sleep(1)
                        continue
                except Exception as e:
                    error_msg = str(e)
                    if "rate_limit" in error_msg.lower() or "quota" in error_msg.lower():
                        break  # Try next model with this key
                    elif attempt < max_retries - 1:
                        time.sleep(2)
                        continue
        
        # All models failed with this key
        if key_idx < len(API_KEYS) - 1:
            print(f"⚠️ {key_name} exhausted, switching to next API key...")
    
    return None

def generate_list(total_count):
    """Generate the complete list of blog topics"""
    
    print(f"\n{'='*60}")
    print(f"🚀 Lazy Prompt List Generator")
    print(f"{'='*60}")
    print(f"📊 Target: {total_count} unique blog topics")
    print(f"🎯 Focus: Western, Niche, High-Demand Topics")
    print(f"{'='*60}\n")
    
    all_topics = []
    existing_titles = []
    batch_size = 5
    batches_needed = (total_count + batch_size - 1) // batch_size
    
    for batch_num in range(batches_needed):
        remaining = total_count - len(all_topics)
        current_batch_size = min(batch_size, remaining)
        
        print(f"📦 Batch {batch_num + 1}/{batches_needed} (Generating {current_batch_size} topics)...", end=' ')
        
        batch_topics = generate_topics_batch(current_batch_size, existing_titles)
        
        if batch_topics:
            # Filter duplicates
            new_topics = []
            for topic in batch_topics:
                if topic['topic'] not in existing_titles:
                    new_topics.append(topic)
                    existing_titles.append(topic['topic'])
            
            all_topics.extend(new_topics)
            print(f"✅ Added {len(new_topics)} topics (Total: {len(all_topics)}/{total_count})")
        else:
            print(f"❌ Failed")
        
        # Rate limiting (RPM 제한 방지)
        if batch_num < batches_needed - 1:
            time.sleep(6)  # 6초 대기 (RPM 제한 방지)
    
    return all_topics

def save_to_excel(topics, filename='list.xlsx'):
    """Save topics to Excel file"""
    
    if not topics:
        print("❌ No topics to save!")
        return False
    
    try:
        df = pd.DataFrame(topics)
        df = df[['topic', 'prompt', 'category']]  # Ensure column order
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n✅ Successfully saved {len(topics)} topics to '{filename}'")
        return True
    except Exception as e:
        print(f"\n❌ Error saving to Excel: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("🎨 LAZY PROMPT - Auto List Generator")
    print("="*60)
    print("Generate niche, Western-focused blog topics automatically!")
    print("="*60 + "\n")
    
    # Get user input
    while True:
        try:
            count_input = input("📝 How many topics do you want to generate? (1-200): ").strip()
            count = int(count_input)
            
            if 1 <= count <= 200:
                break
            else:
                print("⚠️ Please enter a number between 1 and 200")
        except ValueError:
            print("⚠️ Please enter a valid number")
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Cancelled by user")
            exit(0)
    
    # Confirm overwrite
    if os.path.exists('list.xlsx'):
        try:
            print(f"\n⚠️ WARNING: 'list.xlsx' already exists and will be OVERWRITTEN")
            confirm = input("Continue? (y/n): ").strip().lower()
            if confirm != 'y':
                print("👋 Cancelled")
                return
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Cancelled by user")
            exit(0)
    
    # Generate topics
    start_time = time.time()
    topics = generate_list(count)
    elapsed = time.time() - start_time
    
    # Save to Excel
    if topics:
        save_to_excel(topics)
        
        print(f"\n{'='*60}")
        print(f"🎉 GENERATION COMPLETE!")
        print(f"{'='*60}")
        print(f"⏱️  Time taken: {elapsed:.1f} seconds")
        print(f"📊 Topics generated: {len(topics)}/{count}")
        print(f"📁 Saved to: list.xlsx")
        print(f"\n💡 Next step: Run 'deploy_posts.bat' to create blog posts!")
        print(f"{'='*60}\n")
    else:
        print(f"\n❌ Failed to generate topics. Please try again.\n")

if __name__ == "__main__":
    main()
