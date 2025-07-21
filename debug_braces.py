#!/usr/bin/env python3
"""Debug script to count braces in pin-nxtscape-agents-together.patch"""

def count_braces_in_patch():
    patch_file = "patches/nxtscape/pin-nxtscape-agents-together.patch"
    
    with open(patch_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    open_braces = 0
    close_braces = 0
    in_diff_section = False
    
    print("Analyzing braces in added lines:")
    print("-" * 50)
    
    for line_num, line in enumerate(content.split('\n'), 1):
        # Skip patch metadata lines
        if line.startswith(('From ', 'Date:', 'Subject:', '---', '+++', 'index ', 'diff --git')):
            continue
        
        # Check if we're in a diff section
        if line.startswith('@@'):
            in_diff_section = True
            continue
            
        # Only process lines in diff sections
        if not in_diff_section:
            continue
            
        # Count braces only in added lines (starting with +)
        if line.startswith('+') and not line.startswith('+++'):
            code_line = line[1:]  # Remove the + prefix
            
            # Count braces
            line_open = code_line.count('{')
            line_close = code_line.count('}')
            
            if line_open > 0 or line_close > 0:
                print(f"Line {line_num}: '{code_line.strip()}' -> {line_open} open, {line_close} close")
            
            open_braces += line_open
            close_braces += line_close
    
    print("-" * 50)
    print(f"Total open braces: {open_braces}")
    print(f"Total close braces: {close_braces}")
    print(f"Balance: {open_braces - close_braces}")
    
    if open_braces == close_braces:
        print("✓ Braces are balanced!")
    else:
        print(f"✗ Braces are NOT balanced! Difference: {open_braces - close_braces}")

if __name__ == '__main__':
    count_braces_in_patch()