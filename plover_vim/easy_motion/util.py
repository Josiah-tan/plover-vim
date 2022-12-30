# from typing import List
from plover.system import english_stenotype as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def insertSpaces(x):
    # works for characters in strings as well
    return ' '.join(x)


def getLeftRightHandLetters(left_hand, right_hand):
    return (s(left_hand) * s(right_hand)).map(insertSpaces)


def combineStrokes(first, second):
    combine = first.named("first") / second.named("second")
    return combine.map(lambda first, second: second)
