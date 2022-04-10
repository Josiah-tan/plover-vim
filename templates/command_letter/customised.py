from contextlib import suppress
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from command_letter.builtins import Lookup as CommandLetterLookup

LONGEST_KEY = 1


command_letter_lookup = CommandLetterLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",  #
                # "-FB": "space space f",  # Forward Back (moving this to another module)
                "-PB": "shift(t)",  # Previous Backwards
                "-F": "f",  # Forwards
                "-P": "t",  # Previous
                "-B": "shift(f)",  # Backwards
                "": ""  # for normal commands
                }
            },
        {
            "unique_ender": "-TZ",
            "mods": {
                "-FPB": "q",  # liSten
                "-FP": "shift(at)",  # @
                # "-FB": "",
                "-PB": "z",  # zeN
                "-F": "g",  # the good Spot (primeagen youtube video on the g command)
                "-P": "r",
                "-B": "m"
                }
            }]
        })


assert command_letter_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [command_letter_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    command_letter_lookup.generateJson()
