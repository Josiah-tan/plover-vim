defaults = {
        "up": "-B",
        "down": "-R",
        }

from relative_number.util import reverse, double, Zeroes
# from plover.system import english_stenotype as e
from relative_number.util import down, up, clock


classic_system = {
        "reverseU": {
            "stroke": "-U",
            "callback": reverse,
            "min_number": 10,
            },
        "doubleU": {
            "stroke": "-U",
            "callback": double,
            "min_number": 0,
            "max_number": 9,
            },
        }

# zeroes_system = {
#         "zeros": {"dependencies": ["0" * i for i in range(1, 3)]},
#         "0": {
#             "stroke": "-S",
#             "callback": Zeroes(1),
#             "dependencies": ["reverseU", "doubleU"]
#             },
#         "0" * 2: {
#             "stroke": "-SZ",
#             "callback": Zeroes(2),
#             "dependencies": ["reverseU", "doubleU"]
#             },
#         }

up_down_system = {
        "up": {
            "stroke": "-R",
            "callback": down,
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down": {
            "stroke": "-B",
            "callback": up,
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            }
        }

clock_system = {
        "clock": {
            "stroke": "-BG",
            "callback": clock,
            "dependencies": ["reverseU", "doubleU"],
            "min_number": 1,
            "max_number": 24,
            }
        }

zeroes_system = {
        "zeros": {"dependencies": ["0" * i for i in range(1, 10)]},
        "0": {
            "stroke": "-S",
            "callback": Zeroes(1),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 2: {
            "stroke": "-SZ",
            "callback": Zeroes(2),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 3: {
            "stroke": "-Z",
            "callback": Zeroes(3),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 4: {
            "stroke": "-TS",
            "callback": Zeroes(4),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 5: {
            "stroke": "-TSDZ",
            "callback": Zeroes(5),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 6: {
            "stroke": "-DZ",
            "callback": Zeroes(6),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 7: {
            "stroke": "-T",
            "callback": Zeroes(7),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 8: {
            "stroke": "-TD",
            "callback": Zeroes(8),
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 9: {
            "stroke": "-D",
            "callback": Zeroes(9),
            "dependencies": ["reverseU", "doubleU"]
            },
        }

default_system = {
        **classic_system, **zeroes_system, **up_down_system, **clock_system
        }

defaults_2 = {
        "silence_warnings": True,
        "disable_defaults": True,
        "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9', "-S": '0'},
        "systems": default_system
        }
