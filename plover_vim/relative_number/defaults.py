defaults = {
        "up": "-B",
        "down": "-R",
        }

from plover_vim.relative_number.util import reverse, double, Zeroes
# from plover.system import english_stenotype as e
from plover_vim.relative_number.util import down, up, clock


classic_system = {
        "reverseU": {
            "stroke": "-U",
            "callback": reverse,
            "min_number": 12,
            },
        "doubleU": {
            "stroke": "-U",
            "callback": double,
            "min_number": 1,
            "max_number": 9,
            },
        }


up_down_system = {
        "up": {
            "stroke": "-B",
            "callback": up,
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down": {
            "stroke": "-R",
            "callback": down,
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
            "additional_map": "0",
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 2: {
            "stroke": "-SZ",
            "callback": Zeroes(2),
            "additional_map": "0" * 2,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 3: {
            "stroke": "-Z",
            "callback": Zeroes(3),
            "additional_map": "0" * 3,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 4: {
            "stroke": "-TS",
            "callback": Zeroes(4),
            "additional_map": "0" * 4,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 5: {
            "stroke": "-TSDZ",
            "callback": Zeroes(5),
            "additional_map": "0" * 5,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 6: {
            "stroke": "-DZ",
            "callback": Zeroes(6),
            "additional_map": "0" * 6,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 7: {
            "stroke": "-T",
            "callback": Zeroes(7),
            "additional_map": "0" * 7,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 8: {
            "stroke": "-TD",
            "callback": Zeroes(8),
            "additional_map": "0" * 8,
            "dependencies": ["reverseU", "doubleU"]
            },
        "0" * 9: {
            "stroke": "-D",
            "callback": Zeroes(9),
            "additional_map": "0" * 9,
            "dependencies": ["reverseU", "doubleU"]
            },
        }

default_system = {
        **classic_system, **zeroes_system, **up_down_system, **clock_system
        }

defaults_2 = {
        "silence_warnings": False,
        "disable_defaults": True,
        "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
        "systems": default_system
        }
