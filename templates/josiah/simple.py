from contextlib import suppress
import sys
import os.path
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")

sys.path.append(repository_location)

# import the modules that you want for your vim experience here
# from command_letter.builtins import findLookup, miscLookup
# from command_object.builtins import lookup as command_object_lookup
from command_letter_2.builtins import (
        findLookup2, miscLookup2,
        commandObjectLookup2)

from josiah_modifier.builtins import lookup as josiahLookup

from relative_number.builtins import lookup as relative_number_lookup

LONGEST_KEY = 1


def lookup(key):
    for look in [
            findLookup2,
            miscLookup2,
            commandObjectLookup2,
            relative_number_lookup,
            josiahLookup
            ]:
        with suppress(KeyError):
            return look(key)

if __name__ == "__main__":
    import json
    dict = {**josiahLookup.dictionary.items_str_dict(),
            }
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)
