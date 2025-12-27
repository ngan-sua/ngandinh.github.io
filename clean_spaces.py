
import os
import re

target_dir = 'layouts'

# Regex to find {{ "  string" | relURL }} pattern
# We look for {{ " followed by one or more spaces
pattern = re.compile(r'(\{\{\s*")\s+([^"]*"\s*\|\s*rel(?:Lang)?URL\s*\}\})')

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if BOM exists and strip it for processing, but we might want to preserve it if needed?
    # Actually, Hugo prefers no BOM.
    if content.startswith('\ufeff'):
        content = content.replace('\ufeff', '')

    new_content = pattern.sub(r'\1\2', content)
    
    if content != new_content:
        print(f"Fixed spaces in: {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            clean_file(os.path.join(root, file))
