# PrivacyAgent AI Features Guide

## 🤖 How to Access AI in PrivacyAgent

### Quick Access Methods:
1. **Keyboard Shortcut**: Press `Ctrl+E` (Windows) or `Cmd+E` (Mac)
2. **Toolbar Icon**: Look for the "Agent" extension icon in the browser toolbar
3. **Side Panel**: Check the side panel menu (usually on the right side)

### What the AI Can Do:
- **Chat with AI**: Ask questions and get responses
- **Page Analysis**: Analyze current webpage content
- **DOM Interaction**: Interact with page elements
- **Content Extraction**: Extract and process page information

## 🔍 Troubleshooting: AI Not Visible

### Check 1: Extension Status
1. Go to `chrome://extensions/` in the address bar
2. Look for "Agent" extension (should be enabled)
3. Check if it's listed as a "Component Extension"

### Check 2: Side Panel
1. Look for a side panel toggle button in the browser toolbar
2. Try right-clicking in the toolbar area
3. Check browser settings for side panel options

### Check 3: Keyboard Shortcut
1. Press `Ctrl+E` multiple times
2. Check if anything appears on the right side
3. Try `F12` to open DevTools and look for console errors

## 🚀 Expected AI Interface

When working correctly, you should see:
- **Side Panel**: A dark-themed panel on the right side
- **Chat Interface**: Text input area for AI conversations
- **Page Context**: AI awareness of current webpage
- **Interactive Elements**: Buttons and controls for AI features

## 🔧 Development Notes

The AI extension includes:
- **Background Script**: `background.js` (handles AI logic)
- **Content Scripts**: `content.js`, `buildDomTree.js` (page interaction)
- **Side Panel**: `sidepanel.html` (main AI interface)
- **Permissions**: Full page access, storage, tabs, debugging

## 📝 If AI Still Not Working

The AI features require:
1. **Proper Build**: Extension must be compiled correctly
2. **Chromium Source**: Full build with all patches applied
3. **Component Registration**: Extension must be registered as component
4. **Side Panel Support**: Browser must support side panel API

If you're using a pre-built version and AI isn't working, the build might be incomplete or the AI features might need additional setup.