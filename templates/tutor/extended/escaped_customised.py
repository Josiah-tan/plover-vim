from contextlib import suppress


# import the modules that you want for your vim experience here
# from command_letter.builtins import findLookup, miscLookup
# from command_object.builtins import lookup as command_object_lookup
from plover_vim.command_letter_2.builtins import Lookup

from plover_vim.Josiah_modifier.builtins import Lookup as JosiahLookup

from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
from plover_vim.relative_number.util import reverse, double, up, down, addWhitespace

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

# relative_number_lookup = OldRelativeNumberLookup()
relative_number_lookup = RelativeNumberLookup({
    "disable_defaults": True,
    "numbers": { 'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '0', '-F': '6', '-P': '7', '-L': '8', '-T': '9', },
    "systems": {
        "reverse": {
            "stroke": "-EU",
            "callback": reverse,
            "min_number": 10,
            "dependencies": []
            },
        "double": {
            "stroke": "-EU",
            "callback": double,
            "min_number": 1,
            "max_number": 9,
            "dependencies": []
            },
        "up": {
            "stroke": "-B",
            "callback": up,
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "down": {
            "stroke": "-R",
            "callback": down,
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_yank": {
            "stroke": "K-B",
            "callback": lambda x: f"{{#escape y {addWhitespace(x)} k}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_yank": {
            "stroke": "K-R",
            "callback": lambda x: f"{{#escape y {addWhitespace(x)} j}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_visualize": {
            "stroke": "W-B",
            "callback": lambda x: f"{{#escape shift(V) {addWhitespace(x)} k}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_visualize": {
                "stroke": "W-R",
                "callback": lambda x: f"{{#escape shift(V) {addWhitespace(x)} j}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                },
        "up_remove": {
                "stroke": "R-B",
                "callback": lambda x: f"{{#escape c {addWhitespace(x)} k}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                },
        "down_remove": {
                "stroke": "R-R",
                "callback": lambda x: f"{{#escape c {addWhitespace(x)} j}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                }
        }
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
                "-FP": "<escape> shift(at) <objects>",  # @
                "#-FP": "<escape> q <objects>",  # liSten
                "-FB": "<escape> c s <objects>",  # Blot Furround
                "#-FB": "<escape> d s <objects>", # Blot Surround
                "-FPB": "<escape> z <objects>",  # ZeN
                "-PB": "<escape> g l <objects>",  # lioN
                "#-PB": "<escape> g shift(L) <objects>",  # lioN
                "-F": "<escape> g <objects>",  # the good Spot (primeagen youtube video on the g command)
                "#-F": "shift(s) <objects>", # Furround
                "-P": "<escape> r <objects>",
                "#-P": "<escape> <objects> <objects>", # repeat
                "-B": "<escape> apostrophe <objects>",
                "#-B": "<escape> m <objects>",

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


