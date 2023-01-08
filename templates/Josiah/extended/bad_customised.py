from contextlib import suppress


# import the modules that you want for your vim experience here
# from command_letter.builtins import findLookup, miscLookup
# from command_object.builtins import lookup as command_object_lookup
from plover_vim.command_letter_2.builtins import Lookup

from plover_vim.Josiah_modifier.builtins import Lookup as JosiahLookup

from plover_vim.relative_number.builtins import relative_number_lookup as relative_number_lookup

LONGEST_KEY = 1

findLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "#E": "shift(t)",  # "#" to denote go to just before the letter
        "#U": "t",  
        "E": "shift(f)",    # E (because it is more to the left)
        "U": "f",    # U (because it is more to the right)
        },  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "@LG",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",
                # "-FB": "",
                # "-PB": "",
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "<escape> <middles> <objects>",
                # "": ""  # for normal commands (done in josiah-modifers)
                }
            }]
        })


miscLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    # "middles": {},  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "@G",
            "mods": {  # 64 total possibilities from #EURPB
                "-FPB": "<escape> q <objects>",  # liSten
                "-FP": "<escape> shift(at) <objects>",  # @
                # "-FB": "",
                "-PB": "<escape> z <objects>",  # zeN
                "-F": "<escape> g <objects>",  # the good Spot (primeagen youtube video on the g command)
                "-P": "<escape> r <objects>",
                "-B": "<escape> m <objects>",  # set marBg
                "#-B": "<escape> apostrophe <objects>",  # go to marBg
                "#-P": "<escape> <objects> <objects>", # repeat
                "-EFP": "<escape> bracketleft <objects>", # ] 
                "-UFP": "<escape> bracketright <objects>", # [ 
                }
            }]
        })


commandObjectLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "E": "i",  # physically located closer to keyboard centre
        "EU": "O",  # used in Org mode?
        "U": "a",  # physically localed away from the keyboard centre
        "": ""
        },  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "@L",  # ring finger on T, pinky on DZ
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                "-FPB": "<escape> equal <middles> <objects>",
                "-FP": "<escape> y s <middles> <objects>",  # coPy Furround
                "-FB": "<escape> c s <objects>",  # Blot Furround
                "-PB": "<escape> g c <middles> objects>",  # commeNt
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "",

                "#-FPB": "",
                "#-FP": "shift(s) <objects>",
                "#-FB": "<escape> d s <objects>",
                "#-PB": "<escape> g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "",
                "#-B": "",
                "#": ""
                }
            }]
    })

def lookup(key):
    for look in [
            findLookup2,
            miscLookup2,
            commandObjectLookup2,
            relative_number_lookup,
            JosiahLookup(
                {
                    "unique_ender": "@",
                    "prefixes": {
                        "#": "escape"
                        }
                    }
                )
            ]:
        with suppress(KeyError):
            return look(key)

if __name__ == "__main__":
    import json
    import sys
    dict = {**JosiahLookup.dictionary.items_str_dict(),
            }
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)


