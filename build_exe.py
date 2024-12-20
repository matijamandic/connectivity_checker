import os
from PyQt6.QtWidgets import QApplication
import sys
from src.ui.icons import create_app_icon  # Updated import path
from PyQt6.QtGui import QIcon

# Initialize QApplication first
app = QApplication(sys.argv)

# Create and save the icon
pixmap = create_app_icon()
pixmap.save("app_icon.png")

# Convert PNG to ICO (requires pillow)
from PIL import Image
img = Image.open("app_icon.png")
img.save("app_icon.ico")

# Clean up PNG
os.remove("app_icon.png")

# Create a spec file if it doesn't exist
spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/main.py'],  # Updated path to main.py
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NetworkMonitor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app_icon.ico'  # Add icon to the executable
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NetworkMonitor'
)
"""

# Write the spec file
with open("build.spec", "w") as f:
    f.write(spec_content)

# Run PyInstaller
os.system("pyinstaller build.spec")