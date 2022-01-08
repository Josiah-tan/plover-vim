from contextlib import suppress
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your python experience here
from command_object.builtins import Lookup as CommandObjectLookup

LONGEST_KEY = 1


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
                "-DZ": "",
                "-SZ": "v",  # ViSualiZe
                "-TS": "",
                "*T": "g b",  # numToStr/Comment.nvim (for block commenting)
                "*D": "",
                "*S": "shift(s)",
                "*Z": "",
                "*TD": "",
                "*DZ": "",
                "*SZ": "",
                "*TS": ""
                }
            }
        ]})


assert command_object_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [command_object_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    command_object_lookup.generateJson()
