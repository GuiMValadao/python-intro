from PyInstaller.utils.hooks import collect_data_files
import os

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('images', 'images'),
        ('sounds', 'sounds'),
        ('saves',  'saves'),   # remove if saves dir doesn't exist yet
    ],
    hiddenimports=['numpy', 'pygame'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='MusicGame',
    debug=False,
    strip=False,
    upx=True,
    console=False,   # set True temporarily if you need to see crash output
    icon=None,       # replace with 'images/icon.ico' if you have one
)