from contextlib import suppress

# import the modules that you want for your vim experience here
# from command_letter.builtins import Lookup as CommandLetterLookup
# from command_object.builtins import Lookup as CommandObjectLookup

from plover_vim.command_letter_2.builtins import Lookup as CommandLetterLookup2
from plover_vim.relative_number.util import Zeroes, reverse, double, addWhitespace
from plover_vim.relative_number.defaults import classic_system, zeroes_system, up_down_system, clock_system, Roman_system, symbol_system
from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
from plover_vim.Josiah_modifier.builtins import Lookup as JosiahModifierLookup

LONGEST_KEY = 1

find_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "#E": "shift(t)",  # "#" to denote go to just before the letter
        "#U": "t",  
        "E": "shift(f)",    # E (because it is more to the left)
        "U": "f",    # U (because it is more to the right)
        },  # dict: middles
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-LTDZ",
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

command_object_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "E": "i",  # physically located closer to keyboard centre
        "EU": "O",  # used in Org mode?
        "U": "a",  # physically localed away from the keyboard centre
        "": ""
        },  # dict: middles
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-TDZ",  # ring finger on T, pinky on DZ
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                "-FPB": "<escape> equal <middles> <objects>",
                "-FP": "<escape> y s <middles> <objects>",  # coPy Furround
                "-FB": "",  # Blot Furround
                "-PB": "escape g c <middles> <objects>",  # commeNt
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "<escape> g shift(u) <middles> <objects>",

                "#-FPB": "<escape> v <middles> <objects> shift(asciitilde)",
                "#-FP": "",
                "#-FB": "",
                "#-PB": "escape g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "<escape> shift(quotedbl) shift(plus) y <middles> <objects>",
                "#-B": "",
                "#": "<escape> g u <middles> <objects>"
                }
            }]
    })

# relative_number_lookup = OldRelativeNumberLookup()
relative_number_lookup = RelativeNumberLookup({
    "disable_defaults": True,
    "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
    "systems": {
        **classic_system,
        **zeroes_system,
        **up_down_system,
        **clock_system,
        **Roman_system,
        **symbol_system,
        # **vim_up_down_system
        "up_yank": {
            "stroke": "K-B",
            "callback": lambda x: f"{{#control(j) y {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_yank": {
            "stroke": "K-R",
            "callback": lambda x: f"{{#control(j) y {addWhitespace(x)} j}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_visualize": {
            "stroke": "W-B",
            "callback": lambda x: f"{{#control(j) shift(V) {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_visualize": {
            "stroke": "W-R",
            "callback": lambda x: f"{{#control(j) shift(V) {addWhitespace(x)} j}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_remove": {
            "stroke": "R-B",
            "callback": lambda x: f"{{#control(j) c {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_remove": {
            "stroke": "R-R",
            "callback": lambda x: f"{{#control(j) c {addWhitespace(x)} j}}",
            "dependencies": ["reverseU", "doubleU", "0"],
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
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-TZ",
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

Josiah_modifier_lookup = JosiahModifierLookup()


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

