import collections

from typing import List
from plover.system import english_stenotype as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def recursiveUpdate(d: dict, u: dict) -> dict:
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = recursiveUpdate(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def spaceFormat(x):
    return x + ' ' if x != "" else ""


def convert2Stroke(x):
    return [stroke(i) for i in x]


def getMods(mods):
    return [s(mod).map(spaceFormat) for mod in mods]


def applyModifiers(character: str, mods: List[str]) -> str:
    # apply those modifiers
    combo = character
    for mod in mods:
        if mod not in combo:  # shift could already be used to create a symbol
            combo = mod + "(" + combo + ")"
    return combo


# def addCommandSyntax(combo: str) -> str:
#     return "{#" + combo + "}{plover:clear_trans_state}"
def addCommandSyntax(command_suffix):
    def _addCommandSyntax(combo):
        return f"{{#{combo}}}{command_suffix}"
    return _addCommandSyntax

# def accumulateModifiers(character: str, mods: List[str]) -> str:
#     combo = applyModifiers(character, mods)
#     # package it up with the syntax
#     # all done! :D
#     return addCommandSyntax(combo)


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
            raise TypeError
    return d


def productThenUnion(first, second):
    res = None
    for s, f in zip(second, first):
        mult = s * f
        if res is None:
            res = mult
        else:
            res = res | mult
    return res

