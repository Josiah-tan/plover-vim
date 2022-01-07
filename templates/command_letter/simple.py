from contextlib import suppress
# change this to be the location of where you installed this respository
import sys; sys.path.append("/home/josiah/.dotfiles/plover/.config/plover/vim")

# import the modules that you want for your python experience here
from command_letter.builtins import findLookup, miscLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [findLookup, miscLookup]:
        with suppress(KeyError):
            return look(key)
