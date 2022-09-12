import re


def removeNumbers(s):
    return ''.join([i for i in s if not i.isdigit()])


def removeNotNumbers(s):
    return ''.join([i for i in s if i.isdigit()])


def removeDouble(s):
    return ''.join([i for i in s if i != "D"])


def assertGetDirection(strokes, start, wild, end):
    for direction, stroke in strokes.items():
        match = re.fullmatch('([KWR]*)([*-]?)([RBGSDZ]*)', stroke)
        (lhs, mid, rhs) = match.groups()
        if lhs == removeNumbers(start) and \
                rhs == removeDouble(removeNumbers(end)) and \
                (mid == wild or (mid == "-" and wild == "") or
                (mid == "" and wild == "-")):
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


def assertDoubleValue(number, end):
    if "D" in end:
        if number >= 10:
            raise KeyError
        return number * 11
    return number


class Zeroes:
    def __init__(self, number_zeroes: int):
        self.number_zeroes = number_zeroes
    def excludezeroes(self, string: str):
        return "0" in string
    def __call__(self, string: str):
        if self.excludezeroes(string):
            return None
        return string + self.number_zeroes * "0"

def reverse(string: str):
    return string[::-1]

def double(string: str):
    return string * 2

def up(string: str):
    return f"{{#up{' up' * (int(string) - 1)}}}"

def down(string: str):
    return f"{{#down{' down' * (int(string) - 1)}}}"

def clock(string: str):
    return string + ":00"

def addWhitespace(string: str):
    return " ".join([i for i in string])
