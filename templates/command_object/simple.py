from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.command_object.builtins import lookup as commandObjectLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [commandObjectLookup]:
        with suppress(KeyError):
            return look(key)
