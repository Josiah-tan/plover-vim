defaults = {
        "up": "-B",
        "down": "-R",
        }

from plover_vim.relative_number.util import reverse, double, Zeroes
# from plover.system import english_stenotype as e
from plover_vim.relative_number.util import down, up, clock, addWhitespace
from plover_vim.relative_number.Roman_numeral import number2Roman


classic_system = {
        "reverseU": {
            "stroke": "-U",
            "callback": reverse,
            "min_number": 10,
            "dependencies": ["zeroes"]
            },
        "doubleU": {
            "stroke": "-U",
            "callback": double,
            "min_number": 1,
            "max_number": 9,
            "dependencies": ["0"]
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

vim_up_down_system = {
        "up_yank": {
            "stroke": "K-B",
            "callback": lambda x: f"{{#escape y {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_yank": {
            "stroke": "K-R",
            "callback": lambda x: f"{{#escape y {addWhitespace(x)} j}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_visualize": {
            "stroke": "W-B",
            "callback": lambda x: f"{{#escape shift(V) {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_visualize": {
            "stroke": "W-R",
            "callback": lambda x: f"{{#escape shift(V) {addWhitespace(x)} j}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "up_remove": {
            "stroke": "R-B",
            "callback": lambda x: f"{{#escape c {addWhitespace(x)} k}}",
            "dependencies": ["reverseU", "doubleU", "0"],
            "min_number": 1,
            "max_number": 99,
            },
        "down_remove": {
            "stroke": "R-R",
            "callback": lambda x: f"{{#escape c {addWhitespace(x)} j}}",
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
            "post_callback": (lambda x: x)
            },
        "clock_append": {
            "stroke": "-RBG",
            "callback": lambda x: f"{{^}}:{int(x):02}",
            "dependencies": ["reverseU", "doubleU"],
            "min_number": 0,
            "max_number": 60,
            "post_callback": (lambda x: x)
            }
        }

zeroes_system = {
        "zeroes": {"dependencies": ["0" * i for i in range(1, 10)]},
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
        }

Roman_system = {
        "Roman" : {
            "stroke": "R",
            "callback": number2Roman,
            "dependencies": ["reverseU", "doubleU", "zeroes"],
            "min_number": 1,
            "max_number": 3999,
            "post_callback": lambda x: x
            }
        }

symbol_system = {
        "decimal": {
            "stroke": "E",
            "callback": lambda x: x[0] + "." + x[1:],
            "dependencies": ["reverseU", "doubleU", "zeroes"],
            "min_number": 0
            },
        "percentage": {
            "stroke": "-G",
            "callback": lambda x: x + "%",
            "dependencies": ["reverseU", "doubleU", "zeroes", "decimal"]
            },
        "dollar": {
            "stroke": "KR",
            "callback": lambda x: "$" + x,
            "dependencies": ["reverseU", "doubleU", "zeroes", "decimal"]
            }
        }

default_system = {
        **classic_system, **zeroes_system, **up_down_system, **clock_system, **Roman_system, **symbol_system, **vim_up_down_system
        }

defaults_2 = {
        "silence_warnings": False,
        "disable_defaults": True,
        "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
        "systems": default_system
        }
