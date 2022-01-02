import relative_number.globals as Config
from shared.builtins.builtins import containsNumber
import re


def removeNumbers(s):
    return ''.join([i for i in s if not i.isdigit()])


def removeNotNumbers(s):
    return ''.join([i for i in s if i.isdigit()])


def getDirection(stroke):
    return {Config.UP: "up", Config.DOWN: "down"}.get(stroke)


def assertGetDirection(strokes, start, end):
    for raw_stroke in strokes:
        match = re.fullmatch('([KWR]*)([*-]?)([RBGSDZ]*)', raw_stroke)
        (lhs, _, rhs) = match.groups()
        if lhs == removeNumbers(start) and rhs == removeNumbers(end):
            return getDirection(raw_stroke)
    raise KeyError


def assertGetNumber(start, mid_left, isInverted, end):
    start = removeNotNumbers(start)
    end = removeNotNumbers(end)
    number = start + mid_left + end

    if number == "0":
        raise KeyError
    elif len(number) == 1 and not isInverted:
        return int(number)
    elif len(number) == 2:
        if isInverted:
            return int(number[1] + number[0])
        else:
            return int(number)
    raise KeyError


def assertGetInversion(inversion):
    if inversion == "":
        return False
    if inversion == "EU":
        return True
    raise KeyError


def testLookup(chord, down, up):
    Config.UP = up
    Config.DOWN = down
    return lookup(chord)


# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(chord):
    assert len(chord) <= Config.LONGEST_KEY
    stroke = chord[0]
    if not containsNumber(stroke):
        raise KeyError

    match = re.fullmatch(r'([12K3W4R]*)([50]*)([*-]?)([EU]*)([6R7B8G9SDZ]*)', stroke)
    (start, mid_left, wild, inversion, end) = match.groups()

    direction = assertGetDirection((Config.UP, Config.DOWN), start, end)
    isInverted = assertGetInversion(inversion)
    repeat = assertGetNumber(start, mid_left, isInverted, end)

    output = f"{{#{direction}{f' {direction}' * (repeat - 1)}}}"
    return output

##
