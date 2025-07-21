# Chromium Source Setup Guide for PrivacyAgent

## Prerequisites
- ~100GB free disk space
- Fast internet connection (download will take hours)
- Git for Windows
- Visual Studio 2022 (Community Edition is fine)

## Step 1: Install depot_tools
1. Download depot_tools: https://storage.googleapis.com/chrome-infra/depot_tools.zip
2. Extract to `C:\depot_tools`
3. Add `C:\depot_tools` to your PATH environment variable
4. Open Command Prompt and run: `gclient`

## Step 2: Set up Chromium
```cmd
# Create a directory for Chromium (choose a drive with lots of space)
mkdir C:\chromium
cd C:\chromium

# Fetch Chromium source (this will take several hours)
fetch chromium

# This creates C:\chromium\src - this is your chromium source path
```

## Step 3: Use with BrowserOS
Once you have Chromium source at `C:\chromium\src`, you can build BrowserOS:

```powershell
cd "C:\Users\emcal\OneDrive\Desktop\BrowserOS"
python build\build.py --config build\config\debug.yaml --chromium-src "C:\chromium\src"
```

## Alternative: Use existing Chromium if you have it
If you already have Chromium source somewhere, just point to that directory.