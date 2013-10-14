# -*- mode: python -*-
a = Analysis(['src/vaUI.py'],
             pathex=['Z:\\ihme-va'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
for d in a.datas:
  if 'pyconfig' in d[0]:
    a.datas.remove(d)
    break
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('res\\logo.png', 'Z:\\ihme-va\\src\\res\\logo.png', 'DATA')],
          [('res\\about.html', 'Z:\\ihme-va\\src\\res\\about.html', 'DATA')],
          [('res\\documentation.htm', 'Z:\\ihme-va\\src\\res\\documentation.htm', 'DATA')],
          [('res\\documentation_files\\header.htm', 'Z:\\ihme-va\\src\\res\\documentation_files\\header.htm','DATA')],
          [('res\\documentation_files\\item0001.xml', 'Z:\\ihme-va\\src\\res\\documentation_files\\item0001.xml','DATA')],
          [('res\\documentation_files\\props0002.xml', 'Z:\\ihme-va\\src\\res\\documentation_files\\props0002.xml','DATA')],
          [('res\\documentation_files\\themedata.xml', 'Z:\\ihme-va\\src\\res\\documentation_files\\themedata.xml','DATA')],
          [('res\\documentation_files\\image001.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image001.png', 'DATA')],
          [('res\\documentation_files\\image002.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image002.png', 'DATA')],
          [('res\\documentation_files\\image003.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image003.png', 'DATA')],
          [('res\\documentation_files\\image004.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image004.png', 'DATA')],
          [('res\\documentation_files\\image005.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image005.png', 'DATA')],
          [('res\\documentation_files\\image006.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image006.png', 'DATA')],
          [('res\\documentation_files\\image007.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image007.png', 'DATA')],
          [('res\\documentation_files\\image008.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image008.png', 'DATA')],
          [('res\\documentation_files\\image009.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image009.png', 'DATA')],
          [('res\\documentation_files\\image010.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image010.png', 'DATA')],
          [('res\\documentation_files\\image011.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image011.png', 'DATA')],
          [('res\\documentation_files\\image012.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image012.png', 'DATA')],
          [('res\\documentation_files\\image013.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image013.png', 'DATA')],
          [('res\\documentation_files\\image014.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image014.png', 'DATA')],
          [('res\\documentation_files\\image015.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image015.png', 'DATA')],
          [('res\\documentation_files\\image016.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image016.png', 'DATA')],
          [('res\\documentation_files\\image017.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image017.png', 'DATA')],
          [('res\\documentation_files\\image018.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image018.png', 'DATA')],
          [('res\\documentation_files\\image019.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image019.png', 'DATA')],
          [('res\\documentation_files\\image020.png', 'Z:\\ihme-va\\src\\res\\documentation_files\\image020.png', 'DATA')],
          [('tariffs-adult.csv', 'Z:\\ihme-va\\src\\tariffs-adult.csv', 'DATA')],
          [('tariffs-child.csv', 'Z:\\ihme-va\\src\\tariffs-child.csv', 'DATA')],
          [('tariffs-neonate.csv', 'Z:\\ihme-va\\src\\tariffs-neonate.csv', 'DATA')],
          [('validated-adult.csv', 'Z:\\ihme-va\\src\\validated-adult.csv', 'DATA')],
          [('validated-child.csv', 'Z:\\ihme-va\\src\\validated-child.csv', 'DATA')],
          [('validated-neonate.csv', 'Z:\\ihme-va\\src\\validated-neonate.csv', 'DATA')],
          [('adult_undetermined_weights-hce0.csv', 'Z:\\ihme-va\\src\\adult_undetermined_weights-hce0.csv', 'DATA')],
          [('adult_undetermined_weights-hce1.csv', 'Z:\\ihme-va\\src\\adult_undetermined_weights-hce1.csv', 'DATA')],
          [('child_undetermined_weights-hce0.csv', 'Z:\\ihme-va\\src\\child_undetermined_weights-hce0.csv', 'DATA')],
          [('child_undetermined_weights-hce1.csv', 'Z:\\ihme-va\\src\\child_undetermined_weights-hce1.csv', 'DATA')],
          [('neonate_undetermined_weights-hce0.csv', 'Z:\\ihme-va\\src\\neonate_undetermined_weights-hce0.csv', 'DATA')],
          [('neonate_undetermined_weights-hce1.csv', 'Z:\\ihme-va\\src\\neonate_undetermined_weights-hce1.csv', 'DATA')],
          name='SmartVA.exe',
          debug=False,
          strip=None,
          upx=False,
          console=False,icon='pkg\\icon.ico')