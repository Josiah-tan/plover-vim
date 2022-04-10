from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from easy_motion.builtins import lookup as findLetterLookup

LONGEST_KEY = 2


def lookup(key):
    for look in [findLetterLookup]:
        with suppress(KeyError):
            return look(key)
