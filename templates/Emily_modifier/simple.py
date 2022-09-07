from contextlib import suppress
# import the modules that you want for your vim experience here
from plover_vim.Emily_modifier.builtins import EmilyLookup, escapedLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [EmilyLookup, escapedLookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    EmilyLookup.generateJson()
    # escapedLookup.generateJson()
