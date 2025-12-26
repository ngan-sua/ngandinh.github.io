import re
import os

files = [r'layouts\baseof.html', r'layouts\partials\sidebar.html']

for fpath in files:
    if not os.path.exists(fpath):
        print(f"Skipping {fpath} (not found)")
        continue
        
    with open(fpath, 'rb') as f:
        content = f.read().decode('utf-8')
    
    # Regex to capture: {{ " <space> path" | relURL }}
    # We want to remove the leading spaces inside the string.
    # Pattern: {{ " + MATCH " | relURL }}
    # We replace with {{ "MATCH" | relURL }}
    
    # Be careful with multiple occurrences
    def replacer(match):
        inner = match.group(1) # The content inside quotes
        clean_inner = inner.lstrip() # Remove leading space
        return f'{{{{ "{clean_inner}" | relURL }}}}'

    # Pattern explains:
    # \{\{        match {{
    # \s*         match optional whitespace
    # "           match quote
    # ([^"]+)     match content (group 1)
    # "           match quote
    # \s*\|\s*relURL match | relURL
    # \s*\}\}     match }}
    
    pattern = r'\{\{\s*"([^"]+)"\s*\|\s*relURL\s*\}\}'
    
    new_content = re.sub(pattern, replacer, content)
    
    if content != new_content:
        print(f"Fixing {fpath}")
        with open(fpath, 'wb') as f:
            f.write(new_content.encode('utf-8'))
    else:
        print(f"No changes for {fpath}")
