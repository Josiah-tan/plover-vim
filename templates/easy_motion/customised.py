from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.easy_motion.builtins import Lookup as EasyMotionLookup

LONGEST_KEY = 2


easy_motion_lookup = EasyMotionLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "escape": "control(j)",  # default: "escape"
    "right_hand": {},  # dict: easymotion finger spelling (right hand)
    "left_hand": {},  # dict: easymotion finger spelling (left hand)
    "systems": [
        {
            "unique_ender": "LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  #
                # "-FP": "",  #
                "-FB": "space space f",  # Forward Back
                # "-PB": "shift(t)",  # Previous Backwards (in command_letter)
                # "-F": "f",  # Forwards (in command_letter)
                # "-P": "t",  # Previous (in command_letter)
                # "-B": "shift(f)",  # Backwards (in command_letter)
                # "": ""  # for normal commands (in command_letter)
                }
            },
        ]})


assert easy_motion_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [easy_motion_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    easy_motion_lookup.generateJson()
