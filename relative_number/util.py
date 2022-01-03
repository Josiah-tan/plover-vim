import collections.abc
# import relative_number.globals as Config
import re


def removeNumbers(s):
    return ''.join([i for i in s if not i.isdigit()])


def removeNotNumbers(s):
    return ''.join([i for i in s if i.isdigit()])


# def getDirection(stroke):
#     return {Config.UP: "up", Config.DOWN: "down"}.get(stroke)


def assertGetDirection(strokes, start, end):
    for direction, stroke in strokes.items():
        match = re.fullmatch('([KWR]*)([*-]?)([RBGSDZ]*)', stroke)
        (lhs, _, rhs) = match.groups()
        if lhs == removeNumbers(start) and rhs == removeNumbers(end):
            return direction
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


def recursiveUpdate(d: dict, u: dict) -> dict:
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = recursiveUpdate(d.get(k, {}), v)
        else:
            d[k] = v
    return d
