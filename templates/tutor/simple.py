from contextlib import suppress


# import the modules that you want for your vim experience here
# from command_letter.builtins import findLookup, miscLookup
# from command_object.builtins import lookup as command_object_lookup
from plover_vim.command_letter_2.builtins import (
        findLookup2, miscLookup2,
        commandObjectLookup2)

from plover_vim.Josiah_modifier.builtins import lookup as JosiahLookup

from plover_vim.relative_number.builtins import relative_number_lookup as relative_number_lookup

LONGEST_KEY = 1


def lookup(key):
    for look in [
            findLookup2,
            miscLookup2,
            commandObjectLookup2,
            relative_number_lookup,
            JosiahLookup
            ]:
        with suppress(KeyError):
            return look(key)

if __name__ == "__main__":
    import json
    import sys
    dict = {**JosiahLookup.dictionary.items_str_dict(),
            }
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)
