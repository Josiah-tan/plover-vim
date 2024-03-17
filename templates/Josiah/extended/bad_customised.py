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
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        },  
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
                "-F": "<escape> <numbers> v <middles> <objects>",  # Fisualise
                "-P": "<escape> <numbers> y <middles> <objects>",  # coPy
                "-B": "<escape> <numbers> c <middles> <objects>",  # Blot
                "": "<escape> <numbers> <middles> <objects>",
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
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        },  
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "@G",
            "mods": {  # 64 total possibilities from #EURPB
                "-FP": "<escape> <numbers> shift(at) <objects>",  # @
                "#-FP": "<escape> <numbers> q <objects>",  # liSten
                "-FB": "<escape> <numbers> c s <objects>",  # Blot Furround
                "#-FB": "<escape> <numbers> d s <objects>", # Blot Surround
                "-FPB": "<escape> <numbers> z <objects>",  # ZeN
                "-PB": "<escape> <numbers> g l <objects>",  # lioN
                "#-PB": "<escape> <numbers> g shift(L) <objects>",  # lioN
                "-F": "<escape> <numbers> g <objects>",  # the good Spot (primeagen youtube video on the g command)
                "#-F": "shift(s) <objects>", # Furround
                "-P": "<escape> <numbers> r <objects>",
                "#-P": "<escape> <numbers> <objects> <objects>", # repeat
                "-B": "<escape> <numbers> apostrophe <objects>",
                "#-B": "<escape> <numbers> m <objects>",

                "-EFP": "<escape> <numbers> bracketleft <objects>", # [ 
                "-UFP": "<escape> <numbers> bracketright <objects>", # ] 
                "#EU": "<escape> <numbers> shift(quotedbl) <objects>", # regIster
                }
            }]
        })


commandObjectLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        },  
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

                "-FPB": "<escape> <numbers> equal <middles> <objects>",
                "-FP": "<escape> <numbers> y s <middles> <objects>",  # coPy Furround
                "-FB": "<escape> <numbers> shift(greater) <middles> <objects>",  # FB looks like half an > arrow
                "-PB": "escape g c <middles> <objects>",  # commeNt
                "-F": "<escape> <numbers> v <middles> <objects>",  # Fisualise
                "-P": "<escape> <numbers> y <middles> <objects>",  # coPy
                "-B": "<escape> <numbers> c <middles> <objects>",  # Blot
                "": "<escape> <numbers> g shift(u) <middles> <objects>",

                "#-FPB": "<escape> <numbers> v <middles> <objects> shift(asciitilde)",
                "#-FP": "escape c x <middles> <objects>",  # vim exFPange
                "#-FB": "<escape> <numbers> less <middles> <objects>",
                "#-PB": "escape g b <middles> <objects>",
                "#-F": "<escape> <numbers> v <middles> <objects> p",  # visualise and paste!
                "#-P": "<escape> <numbers> shift(quotedbl) shift(plus) y <middles> <objects>",
                "#-B": "<escape> <numbers> g shift(question) <middles> <objects>", # Bguestion
                "#": "<escape> <numbers> g u <middles> <objects>",
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
                        },
                    "numbers": {
                        "-S": "2",
                        "-T": "3",
                        "-TS": "4",
                        }
                    }
                )
            ]:
        with suppress(KeyError):
            return look(key)

if __name__ == "__main__":
    import json
    import sys
    dict = {**JosiahLookup.dictionary().items_str_dict(),
            }
    json.dump(dict, sys.stdout, ensure_ascii=False, indent=0)


