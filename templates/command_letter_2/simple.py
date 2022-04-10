from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from command_letter_2.builtins import (
        findLookup2, miscLookup2,
        commandObjectLookup2)

LONGEST_KEY = 1


def lookup(key):
    for look in [findLookup2, miscLookup2, commandObjectLookup2]:
        with suppress(KeyError):
            return look(key)


if __name__ == '__main__':
    import json
    dict = {**findLookup2.dictionary.items_str_dict(),
            **miscLookup2.dictionary.items_str_dict(),
            **commandObjectLookup2.dictionary.items_str_dict()}
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)
