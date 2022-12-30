shifted_symbols_aus = {
        "asciitilde", "exclam", "at",
        "numbersign", "dollar", "percent",
        "asciicircum", "ampersand", "asterisk",
        "parenleft", "parenright", "underscore",
        "plus", "braceleft", "braceright",
        "bar", "colon", "quotedbl",
        # "less", "greater", "question" # shifting "<" => ">" which is weird, seems like "<" is fine without shifting
        "greater", "question"
        }

symbols = {
        "TR": ["tab", "delete", "backspace", "escape"],
        "KPWR": ["up", "left", "right", "down"],
        "KPWHR": ["pageup", "end", "home", "pagedown"],
        "": ["", "tab", "return", "space"],

        # typable symbols
        "HR": ["exclam", "", "notsign", "exclamdown"],
        "PH": ["quotedbl", "", "", ""],
        "TKHR": ["numbersign", "registered", "copyright", ""],
        "KPWH": ["dollar", "euro", "yen", "sterling"],
        "PWHR": ["percent", "", "", ""],
        "SKP": ["ampersand", "", "", ""],
        # "H": ["apostrophe", "", "", ""],
        "H": ["quoteright", "", "", ""],
        "TPH": ["parenleft", "less", "bracketleft", "braceleft"],
        "KWR": ["parenright", "greater", "bracketright", "braceright"],
        "T": ["asterisk", "section", "", "multiply"],
        "K": ["plus", "paragraph", "", "plusminus"],
        "W": ["comma", "", "", ""],
        "TP": ["minus", "", "", ""],
        "R": ["period", "periodcentered", "", ""],
        "WH": ["slash", "", "", "division"],
        "TK": ["colon", "", "", ""],
        "WR": ["semicolon", "", "", ""],
        "TKPW": ["equal", "", "", ""],
        "TPW": ["question", "", "questiondown", ""],
        "TKPWHR": ["at", "", "", ""],
        "PR": ["backslash", "", "", ""],
        "KPR": ["asciicircum", "guillemotleft", "guillemotright", "degree"],
        "KW": ["underscore", "", "", "mu"],
        # "P": ["grave", "", "", ""],
        "P": ["quoteleft", "", "", ""],
        "PW": ["bar", "", "", "brokenbar"],
        "TPWR": ["asciitilde", "", "", ""]
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

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "command_suffix": "{plover:clear_trans_state}",
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
                    "-P": "r",
                    "-B": "m"
                    }
                }]
            }
