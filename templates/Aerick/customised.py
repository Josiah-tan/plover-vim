from contextlib import suppress
from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
from plover_vim.relative_number.util import down, up
from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
import plover.system as e
try:
	context = get_context_from_system(e) # will break test suite
except:
	from plover.system import english_stenotype as e
	context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation

LONGEST_KEY = 1
relative_number_lookup = RelativeNumberLookup({
    "disable_defaults": True,
    # using user 2's plover_python_dictionary_lib to generate all of the numbers
    "numbers": s({'-R': '1', '-B': '2', '-G': '3', '-FR': '4', '-PB': '5', '-LG': '6', '-F': '7', '-P': '8', '-L': '9'}),  
    "systems": {
        "0": {
            "stroke": "-E",
            "callback": lambda x: x + "0",
            },
        "00": {
            "stroke": "-U",
            "callback": lambda x: x + "00",
            },
        "000": {
            "stroke": "-EU",
            "callback": lambda x: x + "000",
            },
        "up": {
            "stroke": "-T",
            "callback": up,
            "dependencies": ["0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down": {
            "stroke": "-S",
            "callback": down,
            "dependencies": ["0"],
            "min_number": 1,
            "max_number": 99,
            }
        }
    })

def lookup(key):
    for look in [
            relative_number_lookup,
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError

# in case you are curious what is in your dictionary
# relative_number_lookup.getDictionary().print_items()  
