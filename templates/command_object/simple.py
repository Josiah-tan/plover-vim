from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your python experience here
from command_object.builtins import lookup as command_object_lookup

LONGEST_KEY = 1


def lookup(key):
    for look in [command_object_lookup]:
        with suppress(KeyError):
            return look(key)
