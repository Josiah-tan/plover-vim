from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your python experience here
from relative_number.builtins import lookup as relative_number_lookup


LONGEST_KEY = 1


def lookup(key):
    for look in [relative_number_lookup]:
        with suppress(KeyError):
            return look(key)
