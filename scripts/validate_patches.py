#!/usr/bin/env python3
"""
Patch Validation Script for PrivacyAgent
Automatically checks patches for common syntax issues and best practices.
"""

import os
import re
import sys
from pathlib import Path

def check_brace_balance(content):
    """Check if braces are properly balanced in patch content."""
    open_braces = 0
    issues = []
    in_diff_section = False
    
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
        # Ignore removed lines (starting with -) and context lines
        if line.startswith('+') and not line.startswith('+++'):
            code_line = line[1:]  # Remove the + prefix
            
            # Skip lines that are just comments or strings
            stripped = code_line.strip()
            if stripped.startswith(('//')) or stripped.startswith(('*', '/*')):
                continue
                
            # Count braces
            line_open = code_line.count('{')
            line_close = code_line.count('}')
            
            open_braces += line_open
            open_braces -= line_close
            
            if open_braces < 0:
                issues.append(f"Line {line_num}: Unmatched closing brace")
                open_braces = 0  # Reset to continue checking
    
    # Only report unclosed braces if we found actual code changes
    if open_braces > 0 and in_diff_section:
        issues.append(f"End of file: {open_braces} unclosed braces")
    
    return issues

def check_patch_format(content):
    """Check if patch follows proper format."""
    issues = []
    
    # Check for basic patch structure
    if not content.startswith('From '):
        issues.append("Missing proper patch header (should start with 'From ')")
    
    # Check for diff markers (more flexible)
    if '---' not in content or '+++' not in content:
        issues.append("Missing file diff markers")
    
    # Check for at least one diff section
    if '@@' not in content:
        issues.append("Missing diff sections")
    
    return issues

def check_branding_consistency(content, filename):
    """Check for consistent branding across patches."""
    issues = []
    
    # Define expected branding terms
    old_terms = ['Chromium', 'BrowserOS', 'Chrome']
    new_term = 'PrivacyAgent'
    
    if 'branding' in filename.lower():
        for line_num, line in enumerate(content.split('\n'), 1):
            if line.startswith('+') and any(term in line for term in old_terms):
                if new_term not in line:
                    issues.append(f"Line {line_num}: Inconsistent branding - should use '{new_term}'")
    
    return issues

def validate_patch_file(filepath):
    """Validate a single patch file."""
    print(f"\nValidating: {filepath.name}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    all_issues = []
    
    # Run all checks
    all_issues.extend(check_patch_format(content))
    all_issues.extend(check_brace_balance(content))
    all_issues.extend(check_branding_consistency(content, filepath.name))
    
    if all_issues:
        print(f"Found {len(all_issues)} issues:")
        for issue in all_issues:
            print(f"   • {issue}")
        return False
    else:
        print("No issues found")
        return True

def main():
    """Main validation function."""
    patches_dir = Path(__file__).parent.parent / 'patches' / 'nxtscape'
    
    if not patches_dir.exists():
        print(f"Error: Patches directory not found: {patches_dir}")
        sys.exit(1)
    
    print("BrowserOS Patch Validator")
    print("=" * 40)
    
    patch_files = list(patches_dir.glob('*.patch'))
    if not patch_files:
        print("Error: No patch files found")
        sys.exit(1)
    
    valid_count = 0
    total_count = len(patch_files)
    
    for patch_file in sorted(patch_files):
        if validate_patch_file(patch_file):
            valid_count += 1
    
    print("\n" + "=" * 40)
    print(f"Results: {valid_count}/{total_count} patches valid")
    
    if valid_count == total_count:
        print("All patches are valid!")
        sys.exit(0)
    else:
        print("Some patches need attention")
        sys.exit(1)

if __name__ == '__main__':
    main()