from contextlib import suppress
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from relative_number.builtins import Lookup as RelativeNumberLookup

LONGEST_KEY = 1


relative_number_lookup = RelativeNumberLookup({
    "up": "-B",
    "down": "-R"
    })

# Other API ideas (not implemented unless people want it)

# relative_number_lookup = RelativeNumberLookup({
#     "disable_defaults": True,
#     "translations": {
#         "up": "-B",
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
#         "k": "-B",
#         "j": "-R"
#         },
#     "use_escape": ["k", "j"],
#     "multiplier": ["k", "j"],
#     })


def lookup(key):
    for look in [relative_number_lookup]:
        with suppress(KeyError):
            return look(key)

