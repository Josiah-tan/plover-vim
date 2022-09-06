from contextlib import suppress

# import the modules that you want for your vim experience here
# from command_letter.builtins import Lookup as CommandLetterLookup
# from command_object.builtins import Lookup as CommandObjectLookup
from plover_vim.relative_number.util import Zeroes, reverse, double
from plover_vim.relative_number.defaults import up_down_system, clock_system, classic_system
from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup

LONGEST_KEY = 1
# relative_number_lookup = OldRelativeNumberLookup()
relative_number_lookup = RelativeNumberLookup({
    "disable_defaults": True,
    "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
    "systems": {
        **up_down_system,
        **clock_system,
        "reverseU": {
            "stroke": "-U",
            "callback": reverse,
            "min_number": 10,
            "dependencies": ["0" * i for i in range(1, 10)]
            },
        "doubleU": {
            "stroke": "-U",
            "callback": double,
            "min_number": 1,
            "max_number": 9,
            "dependencies": ["0"]
            },
        "0": {
            "stroke": "-S",
            "callback": Zeroes(1),
            "additional_map": "0",
            },
        "0" * 2: {
                "stroke": "-SZ",
                "callback": Zeroes(2),
                "additional_map": "0" * 2,
                },
        "0" * 3: {
                "stroke": "-Z",
                "callback": Zeroes(3),
                "additional_map": "0" * 3,
                },
        "0" * 4: {
                "stroke": "-TS",
                "callback": Zeroes(4),
                "additional_map": "0" * 4,
                },
        "0" * 5: {
                "stroke": "-TSDZ",
                "callback": Zeroes(5),
                "additional_map": "0" * 5,
                },
        "0" * 6: {
                "stroke": "-DZ",
                "callback": Zeroes(6),
                "additional_map": "0" * 6,
                },
        "0" * 7: {
                "stroke": "-T",
                "callback": Zeroes(7),
                "additional_map": "0" * 7,
                },
        "0" * 8: {
                "stroke": "-TD",
                "callback": Zeroes(8),
                "additional_map": "0" * 8,
                },
        "0" * 9: {
                "stroke": "-D",
                "callback": Zeroes(9),
                "additional_map": "0" * 9,
                },
        # "triple": {
        #         "stroke": "E",
        #         "callback": lambda x: x*3,
        #         "min_number": 0,
        #         "max_number": 9,
        #         },
        "decimal": {
                "stroke": "E",
                "callback": lambda x: x[0] + "." + x[1:],
                "dependencies": ["reverseU", "doubleU", *["0" * i for i in range(1, 10)]],
                "min_number": 0,
                # "max_number": 99,
                }
        }
    })


def lookup(key):
    for look in [
            relative_number_lookup
            ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError

