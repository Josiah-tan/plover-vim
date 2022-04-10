from contextlib import suppress
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from emily_modifier.builtins import Lookup as EmilyModifierLookup


LONGEST_KEY = 1


emily_modifier_lookup = EmilyModifierLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "escape": "control(j)",  # default: "escape"
    "unique_ender": "#-LTZ",
    })


assert emily_modifier_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [emily_modifier_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    emily_modifier_lookup.generateJson()
