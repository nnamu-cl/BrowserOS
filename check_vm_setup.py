#!/usr/bin/env python3
"""
VM Setup Checker for PrivacyAgent Build
This script helps you verify your VM setup and find the correct paths
"""

import os
import sys
import subprocess
from pathlib import Path

def check_command(cmd):
    """Check if a command is available"""
    try:
        result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip()
    except FileNotFoundError:
        return False, "Not found"

def find_chromium_src():
    """Try to find Chromium source directory"""
    common_paths = [
        "C:\\chromium\\src",
        "C:\\src\\chromium\\src", 
        "D:\\chromium\\src",
        "C:\\Users\\%USERNAME%\\chromium\\src",
        "C:\\dev\\chromium\\src"
    ]
    
    found_paths = []
    for path in common_paths:
        expanded_path = os.path.expandvars(path)
        if os.path.exists(expanded_path):
            # Check if it's actually a Chromium source directory
            if os.path.exists(os.path.join(expanded_path, "chrome", "browser")):
                found_paths.append(expanded_path)
    
    return found_paths

def check_disk_space():
    """Check available disk space"""
    try:
        import shutil
        total, used, free = shutil.disk_usage("C:\\")
        return {
            'total_gb': total // (1024**3),
            'used_gb': used // (1024**3), 
            'free_gb': free // (1024**3)
        }
    except:
        return None

def main():
    print("🔍 PrivacyAgent VM Setup Checker")
    print("=" * 50)
    
    # Check current directory
    current_dir = Path.cwd()
    print(f"📁 Current directory: {current_dir}")
    
    # Check if we're in PrivacyAgent directory
    if (current_dir / "build" / "build.py").exists():
        print("✅ Found PrivacyAgent build system")
        privacyagent_path = current_dir
    else:
        print("❌ Not in PrivacyAgent directory")
        print("   Please navigate to your PrivacyAgent folder first")
        return
    
    print(f"📁 PrivacyAgent path: {privacyagent_path}")
    
    # Check for Chromium source
    print("\n🔍 Looking for Chromium source...")
    chromium_paths = find_chromium_src()
    if chromium_paths:
        print("✅ Found Chromium source directories:")
        for path in chromium_paths:
            print(f"   📁 {path}")
        recommended_path = chromium_paths[0]
        print(f"🎯 Recommended: {recommended_path}")
    else:
        print("❌ No Chromium source found in common locations")
        print("   You need to set up Chromium first!")
        print("   See CHROMIUM_SETUP_WINDOWS.md for instructions")
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    
    # Python
    python_ok, python_version = check_command("python")
    if python_ok:
        print(f"✅ Python: {python_version}")
    else:
        print("❌ Python not found or not working")
    
    # Git
    git_ok, git_version = check_command("git")
    if git_ok:
        print(f"✅ Git: {git_version}")
    else:
        print("❌ Git not found")
    
    # Check disk space
    print("\n💾 Disk space:")
    disk_info = check_disk_space()
    if disk_info:
        print(f"   Total: {disk_info['total_gb']} GB")
        print(f"   Used:  {disk_info['used_gb']} GB") 
        print(f"   Free:  {disk_info['free_gb']} GB")
        
        if disk_info['free_gb'] < 50:
            print("⚠️  Warning: Less than 50GB free space")
            print("   You may need more space for building")
        else:
            print("✅ Sufficient disk space")
    
    # Check requirements.txt
    requirements_file = privacyagent_path / "requirements.txt"
    if requirements_file.exists():
        print(f"\n📦 Found requirements.txt")
        print("   Run: pip install -r requirements.txt")
    
    # Generate build command
    if chromium_paths:
        print("\n🚀 Ready to build! Use this command:")
        print("=" * 50)
        print(f"cd \"{privacyagent_path}\"")
        print("pip install -r requirements.txt")
        print(f"python build\\build.py --config build\\config\\debug.yaml --chromium-src \"{chromium_paths[0]}\"")
        print("=" * 50)
    else:
        print("\n❌ Cannot generate build command - Chromium source not found")
        print("   Please set up Chromium first using CHROMIUM_SETUP_WINDOWS.md")

if __name__ == "__main__":
    main()