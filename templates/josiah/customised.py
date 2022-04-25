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
from relative_number.builtins import Lookup as RelativeNumberLookup
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
                "": "",

                "#-FPB": "",
                "#-FP": "shift(s) <objects>",
                "#-FB": "<escape> d s <objects>",
                "#-PB": "escape g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "<escape> shift(quotedbl) shift(plus) y <middles> <objects>",
                "#-B": "",
                "#": ""
                }
            }]
    })

relative_number_lookup = RelativeNumberLookup({
    "up": "-B",
    "down": "-R"
    })

josiah_modifier_lookup = JosiahModifierLookup()


def lookup(key):
    for look in [
            find_lookup_2,
            misc_lookup_2,
            command_object_lookup_2,
            relative_number_lookup,
            josiah_modifier_lookup
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError
