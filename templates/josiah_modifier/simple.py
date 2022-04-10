from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from josiah_modifier.builtins import lookup as josiahLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [josiahLookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    josiahLookup.generateJson()
