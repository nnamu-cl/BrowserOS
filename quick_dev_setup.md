# Quick Development Setup for PrivacyAgent

## ⚡ Fast Track: Get PrivacyAgent Running in 10 Minutes

## What you can do without Chromium source:
1. Study the patch files to understand modifications
2. Modify existing patches
3. Create new patches
4. Update resources (icons, extensions)
5. Modify build scripts

## Key areas to explore:

### 1. Patches (Main customizations)
- Location: `patches/nxtscape/`
- These modify Chromium's behavior
- Each .patch file shows exactly what changes

### 2. AI Extensions
- Location: `resources/files/ai_side_panel/`
- Browser extensions that add AI functionality

### 3. Build System
- Location: `build/`
- Python scripts that orchestrate the build

## Learning workflow:
1. Read patches to understand what's changed from Chromium
2. Examine the AI extensions
3. Study the build system
4. Make small modifications to patches
5. When ready for full development, set up Chromium source

## Testing patches:
You can validate patch syntax and understand changes without building:
```bash
# View what a patch does
git apply --stat patches/nxtscape/ai-chat-extension.patch

# Check if patch is valid
git apply --check patches/nxtscape/ai-chat-extension.patch
```