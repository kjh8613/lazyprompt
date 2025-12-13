import os
import re
from pathlib import Path

def fix_file(file_path):
    """Fix frontmatter by removing ALL line breaks within quotes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match titles that span multiple lines
        # Pattern: title: "...\n..."
        def fix_title_match(match):
            full_match = match.group(0)
            # Remove all newlines within the title string
            fixed = re.sub(r'\n\s*', ' ', full_match)
            return fixed
        
        # Fix multi-line titles
        original = content
        content = re.sub(
            r'title:\s*"[^"]*\n[^"]*"',
            fix_title_match,
            content,
            flags=re.MULTILINE
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Fixed"
        else:
            return False, "No change"
            
    except Exception as e:
        return False, f"Error: {e}"

# Process all markdown files
content_dir = Path(r'c:\Users\user\Documents\visual\lazyprompt\content')
fixed_count = 0

for md_file in content_dir.rglob('*.md'):
    success, msg = fix_file(md_file)
    if success:
        fixed_count += 1
        print(f"✓ {md_file.name}")

print(f"\n✓ Files fixed: {fixed_count}")
