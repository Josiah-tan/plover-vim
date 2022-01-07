from typing import List
from plover.system import english_stenotype as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def spaceFormat(x):
    return x + ' ' if x != "" else ""


def getEnders(enders):
    return [stroke(ender) for ender in enders]


def getMods(mods):
    return s(mods).map(spaceFormat)


def combineModsEnders(mods, enders):
    lis = []
    for ender, mod in zip(enders, mods):
        lis.append(ender * mod)

    res = lis[0]
    for i in range(1, len(lis)):
        res = res | lis[i]
    return res


def getEscape(escape):
    return translation(spaceFormat(escape))

def getCharacters(spelling, symbols, shifted):

def getCasedCharacters(characters):
    return (
            characters *
            s({"-R": ["shift"], "": []}).named("mods")
            ).map(applyModifiers)

# define your ender here
uniqueEnderSearch = stroke("LTDZ")
uniqueEnderMisc = stroke("-TZ")
# some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ

# fingerspelling dictionary entries for relevant theories
spelling = s({
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
    })


def getShifted(s):
    return f"shift({s})"


def convertShiftDict(raw_symbols, shifted):
    d = raw_symbols
    for key, item in d.items():
        if type(item) == list:
            for i in range(len(item)):
                if item[i] in shifted:
                    d[key][i] = getShifted(item[i])
        elif type(item) == str:
            d[key] = getShifted(item)
        else:
            raise TypeError# (f"expected str or list, instead got {type(item)}")
    return d


def getSymbols(symbols, shifted):
    return s(convertShiftDict(symbols, shifted)).named("symbol")


shifted_symbols_aus = {
        "asciitilde", "exclam", "at",
        "numbersign", "dollar", "percent",
        "asciicircum", "ampersand", "asterisk",
        "parenleft", "parenright", "underscore",
        "plus", "braceleft", "braceright",
        "bar", "colon", "quotedbl",
        "less", "greater", "question"
        }

raw_symbols = {
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
        "H": ["apostrophe", "", "", ""],
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
        "P": ["grave", "", "", ""],
        "PW": ["bar", "", "", "brokenbar"],
        "TPWR": ["asciitilde", "", "", ""]
        }

# same as emily-modifiers format
symbols = s(convertShiftDict(raw_symbols, shifted_symbols_aus)).named("symbol")

symbol_variant = (s({"A": 1, "": 0}) * s({"O": 2, "": 0})).named("symbol_variant")

# left-hand bottom row counts in binary for numbers 0-9
count = (
        s({"R": 1, "": 0}) *
        s({"W": 2, "": 0}) *
        s({"K": 4, "": 0}) *
        s({"S": 8, "": 0})
        )


def getCharacters(spelling, symbols):
    # left-hand bottom row counts in binary for numbers 0-9
    count = (
            s({"R": 1, "": 0}) *
            s({"W": 2, "": 0}) *
            s({"K": 4, "": 0}) *
            s({"S": 8, "": 0})
            )

    symbol_variant = (s({"A": 1, "": 0}) * s({"O": 2, "": 0})).named("symbol_variant")

    return (
            # use * to distinguish symbol input from numerical or character input
            (symbols * symbol_variant * stroke("*")).map(
                lambda symbol, symbol_variant:
                (symbol[symbol_variant] or None) if type(symbol) == list else symbol
                )
            |

            # AO is unused in finger spelling, thus used to disginguish numerical input
            stroke("AO") *

            (
                # if TP is being held as well, then user is inputting a Fx key - like alt+F4
                # add the 'F' if F number
                s({"TP": "F"}) * count.filter(lambda x: 1 <= x <= 12).map(str) |
                count.filter(lambda x: x <= 9).map(str)
                )
            |

            # finger spelling input
            # if there is no entry, pass the error
            spelling.filter(lambda character: character != "")

            ).named("character")

characters = (
        # use * to distinguish symbol input from numerical or character input
        (symbols * symbol_variant * stroke("*")).map(
            lambda symbol, symbol_variant:
            (symbol[symbol_variant] or None) if type(symbol) == list else symbol
            )
        |

        # AO is unused in finger spelling, thus used to disginguish numerical input
        stroke("AO") *

        (
            # if TP is being held as well, then user is inputting a Fx key - like alt+F4
            # add the 'F' if F number
            s({"TP": "F"}) * count.filter(lambda x: 1 <= x <= 12).map(str) |
            count.filter(lambda x: x <= 9).map(str)
            )
        |

        # finger spelling input
        # if there is no entry, pass the error
        spelling.filter(lambda character: character != "")

        ).named("character")


def applyModifiers(character: str, mods: List[str]) -> str:
    # apply those modifiers
    combo = character
    for mod in mods:
        if mod not in combo:  # shift could already be used to create a symbol
            combo = mod + "(" + combo + ")"
    return combo


def addCommandSyntax(combo: str) -> str:
    return "{#" + combo + "}"


def accumulateModifiers(character: str, mods: List[str]) -> str:
    combo = applyModifiers(character, mods)
    # package it up with the syntax
    # all done! :D
    return addCommandSyntax(combo)


dictionary = (
        translation("control(j) ") *
        (
            s({
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",  #
                # "-FB": "space space f",  # Forward Back (moving this to another module)
                "-PB": "shift(t)",  # Previous Backwards
                "-F": "f",  # Forwards
                "-P": "t",  # Previous
                "-B": "shift(f)",  # Backwards
                "": ""  # for normal commands
                }).map(lambda x: x + " " if x != "" else "") * uniqueEnderSearch |
            s({
                "-FPB": "q",  # liSten
                "-FP": "shift(at)",  # at
                # "-FB": "",
                "-PB": "z",  # zeN
                "-F": "g",  # the good Spot (primeagen youtube video on the g command)
                # "-P": "",
                "-B": "m"
                }).map(lambda x: x + " " if x != "" else "") * uniqueEnderMisc
            ) *
        (
            characters *
            s({"-R": ["shift"], "": []}).named("mods")
            ).map(applyModifiers)
        ).map(addCommandSyntax)


def lookup(strokes):
    return dictionary.lookup_tuple(strokes)


LONGEST_KEY = dictionary.longest_key
assert LONGEST_KEY == 1

if __name__ == "__main__":
    dictionary.print_items()
