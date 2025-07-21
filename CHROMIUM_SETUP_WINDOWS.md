# Chromium Setup for PrivacyAgent Development on Windows

## ⚠️ Requirements
- ~100GB free disk space
- Fast internet (multi-hour download)
- Windows 10/11
- Visual Studio 2022 (Community Edition)
- Git for Windows

## 📥 Step 1: Install Prerequisites

### Install Visual Studio 2022
1. Download Visual Studio 2022 Community
2. Install with "Desktop development with C++" workload
3. Include Windows 10/11 SDK

### Install depot_tools
```powershell
# Download depot_tools
Invoke-WebRequest -Uri "https://storage.googleapis.com/chrome-infra/depot_tools.zip" -OutFile "depot_tools.zip"
Expand-Archive -Path "depot_tools.zip" -DestinationPath "C:\depot_tools"

# Add to PATH (run as Administrator)
$env:PATH = "C:\depot_tools;" + $env:PATH
[Environment]::SetEnvironmentVariable("PATH", $env:PATH, [EnvironmentVariableTarget]::Machine)
```

## 📦 Step 2: Download Chromium Source

```powershell
# Create chromium directory (choose drive with most space)
mkdir C:\chromium
cd C:\chromium

# Set environment variables
$env:DEPOT_TOOLS_WIN_TOOLCHAIN = "0"
$env:vs2022_install = "C:\Program Files\Microsoft Visual Studio\2022\Community"

# Fetch Chromium (this takes HOURS - be patient!)
gclient config --name src https://chromium.googlesource.com/chromium/src.git
gclient sync
```

## 🔧 Step 3: Build BrowserOS

Once Chromium is downloaded:

```powershell
cd "C:\Users\emcal\OneDrive\Desktop\BrowserOS"

# Install Python dependencies
pip install -r requirements.txt

# Build debug version
python build\build.py --config build\config\debug.yaml --chromium-src "C:\chromium\src"
```

## ⏱️ Expected Timeline
- Chromium download: 4-8 hours (depending on internet)
- First build: 2-4 hours (depending on hardware)
- Subsequent builds: 30-60 minutes

## 🎯 Alternative: Use Existing Chromium
If you already have Chromium source somewhere, just point to it:
```powershell
python build\build.py --config build\config\debug.yaml --chromium-src "path\to\your\chromium\src"
```