#!/usr/bin/env python3
"""
Script to fix all imports from 'permissions' to 'apps.permissions'
"""
import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Patterns to replace
PATTERNS = [
    # Updated mapping: remove legacy apps. prefix
    (r'from apps.permissions\.', 'from permissions.'),
    (r'import apps.permissions\.', 'import permissions.'),
]

# Files to skip
SKIP_DIRS = {'__pycache__', '.git', 'venv', 'env', 'node_modules', 'staticfiles', 'media'}
SKIP_FILES = {'fix_permissions_imports.py'}

def fix_file(file_path):
    """Fix imports in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        modified = False
        
        for pattern, replacement in PATTERNS:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                modified = True
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all Python files"""
    fixed_count = 0
    processed_count = 0
    
    print("Fixing permissions imports...")
    print("-" * 60)
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        
        for file in files:
            if file.endswith('.py') and file not in SKIP_FILES:
                file_path = Path(root) / file
                processed_count += 1
                
                if fix_file(file_path):
                    fixed_count += 1
    
    print("-" * 60)
    print(f"Processed: {processed_count} files")
    print(f"Fixed: {fixed_count} files")
    print("Done!")

if __name__ == '__main__':
    main()
