# import the modules that you want for your python experience here
# call them in this lookup function
import sys; sys.path.append("/home/josiah/.dotfiles/plover/.config/plover/vim")
from relative_number.main import lookup as relative_number_lookup
LONGEST_KEY = 1


def lookup(key):
    return relative_number_lookup(key)


