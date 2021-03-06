from contextlib import suppress
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from easy_motion.builtins import Lookup as EasyMotionLookup
from josiah_modifier.defaults import spelling

LONGEST_KEY = 2

easy_motion_lookup = EasyMotionLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": spelling,  # dict: right handed only finger spelling
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
                # "-FP": "",  # CHrome
                "-FB": "space space f",  # Forward Back
                # "-PB": "shift(t)",  # Previous Backwards (in command_letter)
                # "-F": "f",  # Forwards (in command_letter)
                # "-P": "t",  # Previous (in command_letter)
                # "-B": "shift(f)",  # Backwards (in command_letter)
                # "": ""  # for normal commands (in command_letter)
                }
            },
        ]})


chrome_lookup = EasyMotionLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {"TP": "f"},  # dict: right handed only finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "escape": "escape",  # default: "escape"
    "right_hand": {},  # dict: easymotion finger spelling (right hand)
    "left_hand": {},  # dict: easymotion finger spelling (left hand)
    "systems": [
        {
            "unique_ender": "LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  #
                "-FP": "",  # CHrome (vimium)
                # "-FB": "space space f",  # Forward Back
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
    for look in [
            easy_motion_lookup,
            chrome_lookup,
            ]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    # easy_motion_lookup.generateJson()
    # chrome_lookup.generateJson()
    import json
    dict = {**chrome_lookup.dictionary.items_str_dict(),
            }
    with open("templates/josiah/easy_motion.json", "w") as f:
        json.dump(dict, f, ensure_ascii=False, indent=0)
