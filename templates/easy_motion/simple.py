from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.easy_motion.builtins import lookup as findLetterLookup

LONGEST_KEY = 2


def lookup(key):
    for look in [findLetterLookup]:
        with suppress(KeyError):
            return look(key)
