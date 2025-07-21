# PrivacyAgent Development Guide

## 🚀 Getting Started with PrivacyAgent Development
```bash
# 1. Validate patches before building
python scripts/validate_patches.py

# 2. Build PrivacyAgent
python build/build.py --config config/privacyagent.yaml

# 3. Run tests
python scripts/run_tests.py --suite integration
```

## Patch Development Guidelines

### 1. **Naming Convention**
- Use descriptive names: `feature-ai-chat-extension.patch`
- Include scope: `ui-settings-privacy-panel.patch`
- Version if needed: `branding-v2.patch`

### 2. **Patch Structure**
```
From: Developer Name <email@domain.com>
Date: Mon, 1 Jan 2025 12:00:00 +0000
Subject: [PATCH] Brief description of changes

Detailed description of what this patch does,
why it's needed, and any side effects.

Fixes: #issue-number
---
 file1.cc | 10 +++++++---
 file2.h  |  5 +++++
 2 files changed, 12 insertions(+), 3 deletions(-)
```

### 3. **Best Practices**
- ✅ One logical change per patch
- ✅ Include tests when adding features
- ✅ Update documentation for user-facing changes
- ✅ Use consistent branding terms
- ❌ Don't mix unrelated changes
- ❌ Don't include debugging code
- ❌ Don't hardcode paths or URLs

### 4. **Testing Your Patches**
```bash
# Syntax validation
python scripts/validate_patches.py

# Build test
python build/build.py --test-only

# Integration test
python scripts/run_tests.py --patch-specific
```

## Common Patch Patterns

### Adding New Features
1. Update `BUILD.gn` files
2. Add source files
3. Update resource files
4. Add to component loader
5. Update allowlists if needed

### Branding Changes
1. Update string resources
2. Modify build configuration
3. Update icons and assets
4. Change bundle identifiers
5. Update copyright notices

### UI Modifications
1. Update HTML templates
2. Modify CSS styles
3. Update JavaScript handlers
4. Add new resources
5. Update manifest files

## Troubleshooting

### Common Issues
- **Missing braces**: Use the validation script
- **Build failures**: Check patch order in `series` file
- **Resource conflicts**: Ensure unique resource IDs
- **Branding inconsistency**: Use centralized config

### Debug Commands
```bash
# Check patch application
git apply --check patches/nxtscape/*.patch

# Validate specific patch
python scripts/validate_patches.py --file branding.patch

# Build with verbose output
python build/build.py --verbose --config config/privacyagent.yaml
```

## Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Develop** your patch following guidelines
4. **Test** thoroughly using provided scripts
5. **Submit** a pull request with detailed description

## Resources

- [Chromium Development Guide](https://chromium.googlesource.com/chromium/src/+/main/docs/README.md)
- [Patch Format Documentation](https://git-scm.com/docs/git-format-patch)
- [BrowserOS Architecture](./ARCHITECTURE.md)