# Hands-On Patch Tutorial: Create Your First PrivacyAgent Modification

## 🎯 Goal: Change the Browser Name from "PrivacyAgent" to "MyCustomBrowser"

This tutorial will walk you through creating your first patch step-by-step.

## 📋 What You'll Learn
- How to read and understand patch files
- How to modify existing patches
- How to test your changes
- How patches integrate with the build system

## 🔍 Step 1: Understand the Current Branding Patch

Let's examine how BrowserOS currently changes "Chromium" to "BrowserOS":

### Current Patch: `patches/nxtscape/branding.patch`

```diff
# This line shows what the original Chromium code looked like:
-            Chromium

# This line shows what BrowserOS changed it to:
+            BrowserOS
```

**What this means:**
- The `-` line is **removed** from the original file
- The `+` line is **added** to the file
- During build, "Chromium" becomes "BrowserOS"

## 🛠️ Step 2: Create Your Custom Patch

### Option A: Modify Existing Patch (Easiest)

1. **Open the branding patch file:**
   ```
   patches/nxtscape/branding.patch
   ```

2. **Find all instances of "BrowserOS" and change them:**
   ```diff
   # Change this:
   +            BrowserOS
   
   # To this:
   +            MyCustomBrowser
   ```

3. **Save the file**

### Option B: Create New Patch (More Advanced)

1. **Create a new patch file:**
   ```
   patches/nxtscape/my-custom-branding.patch
   ```

2. **Add it to the series file:**
   ```
   # Add this line to patches/series
   nxtscape/my-custom-branding.patch
   ```

## 📝 Step 3: Understanding Patch Syntax

### Basic Patch Structure:
```diff
From [commit-hash] Mon Sep 17 00:00:00 2001
From: Your Name <your.email@example.com>
Date: [date]
Subject: [PATCH] Brief description

---
 path/to/file.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/path/to/file.txt b/path/to/file.txt
index [old-hash]..[new-hash] 100644
--- a/path/to/file.txt
+++ b/path/to/file.txt
@@ -line-number,lines-affected +line-number,lines-affected @@
 context line (unchanged)
-old line (removed)
+new line (added)
 context line (unchanged)
```

### Key Elements:
- **Header**: Metadata about the patch
- **File path**: Which file is being modified
- **Line numbers**: `@@ -old +new @@` shows where changes occur
- **Context**: Unchanged lines around the modification
- **Changes**: `-` for removed, `+` for added lines

## 🎨 Step 4: Common Modification Patterns

### Pattern 1: Simple Text Replacement
```diff
# Change displayed text
-  "Welcome to BrowserOS"
+  "Welcome to MyCustomBrowser"
```

### Pattern 2: Change Configuration Values
```diff
# Change default settings
-  default_homepage = "https://browseros.com";
+  default_homepage = "https://mycustombrowser.com";
```

### Pattern 3: Add New Code
```diff
   existing_function();
+  // My custom feature
+  my_custom_function();
   more_existing_code();
```

### Pattern 4: Remove/Disable Features
```diff
-  if (show_unwanted_feature) {
-    display_feature();
-  }
+  // Disabled unwanted feature in MyCustomBrowser
+  // if (show_unwanted_feature) {
+  //   display_feature();
+  // }
```

## 🧪 Step 5: Test Your Patch

### Method 1: Quick Syntax Check
```bash
# Navigate to BrowserOS directory
cd "C:\Users\emcal\OneDrive\Desktop\BrowserOS"

# Check if your patch syntax is valid
git apply --check patches/nxtscape/branding.patch
```

### Method 2: Apply Patch Manually (Advanced)
```bash
# If you have Chromium source, test applying the patch
cd "C:\chromium\src"
git apply "C:\Users\emcal\OneDrive\Desktop\BrowserOS\patches\nxtscape\branding.patch"

# Check what changed
git diff

# Undo the patch
git apply -R "C:\Users\emcal\OneDrive\Desktop\BrowserOS\patches\nxtscape\branding.patch"
```

### Method 3: Full Build Test
```bash
# Build with your modified patch
python build\build.py --config build\config\debug.yaml --chromium-src "C:\chromium\src"
```

## 🔍 Step 6: Understanding Real BrowserOS Patches

### 1. **Branding Patch** (Simple)
**Purpose:** Changes all "Chromium" text to "BrowserOS"
**Files affected:** String resources, branding files
**Complexity:** ⭐ (Beginner)

### 2. **AI Chat Extension Patch** (Medium)
**Purpose:** Adds the AI side panel extension
**Files affected:** Extension system, build files
**Complexity:** ⭐⭐⭐ (Intermediate)

### 3. **BrowserOS API Patch** (Complex)
**Purpose:** Adds completely new browser APIs
**Files affected:** Extension APIs, permissions, build system
**Complexity:** ⭐⭐⭐⭐⭐ (Advanced)

## 🎯 Practical Exercises

### Exercise 1: Change Welcome Message
**Goal:** Modify the first-run welcome text

1. **Find:** Look for "Welcome to BrowserOS" in patches
2. **Modify:** Change to your custom message
3. **Test:** Build and check first-run experience

### Exercise 2: Add Custom Homepage
**Goal:** Set a default homepage for your browser

1. **Research:** Find where default homepage is set
2. **Create patch:** Add your custom URL
3. **Verify:** New installations use your homepage

### Exercise 3: Disable Feature
**Goal:** Remove the downloads bar

1. **Locate:** Find downloads bar code
2. **Disable:** Comment out or return early
3. **Test:** Verify downloads bar doesn't appear

## 🚀 Advanced Patch Techniques

### Conditional Patches
```diff
+#if defined(MY_CUSTOM_BROWSER)
+  // Custom behavior only in my browser
+  custom_function();
+#else
   // Original Chromium behavior
   original_function();
+#endif
```

### Multi-File Patches
```diff
# One patch can modify multiple files
diff --git a/file1.cc b/file1.cc
[changes to file1]

diff --git a/file2.h b/file2.h
[changes to file2]
```

### Build System Integration
```diff
# Add new files to build
+    "my_custom_file.cc",
+    "my_custom_file.h",
```

## 🔧 Troubleshooting Common Issues

### Issue 1: Patch Doesn't Apply
**Cause:** Line numbers or context changed
**Solution:** Update the patch to match current Chromium

### Issue 2: Build Fails After Patch
**Cause:** Syntax error or missing dependencies
**Solution:** Check compiler errors, fix syntax

### Issue 3: Feature Doesn't Work
**Cause:** Incomplete modification
**Solution:** Ensure all related code is patched

## 📚 Next Steps

1. **Start Simple:** Modify existing patches first
2. **Study Examples:** Look at all patches in `patches/nxtscape/`
3. **Experiment:** Try small modifications
4. **Learn Git:** Understanding Git helps with patch creation
5. **Read Chromium Docs:** Learn about Chromium architecture

## 🎯 Key Takeaways

- **Patches are powerful:** Small changes can have big effects
- **Start simple:** Text changes are easiest to understand
- **Test thoroughly:** Always verify your modifications work
- **Study existing patches:** Learn from what's already there
- **Be patient:** Complex modifications take time to understand

---

**Remember:** Patches are the key to customizing Chromium without maintaining a full fork. Master patches, and you can create your own custom browser with any features you want!