from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.command_letter_2.builtins import Lookup as CommandLetterLookup2

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
            "unique_ender": "-LTSZ",  # ring finger on TS, pinky on D
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                "-FPB": "<escape> equal <middles> <objects>",
                "-FP": "<escape> y s <middles> <objects>",  # coPy Furround
                "-FB": "",  # Blot Furround
                "-PB": "<escape> g c <middles> objects>",  # commeNt
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "",

                "#-FPB": "",
                "#-FP": "",
                "#-FB": "",
                "#-PB": "<escape> g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "",
                "#-B": "",
                "#": ""
                }
            }]
    })

# old_stuff = {
#         "-T": "g c",
#         "-D": "d",  # not important
#         "-S": "y s",  # done
#         "-Z": "y",  # done
#         "-TD": "",
#         "-DZ": "d s",  # done
#         "-SZ": "v",  # done
#         "-TS": "",
#         "*T": "g b",
#         "*D": "",
#         "*S": "shift(s)",  # done
#         "*Z": "",
#         "*TD": "",
#         "*DZ": "",
#         "*SZ": "",
#         "*TS": "",
#         "": ""
#         # =
#         # c # done
#         }

assert find_lookup_2.dictionary.longest_key == LONGEST_KEY
assert misc_lookup_2.dictionary.longest_key == LONGEST_KEY
assert command_object_lookup_2.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [find_lookup_2, misc_lookup_2, command_object_lookup_2]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    find_lookup_2.generateJson()
    # misc_lookup_2.generateJson()
    # command_object_lookup_2.generateJson()
