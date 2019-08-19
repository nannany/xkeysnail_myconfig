import re
from xkeysnail.transform import *

define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.RIGHT_ALT],
    Key.HENKAN: [Key.HENKAN, Key.RIGHT_ALT]
})

define_keymap(None, {
    # vim like上下左右
    K("RAlt-h"): K("LEFT"),
    K("RAlt-j"): K("DOWN"),
    K("RAlt-k"): K("UP"),
    K("RAlt-l"): K("RIGHT"),
    # ページup&down
    K("RAlt-q"): K("C-PAGE_UP"),
    K("RAlt-w"): K("C-PAGE_DOWN"),
    # backspace&delete
    K("RAlt-y"): K("BACKSPACE"),
    K("RAlt-o"): K("DELETE"),
    # ページ戻る、次へ
    K("RAlt-n"): K("M-LEFT"),
    K("RAlt-DOT"): K("M-RIGHT"),
    # その他よく使う系
    K("RAlt-a"): K("C-a"),
    K("RAlt-c"): K("C-INSERT"),
    K("RAlt-s"): K("C-s"),
    K("RAlt-v"): K("C-v"),
    K("RAlt-z"): K("C-z"),
    K("RAlt-SPACE"): K("ENTER"),
    K("RAlt-HENKAN"): K("ESC"),
    K("RAlt-MUHENKAN"): K("ESC"),
}, "All")
