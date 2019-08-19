import re
from xkeysnail.transform import *

define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.RIGHT_ALT],
    Key.HENKAN: [Key.HENKAN, Key.RIGHT_ALT]
})

define_keymap(None, {
    K("RAlt-h"): K("LEFT"),
    K("RAlt-j"): K("DOWN"),
    K("RAlt-k"): K("UP"),
    K("RAlt-l"): K("RIGHT"),
    K("RAlt-q"): K("C-PAGE_UP"),
    K("RAlt-w"): K("C-PAGE_DOWN"),
    K("RAlt-y"): K("BACKSPACE"),
    K("RAlt-o"): K("DELETE"),
    K("RAlt-n"): K("M-LEFT"),
    K("RAlt-DOT"): K("M-RIGHT"),
    K("RAlt-SPACE"): K("ENTER"),
    K("RAlt-HENKAN"): K("ESC"),
    K("RAlt-MUHENKAN"): K("ESC"),
}, "All")
