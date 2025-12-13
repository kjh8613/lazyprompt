import os
import glob

POSTS_DIR = "./content/posts"

print("🎨 Adding thumbnails to existing posts...")

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "cover:" in content:
            print(f"⏭️  Skipping {os.path.basename(filepath)} (already has cover)")
            continue

        # Use filename as seed for consistent images
        filename = os.path.basename(filepath)
        seed = filename.replace(".md", "")
        
        cover_yaml = f"""cover:
    image: "https://picsum.photos/seed/{seed}/800/400"
    alt: "Thumbnail for {seed}"
    relative: false
"""
        
        # Insert before the second '---' delimiter
        parts = content.split("---", 2)
        if len(parts) >= 3:
            # parts[0] is empty (before first ---)
            # parts[1] is frontmatter
            # parts[2] is body
            new_frontmatter = parts[1].rstrip() + "\n" + cover_yaml
            new_content = "---" + new_frontmatter + "---\n" + parts[2]
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Updated {filename}")
        else:
            print(f"⚠️  Skipping {filename} (cannot parse frontmatter)")
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")

print("🎉 Thumbnail injection complete!")
