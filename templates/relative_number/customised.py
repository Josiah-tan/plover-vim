from contextlib import suppress
import sys
repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
sys.path.append(repository_location)

# import the modules that you want for your python experience here
from relative_number.builtins import Lookup as RelativeNumberLookup

LONGEST_KEY = 1


relative_number_lookup = RelativeNumberLookup({
    "up": "B",
    "down": "-R"
    })

# Other API ideas (not implemented unless people want it)

# relative_number_lookup = RelativeNumberLookup({
#     "disable_defaults": True,
#     "translations": {
#         "up": "B",
#         "down": "-R"
#         },
#     "escape": {
#         },
#     "multiplier": {
#         },
#     })
#
# relative_number_lookup = RelativeNumberLookup({
#     "disable_defaults": True,
#     "translations": {
#         "k": "B",
#         "j": "-R"
#         },
#     "use_escape": ["k", "j"],
#     "multiplier": ["k", "j"],
#     })


def lookup(key):
    for look in [relative_number_lookup]:
        with suppress(KeyError):
            return look(key)

