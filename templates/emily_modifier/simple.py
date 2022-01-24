from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your python experience here
from emily_modifier.builtins import emilyLookup, escapedLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [emilyLookup, escapedLookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    # emilyLookup.generateJson()
    escapedLookup.generateJson()
