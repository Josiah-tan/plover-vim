from contextlib import suppress
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from josiah_modifier.builtins import Lookup as JosiahModifierLookup


LONGEST_KEY = 1


josiah_modifier_lookup = JosiahModifierLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right hand finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "unique_ender": "-LTZ",
    "prefixes": {
        "#": "control(j)",
        "E": "escape",  # EscapE
        "EU": "control(w)",  # vim splIt
        "U": "control(b)",  # tmUx
        "#E": "control(x)",  # Ex command
        }
    })


assert josiah_modifier_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [josiah_modifier_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    josiah_modifier_lookup.generateJson()
