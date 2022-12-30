from plover_vim.command_letter.defaults import shifted_symbols_aus, symbols

spelling = {
        "A": "a",
        "PW": "b",
        "KR": "c",
        "TK": "d",
        # "E": "e", plover
        "SK": "e",  # Abby
        "TP": "f",
        "TKPW": "g",
        "H": "h",
        # "EU": "i", plover
        # "AOEU": "i", # magnum
        "SKW": "i",  # Abby
        "SKWR": "j",
        # "SKWRAEU": "j", # magnum
        "K": "k",
        "HR": "l",
        "PH": "m",
        "TPH": "n",
        "O": "o",
        "P": "p",
        "KW": "q",
        "R": "r",
        "S": "s",
        "T": "t",
        # "U": "u", plover
        "WR": "u",  # Abby
        "SR": "v",
        "W": "w",
        "KP": "x",
        "KWR": "y",
        "STKPW": "z",
        # "STKPWHR": "z", # magnum
        }

prefixes = {
        "#": "control(j)",
        "E": "escape",  # EscapE
        "EU": "control(j) control(w)",  # vim splIt or wIn
        "#EU": "control(r)",  # regIster
        "U": "control(b)",  # tmUx
        "#E": "control(x)",  # Ex command
        "": "",
        }

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "command_suffix": "{plover:clear_trans_state}",
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "unique_ender": "-LTZ",
        "prefixes": prefixes
        }
