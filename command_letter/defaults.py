shifted_symbols_aus = {
        "asciitilde", "exclam", "at",
        "numbersign", "dollar", "percent",
        "asciicircum", "ampersand", "asterisk",
        "parenleft", "parenright", "underscore",
        "plus", "braceleft", "braceright",
        "bar", "colon", "quotedbl",
        "less", "greater", "question"
        }

symbols = {
        "A": "a",
        "PW": "b",
        "KR": "c",
        "TK": "d",
        "E": "e",
        "TP": "f",
        "TKPW": "g",
        "H": "h",
        "EU": "i",
        # "AOEU": "i", # magnum
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
        "U": "u",
        "SR": "v",
        "W": "w",
        "KP": "x",
        "KWR": "y",
        "STKPW": "z",
        # "STKPWHR": "z", # magnum
        }
spelling = {
        "A": "a",
        "PW": "b",
        "KR": "c",
        "TK": "d",
        "E": "e",
        "TP": "f",
        "TKPW": "g",
        "H": "h",
        "EU": "i",
        "AOEU": "i",  # magnum
        "SKWR": "j",
        "SKWRAEU": "j",  # magnum
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
        "U": "u",
        "SR": "v",
        "W": "w",
        "KP": "x",
        "KWR": "y",
        "STKPW": "z",
        "STKPWHR": "z",  # magnum
        }

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "escape": "escape",
        "systems": [
            {
                "unique_ender": "LTDZ",
                "mods": {
                    # "-FPB": "",  # left empty for you to customise!
                    # "-FP": "",  #
                    # "-FB": "space space f",  # Forward Back (moving this to another module)
                    "-PB": "shift(t)",  # Previous Backwards
                    "-F": "f",  # Forwards
                    "-P": "t",  # Previous
                    "-B": "shift(f)",  # Backwards
                    "": ""  # for normal commands
                    }
                },
            {
                "unique_ender": "-TZ",
                "mods": {
                    "-FPB": "q",  # liSten
                    "-FP": "shift(at)",  # at
                    # "-FB": "",
                    "-PB": "z",  # zeN
                    "-F": "g",  # the good Spot (primeagen youtube video on the g command)
                    # "-P": "",
                    "-B": "m"
                    }
                }]
            }
