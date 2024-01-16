from contextlib import suppress

# import the modules that you want for your vim experience here
# from command_letter.builtins import Lookup as CommandLetterLookup
# from command_object.builtins import Lookup as CommandObjectLookup

from plover_vim.command_letter_2.builtins import Lookup as CommandLetterLookup2
from plover_vim.relative_number.util import Zeroes, reverse, double, addWhitespace, up, down
from plover_vim.relative_number.defaults import classic_system, zeroes_system, up_down_system, clock_system, Roman_system, symbol_system
from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
# from plover_vim.Josiah_modifier.builtins import Lookup as JosiahModifierLookup
from plover_vim.Josiah_modifier.builtins import Lookup as JosiahLookup

LONGEST_KEY = 1

find_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        },  
    "middles": {
        "#E": "shift(t)",  # "#" to denote go to just before the letter
        "#U": "t",  
        "E": "shift(f)",    # E (because it is more to the left)
        "U": "f",    # U (because it is more to the right)
        },  # dict: middles
    "escape": "control(j)",  # default: "escape"
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

command_object_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
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
    "escape": "control(j)",  # default: "escape"
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
            "callback": lambda x: f"{{#control(j) y {addWhitespace(x)} k}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_yank": {
            "stroke": "K-R",
            "callback": lambda x: f"{{#control(j) y {addWhitespace(x)} j}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_visualize": {
            "stroke": "W-B",
            "callback": lambda x: f"{{#control(j) shift(V) {addWhitespace(x)} k}}",
            "dependencies": ["reverse", "double"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_visualize": {
                "stroke": "W-R",
                "callback": lambda x: f"{{#control(j) shift(V) {addWhitespace(x)} j}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                },
        "up_remove": {
                "stroke": "R-B",
                "callback": lambda x: f"{{#control(j) c {addWhitespace(x)} k}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                },
        "down_remove": {
                "stroke": "R-R",
                "callback": lambda x: f"{{#control(j) c {addWhitespace(x)} j}}",
                "dependencies": ["reverse", "double"],
                "min_number": 1,
                "max_number": 99,
                }
        }
    })

misc_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "middles": {},  # dict: middles
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        },  
    "escape": "control(j)",  # default: "escape"
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
                }
            }]
        })

Josiah_modifier_lookup = JosiahLookup({
    "unique_ender": "@",
    "numbers": {
        "-S": "2",
        "-T": "3",
        "-TS": "4",
        }
    })


def lookup(key):
    for look in [
            find_lookup_2,
            misc_lookup_2,
            command_object_lookup_2,
            relative_number_lookup,
            Josiah_modifier_lookup
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError


