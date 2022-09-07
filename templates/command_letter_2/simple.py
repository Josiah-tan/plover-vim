from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.command_letter_2.builtins import (
        findLookup2, miscLookup2,
        commandObjectLookup2)

LONGEST_KEY = 1


def lookup(key):
    for look in [findLookup2, miscLookup2, commandObjectLookup2]:
        with suppress(KeyError):
            return look(key)


if __name__ == '__main__':
    import json
    import sys
    dict = {**findLookup2.dictionary.items_str_dict(),
            **miscLookup2.dictionary.items_str_dict(),
            **commandObjectLookup2.dictionary.items_str_dict()}
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)
