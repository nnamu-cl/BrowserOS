// PrivacyAgent AI Features Diagnostic Script
// Run this in the browser console to check AI feature availability

console.log('🔍 PrivacyAgent AI Features Diagnostic');
console.log("========================");

// Check for AI extension
if (typeof chrome !== 'undefined' && chrome.runtime) {
    console.log("✅ Chrome extension API available");
    
    // Check for side panel API
    if (chrome.sidePanel) {
        console.log("✅ Side Panel API available");
    } else {
        console.log("❌ Side Panel API not available");
    }
    
    // Check for browserOS API
    if (chrome.browserOS) {
        console.log("✅ BrowserOS API available");
    } else {
        console.log("❌ BrowserOS API not available");
    }
} else {
    console.log("❌ Chrome extension API not available");
}

// Check for AI extension in DOM
const aiElements = document.querySelectorAll('[data-extension-id*="ai"], [data-extension-id*="agent"]');
if (aiElements.length > 0) {
    console.log("✅ AI extension elements found:", aiElements.length);
} else {
    console.log("❌ No AI extension elements found");
}

// Check for side panel
const sidePanels = document.querySelectorAll('[role="complementary"], .side-panel, #side-panel');
if (sidePanels.length > 0) {
    console.log("✅ Side panel elements found:", sidePanels.length);
} else {
    console.log("❌ No side panel elements found");
}

console.log("========================");
console.log("💡 Try pressing Ctrl+E to toggle AI panel");
console.log("💡 Check chrome://extensions/ for 'Agent' extension");
console.log("💡 Look for AI icon in browser toolbar");