# PrivacyAgent Development Learning Path
# Start here without needing Chromium source

## 🎯 What You Can Learn Right Now

### 1. Understanding the AI Features
The main AI functionality comes from:
- **AI Side Panel Extension**: `resources/files/ai_side_panel/`
- **Patches**: `patches/nxtscape/` - These modify Chromium behavior
- **Custom APIs**: Added through patches like `privacyagent-API.patch`

### 2. Key Files to Study

#### AI Extension Structure:
- `manifest.json` - Extension configuration
- `sidepanel.html` - AI chat interface
- `background.js` - Extension background logic (compiled)
- `content.js` - Page interaction script (compiled)
- `buildDomTree.js` - DOM analysis for AI

#### Important Patches:
- `ai-chat-extension.patch` - Adds AI extension to Chromium
- `browserOS-API.patch` - Custom browser APIs
- `nxtscape-settings-ui.patch` - Settings interface
- `branding.patch` - Visual customization

### 3. Learning Exercises

#### Exercise 1: Understand Patch System
```bash
# View what each patch does
git apply --stat patches/nxtscape/ai-chat-extension.patch
git apply --stat patches/nxtscape/branding.patch
```

#### Exercise 2: Modify AI Extension
1. Edit `resources/files/ai_side_panel/manifest.json`
2. Change the keyboard shortcut from Ctrl+E to Ctrl+Shift+A
3. Update the description

#### Exercise 3: Create a New Patch
1. Study existing patches in `patches/nxtscape/`
2. Create a simple UI modification patch
3. Add it to the build system

### 4. Development Workflow (Without Full Build)
1. **Study patches** - Understand what changes from Chromium
2. **Modify resources** - Update AI extensions, icons, etc.
3. **Test with pre-built** - Download BrowserOS to see current features
4. **Plan modifications** - Design your changes
5. **Set up Chromium** - When ready for full development

## 🚀 Next Steps
1. Download pre-built BrowserOS to understand current features
2. Study the patch files to understand modifications
3. Experiment with AI extension modifications
4. Set up Chromium source when ready for full development