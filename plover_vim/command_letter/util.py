from plover_vim.shared.util import (
        spaceFormat,
        convert2Stroke,
        applyModifiers,
        convertShiftDict,
        productThenUnion
        )

from plover.system import english_stenotype as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def getEnders(enders):
    return convert2Stroke(enders)


def combineModsEnders(mods, enders):
    return productThenUnion(mods, enders)


def getEscape(escape):
    return translation(spaceFormat(escape))


def getCasedCharacters(characters):
    return (
            characters *
            s({"-R": ["shift"], "": []}).named("mods")
            ).map(applyModifiers)


def getSymbols(symbols, shifted):
    return s(convertShiftDict(symbols, shifted)).named("symbol")


def getCharacters(spelling, symbols):
    spelling = s(spelling)
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
