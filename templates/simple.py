# import the modules that you want for your python experience here
from contextlib import suppress
import sys; sys.path.append("/home/josiah/.dotfiles/plover/.config/plover/vim")
from relative_number.builtins import lookup as relative_number_lookup

LONGEST_KEY = 1


def lookup(key):
    for look in [relative_number_lookup]:
        with suppress(KeyError):
            return look(key)
