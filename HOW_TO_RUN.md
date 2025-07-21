# How to Run PrivacyAgent - Complete Guide

## 🚀 Quick Start Options

### Option 1: Pre-built Version (Recommended for Users)
1. **Download**: Visit https://bit.ly/browseros-windows
2. **Install**: Run the installer like any Windows application
3. **Launch**: Start PrivacyAgent from Start Menu or Desktop
4. **Access AI**: Press `Ctrl+E` to open AI side panel

### Option 2: Build from Source (For Developers)

## 📋 Prerequisites for Building

### Required Software:
- **Windows 10/11** (64-bit)
- **Python 3.8+** with pip
- **Git for Windows**
- **Visual Studio 2022** (Community Edition with C++ workload)
- **~100GB free disk space** (for Chromium source)
- **16GB+ RAM** (recommended for building)

### Check Prerequisites:
```powershell
# Check Python
python --version

# Check Git
git --version

# Check available disk space
Get-WmiObject -Class Win32_LogicalDisk | Select-Object DeviceID, @{Name="Size(GB)";Expression={[math]::Round($_.Size/1GB,2)}}, @{Name="FreeSpace(GB)";Expression={[math]::Round($_.FreeSpace/1GB,2)}}
```

## 🔧 Build Process

### Step 1: Install Python Dependencies
```powershell
cd "C:\Users\emcal\OneDrive\Desktop\PrivacyAgent"
pip install -r requirements.txt
```

### Step 2: Set Up Chromium Source (First Time Only)
```powershell
# This takes 4-8 hours and ~100GB
# Follow the detailed guide in CHROMIUM_SETUP_WINDOWS.md

# Quick version:
mkdir C:\chromium
cd C:\chromium
# Download depot_tools and set up Chromium (see full guide)
```

### Step 3: Build PrivacyAgent

cd "C:\Users\emcal\OneDrive\Desktop\PrivacyAgent"

# Debug build (faster, for development)
python build\build.py --config build\config\debug.yaml --chromium-src "C:\chromium\src"

# Release build (optimized, for production)
python build\build.py --config build\config\release_windows.yaml --chromium-src "C:\chromium\src"
```

### Step 4: Run Built Version
```powershell
# After successful build, the executable will be in:
# C:\chromium\src\out\Default\chrome.exe (debug)
# or
# C:\chromium\src\out\Release\chrome.exe (release)

# Run with development flags:
C:\chromium\src\out\Default\chrome.exe --enable-logging --v=1
```

## ⚡ Quick Development Workflow

### For Code Changes:
```powershell
# 1. Make changes to patches or resources
# 2. Rebuild (incremental, faster)
python build\build.py --config build\config\debug.yaml --chromium-src "C:\chromium\src"

# 3. Test changes
C:\chromium\src\out\Default\chrome.exe
```

### For Resource-Only Changes:
```powershell
# If you only changed files in resources/ folder:
python build\build.py --config build\config\copy_resources.yaml --chromium-src "C:\chromium\src"
```

## 🎯 Build Times (Approximate)

| Build Type | First Time | Incremental |
|------------|------------|-------------|
| Debug | 2-4 hours | 30-60 min |
| Release | 3-6 hours | 45-90 min |
| Resources Only | 5-10 min | 2-5 min |

## 🔍 Troubleshooting

### Common Issues:

1. **"Chromium source not found"**
   - Make sure you've downloaded Chromium source
   - Check the path in your command

2. **"Build failed"**
   - Check you have Visual Studio 2022 with C++ workload
   - Ensure you have enough disk space and RAM

3. **"Python dependencies missing"**
   - Run: `pip install -r requirements.txt`

4. **"AI features not working"**
   - Make sure you built with all patches applied
   - Check that extensions are enabled in chrome://extensions/

### Build Logs:
- Check build output for specific error messages
- Look in `C:\chromium\src\out\Default\` for build artifacts

## 🚀 Running Different Configurations

### Development Mode:
```powershell
# With debugging enabled
chrome.exe --enable-logging --v=1 --disable-web-security --user-data-dir="C:\temp\chrome-dev"
```

### Testing Mode:
```powershell
# With fresh profile
chrome.exe --user-data-dir="C:\temp\chrome-test"
```

### AI Development:
```powershell
# With extension debugging
chrome.exe --enable-logging --v=1 --load-extension="path\to\ai_side_panel"
```

## 📚 Next Steps

After running PrivacyAgent:
1. **Test AI Features**: Press `Ctrl+E` to open AI panel
2. **Check Extensions**: Go to `chrome://extensions/`
3. **Explore Settings**: Look for PrivacyAgent-specific settings
4. **Read Documentation**: Check the guides in this repository

## 🔗 Useful Links

- **Build Guide**: See `BUILD.md` for detailed build instructions
- **Learning Guide**: See `LEARNING_GUIDE.md` for development tips
- **AI Features**: See `AI_FEATURES_GUIDE.md` for AI functionality
- **Chromium Setup**: See `CHROMIUM_SETUP_WINDOWS.md` for detailed setup