import os
import shutil
from PIL import Image

res = 'android/app/src/main/res'
leg = Image.open('ic_launcher.png').convert('RGBA')
rnd = Image.open('ic_launcher_round.png').convert('RGBA') if os.path.exists('ic_launcher_round.png') else leg
dens = {'mdpi': (48, 108), 'hdpi': (72, 162), 'xhdpi': (96, 216), 'xxhdpi': (144, 324), 'xxxhdpi': (192, 432)}
for d, (s, f) in dens.items():
    p = res + '/mipmap-' + d
    os.makedirs(p, exist_ok=True)
    for w in ('ic_launcher.webp', 'ic_launcher_round.webp', 'ic_launcher_foreground.webp'):
        if os.path.exists(p + '/' + w):
            os.remove(p + '/' + w)
    leg.resize((s, s), Image.LANCZOS).save(p + '/ic_launcher.png')
    rnd.resize((s, s), Image.LANCZOS).save(p + '/ic_launcher_round.png')
    fg = Image.new('RGBA', (f, f), (0, 0, 0, 0))
    n = int(f * 0.60)
    logo = rnd.resize((n, n), Image.LANCZOS)
    fg.paste(logo, ((f - n) // 2, (f - n) // 2), logo)
    fg.save(p + '/ic_launcher_foreground.png')

if os.path.exists('ic_launcher_background.xml'):
    os.makedirs(res + '/values', exist_ok=True)
    shutil.copy('ic_launcher_background.xml', res + '/values/ic_launcher_background.xml')
print('Icons done')
