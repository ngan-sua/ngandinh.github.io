
import os

game_file = r'layouts\baseof.html'

if os.path.exists(game_file):
    with open(game_file, 'rb') as f:
        content_bytes = f.read()

    # Remove BOM if present
    if content_bytes.startswith(b'\xef\xbb\xbf'):
        content_bytes = content_bytes[3:]
    
    content = content_bytes.decode('utf-8')
    
    # The line to remove
    target = '<link rel="icon" href="{{ "images/avatar.jpg" | relURL }}" type="image/jpeg">'
    
    if target in content:
        print("Found target, removing...")
        new_content = content.replace(target, '')
        # Clean up potential empty line left behind if it was on its own line
        new_content = new_content.replace('\n    \n', '\n')
        
        with open(game_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Revert successful.")
    else:
        print("Target not found. Content might differ.")
        # Print a snippet to debug
        print(content[:500])
else:
    print("File not found.")
