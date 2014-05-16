from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.utils import platform

def add_path(*paths):
    for p in reversed(paths):
        resource_add_path(p)

def set_regular(family, *filenames):
    for f in filenames:
        try:
            LabelBase.register(family, f)
            break
        except IOError:
            continue
    else:
        raise IOError, 'No appropriate fonts for Kivy UI'

_platform = platform()
if _platform is 'android':
    add_path('/system/fonts', '/data/fonts')
    set_regular(DEFAULT_FONT,
        'DroidSansJapanese.ttf',
        'MTLmr3m.ttf',
        'MTLc3m.ttf',
        'DroidSansFallback.ttf',
    )

elif _platform is 'ios':
    add_path('/Library/Fonts')
    set_regular(DEFAULT_FONT,
        'Osaka.ttf',
        'OsakaMono.ttf',
    )

elif _platform is 'linux':
    add_path('/usr/share/fonts/truetype/ipafont', '/usr/local/share/font-ipa')
    set_regular(DEFAULT_FONT,
        'ipagp.ttf', # IPAfont (http://ipafont.ipa.go.jp/)
        'ipagp.otf', # IPAfont (http://ipafont.ipa.go.jp/)
    )

elif _platform is 'macosx':
    add_path('/Library/Fonts', '/System/Library/Fonts')
    set_regular(DEFAULT_FONT,
        'Hiragino Sans GB W3.otf',
        'Osaka.ttf',
        'OsakaMono.ttf',
        'AppleGothic.ttf',
    )

elif _platform is 'win':
    add_path('c:/Windows/Fonts')
    set_regular(DEFAULT_FONT,
        'VL-Gothic-Regular.ttf', # ProjectVine (http://vlgothic.dicey.org/)
        'meiryo001.ttf',         # separated from meiryo.ttc with unitettc.exe
        'msgothic001.ttf',       # separated from msgothic.ttc with unitettc.exe
        'ipagp.ttf',             # IPAfont (http://ipafont.ipa.go.jp/)
    )

else:
    raise IOError, 'Unknown platform: %s' % _platform