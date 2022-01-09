from command_letter.defaults import shifted_symbols_aus

objects = {
        "-PG": ["p", "", "", ""],
        "-RL": ["w", "shift(w)", "", ""],
        }

symbols = {
        # typable symbols
        "-FR": ["exclam", "notsign", "", "exclamdown"],
        "-FP": ["quotedbl", "", "", ""],
        "-FRLG": ["numbersign", "copyright", "registered", ""],
        "-RPBL": ["dollar", "yen", "euro", "sterling"],
        "-FRPB": ["percent", "", "", ""],
        "-FBG": ["ampersand", "", "", ""],
        "-F": ["apostrophe", "", "", ""],
        "-FPL": ["parenleft", "bracketleft", "less", "braceleft"],
        "-RBG": ["parenright", "bracketright", "greater", "braceright"],
        "-L": ["asterisk", "", "section", "multiply"],
        "-G": ["plus", "", "paragraph", "plusminus"],
        "-B": ["comma", "", "", ""],
        "-PL": ["minus", "", "", ""],
        "-R": ["period", "", "periodcentered", ""],
        "-RP": ["slash", "", "", "division"],
        "-LG": ["colon", "", "", ""],
        "-RB": ["semicolon", "", "", ""],
        "-PBLG": ["equal", "", "", ""],
        "-FPB": ["question", "questiondown", "", ""],
        "-FRPBLG": ["at", "", "", ""],
        "-FB": ["backslash", "", "", ""],
        "-RPG": ["asciicircum", "guillemotright", "guillemotleft", "degree"],
        "-BG": ["underscore", "", "", "mu"],
        "-P": ["grave", "", "", ""],
        "-PB": ["bar", "", "", "brokenbar"],
        "-FPBG": ["asciitilde", "", "", ""],
        # "FPBL": ["↑", "←", "→", "↓"]
            }
middle = {
        "O": "i",
        "A": "a",
        "": ""
        }

defaults = {
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "symbols": symbols,  # dict: right hand symbols
    "objects": objects,  # dict: right hand objects
    "shifted": shifted_symbols_aus,
    "middle": middle,  # dict: middle parts of vim commands
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_starter": "STPR",
            "mods": {
                "-T": "g c",  # tpope/vim-commenTary (for line comments)
                "-D": "d",  # Delete
                "-S": "y s",  # tpope/vim-Surround (for surrounding things)
                "-Z": "y",  # yank? (plZ give ideas for this one)
                "-TD": "",
                "-DZ": "",
                "-SZ": "v",  # ViSualiZe
                "-TS": "",
                "*T": "g b",  # numToStr/Comment.nvim (for block commenting)
                "*D": "",
                "*S": "shift(s)",
                "*Z": "",
                "*TD": "",
                "*DZ": "",
                "*SZ": "",
                "*TS": ""
                }
            }
        ]}