from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.command_letter.builtins import findLookup, miscLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [findLookup, miscLookup]:
        with suppress(KeyError):
            return look(key)
