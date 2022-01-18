from contextlib import suppress
import sys
import platform

linux_repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
windows_repository_location = "c:\\users\\josia\\appdata\\local\\plover\\plover\\vim"
on_wind = "windows" in platform.uname()[0].lower()
if on_wind:
    repository_location = windows_repository_location
else:
    repository_location = linux_repository_location

sys.path.append(repository_location)

# import the modules that you want for your python experience here
from command_letter.builtins import Lookup as CommandLetterLookup
from command_object.builtins import Lookup as CommandObjectLookup
from relative_number.builtins import Lookup as RelativeNumberLookup

LONGEST_KEY = 1


command_letter_lookup = CommandLetterLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_ender": "LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",  #
                # "-FB": "space space f",  # Forward Back (moving this to another module)
                "-PB": "shift(t)",  # Previous Backwards
                "-F": "f",  # Forwards
                "-P": "t",  # Previous
                "-B": "shift(f)",  # Backwards
                "": ""  # for normal commands
                }
            },
        {
            "unique_ender": "-TZ",
            "mods": {
                "-FPB": "q",  # liSten
                "-FP": "shift(at)",  # @
                # "-FB": "",
                "-PB": "z",  # zeN
                "-F": "g",  # the good Spot (primeagen youtube video on the g command)
                "-P": "r",
                "-B": "m"
                }
            }]
        })

command_object_lookup = CommandObjectLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "symbols": {},  # dict: right hand symbols
    "objects": {},  # dict: right hand objects
    "shifted": {},  # set: any symbols that should be shifted
    "middle": {},  # dict: middle parts of vim commands
    "escape": "control(j)",  # default: "escape"
    "systems": [
        {
            "unique_starter": "STPR",
            "mods": {
                "-T": "g c",  # tpope/vim-commenTary (for line comments)
                "-D": "d",  # Delete
                "-S": "y s",  # tpope/vim-Surround (for surrounding things)
                "-Z": "y",  # yank? (plZ give ideas for this one)
                "-TD": "",
                "-DZ": "d s",
                "-SZ": "v",  # ViSualiZe
                "-TS": "",
                "*T": "g b",  # numToStr/Comment.nvim (for block commenting)
                "*D": "",
                "*S": "shift(s)",
                "*Z": "",
                "*TD": "",
                "*DZ": "",
                "*SZ": "",
                "*TS": "",
                "": ""
                }
            }
        ]})

relative_number_lookup = RelativeNumberLookup({
    "up": "B",
    "down": "-R"
    })


def lookup(key):
    for look in [
            command_letter_lookup,
            command_object_lookup,
            relative_number_lookup,
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError
