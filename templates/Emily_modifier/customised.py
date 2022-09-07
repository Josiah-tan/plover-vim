from contextlib import suppress
# import the modules that you want for your vim experience here
from plover_vim.Emily_modifier.builtins import Lookup as EmilyModifierLookup


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
