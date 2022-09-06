from contextlib import suppress
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")

sys.path.append(repository_location)

# import the modules that you want for your vim experience here
# from command_letter.builtins import Lookup as CommandLetterLookup
# from command_object.builtins import Lookup as CommandObjectLookup
from command_letter_2.builtins import Lookup as CommandLetterLookup2
from relative_number.builtins import Lookup as OldRelativeNumberLookup
from relative_number.util import Zeroes, reverse, double
from relative_number.defaults import up_down_system, clock_system, classic_system
from relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
from josiah_modifier.builtins import Lookup as JosiahModifierLookup

LONGEST_KEY = 1


find_lookup_2 = CommandLetterLookup2({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "E": "c",  # dElEtE
        "EU": "y",  # yoInk
        "U": "v",  # visUalise
        "": ""
        },  # dict: middles
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",  #
                # "-FB": "space space f",  # Forward Back (moving this to another module)
                "-PB": "<escape> <middles> shift(t) <objects>",  # Previous Backwards
                "-F": "<escape> <middles> f <objects>",  # Forwards
                "-P": "<escape> <middles> t <objects>",  # Previous
                "-B": "<escape> <middles> shift(f) <objects>",  # Backwards
                # "": ""  # for normal commands (done in josiah-modifers)
                }
            }]
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
                "-FPB": "<escape> q <objects>",  # liSten
                "-FP": "<escape> shift(at) <objects>",  # @
                # "-FB": "",
                "-PB": "<escape> z <objects>",  # zeN
                "-F": "<escape> g <objects>",  # the good Spot (primeagen youtube video on the g command)
                "-P": "<escape> r <objects>",
                "-B": "<escape> m <objects>",
                "#-B": "<escape> apostrophe <objects>",

                "#-P": "<escape> <objects> <objects>", # repeat
                "-E": "<escape> bracketleft <objects>", # ] unfortuately does not work in insert mode...
                "-U": "<escape> bracketright <objects>", # [ unfortuately does not work in insert mode..

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
                "-FB": "<escape> c s <objects>",  # Blot Furround
                "-PB": "escape g c <middles> <objects>",  # commeNt
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "<escape> g shift(u) <middles> <objects>",

                "#-FPB": "<escape> v <middles> <objects> shift(asciitilde)",
                "#-FP": "shift(s) <objects>",
                "#-FB": "<escape> d s <objects>",
                "#-PB": "escape g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "<escape> shift(quotedbl) shift(plus) y <middles> <objects>",
                "#-B": "",
                "#": "<escape> g u <middles> <objects>"
                }
            }]
    })

# relative_number_lookup = RelativeNumberLookup({
#     "up": "-B",
#     "down": "-R"
#     })

# relative_number_lookup = OldRelativeNumberLookup()
relative_number_lookup = RelativeNumberLookup({
    "disable_defaults": True,
    "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
    "systems": {
        **up_down_system,
        **clock_system,
        "reverseU": {
            "stroke": "-U",
            "callback": reverse,
            "min_number": 10,
            "dependencies": ["0" * i for i in range(1, 10)]
            },
        "doubleU": {
            "stroke": "-U",
            "callback": double,
            "min_number": 1,
            "max_number": 9,
            "dependencies": ["0"]
            },
        "0": {
            "stroke": "-S",
            "callback": Zeroes(1),
            "additional_map": "0",
            },
        "0" * 2: {
                "stroke": "-SZ",
                "callback": Zeroes(2),
                "additional_map": "0" * 2,
                },
        "0" * 3: {
                "stroke": "-Z",
                "callback": Zeroes(3),
                "additional_map": "0" * 3,
                },
        "0" * 4: {
                "stroke": "-TS",
                "callback": Zeroes(4),
                "additional_map": "0" * 4,
                },
        "0" * 5: {
                "stroke": "-TSDZ",
                "callback": Zeroes(5),
                "additional_map": "0" * 5,
                },
        "0" * 6: {
                "stroke": "-DZ",
                "callback": Zeroes(6),
                "additional_map": "0" * 6,
                },
        "0" * 7: {
                "stroke": "-T",
                "callback": Zeroes(7),
                "additional_map": "0" * 7,
                },
        "0" * 8: {
                "stroke": "-TD",
                "callback": Zeroes(8),
                "additional_map": "0" * 8,
                },
        "0" * 9: {
                "stroke": "-D",
                "callback": Zeroes(9),
                "additional_map": "0" * 9,
                },
        # "triple": {
        #         "stroke": "E",
        #         "callback": lambda x: x*3,
        #         "min_number": 0,
        #         "max_number": 9,
        #         },
        "decimal": {
                "stroke": "E",
                "callback": lambda x: x[0] + "." + x[1:],
                "dependencies": ["reverseU", "doubleU", *["0" * i for i in range(1, 10)]],
                "min_number": 0,
                # "max_number": 99,
                }
        }
    })
dict(relative_number_lookup.dictionary.items())

josiah_modifier_lookup = JosiahModifierLookup()


def lookup(key):
    for look in [
            find_lookup_2,
            misc_lookup_2,
            command_object_lookup_2,
            # relative_number_lookup,
            josiah_modifier_lookup
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError
