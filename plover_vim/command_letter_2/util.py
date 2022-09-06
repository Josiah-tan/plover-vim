import re
from plover_vim.command_letter.util import (
        getCharacters, getCasedCharacters, combineModsEnders
        )

# from shared.util.util import (
#         spaceFormat,
#         convert2Stroke,
#         applyModifiers,
#         convertShiftDict,
#         productThenUnion
#         )

from plover.system import english_stenotype as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def getMods(mods):
    # return [s(mod).map(spaceFormat) for mod in mods]
    return [s(mod) for mod in mods]


def getEscape(escape):
    return translation(escape).named("escape")


def getObjects(spelling, symbols):
    return getCasedCharacters(
            getCharacters(spelling, symbols)
            ).named("objects")


def getMiddles(middles):
    return s(middles).named("middles")


def getSystems(mods, enders):
    return combineModsEnders(mods, enders).named("systems")


def _cleanWhiteSpace(key):
    return re.sub(r"\s+", ' ', key).strip(" ")


def cleanWhiteSpace(d):
    return d.map(_cleanWhiteSpace)


def _applyFormat(systems, escape, middles, objects):
    systems = re.sub("<escape>", escape, systems)
    systems = re.sub("<middles>", middles, systems)
    systems = re.sub("<objects>", objects, systems)
    return systems


def applyFormat(systems, srcs):
    # for src in srcs:
    #     systems *= src
    systems *= srcs[0]
    systems *= srcs[1]
    systems *= srcs[2]
    return systems.map(_applyFormat)
