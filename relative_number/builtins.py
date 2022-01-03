import re
from shared.builtins.builtins import containsNumber
from relative_number.util import (
        assertGetDirection, assertGetInversion,
        assertGetNumber, assertDoubleValue
        )
from relative_number.util import recursiveUpdate
from relative_number.config import LONGEST_KEY
from relative_number.defaults import defaults


class Lookup:
    def update(self, opts={}):
        if opts:
            recursiveUpdate(self.opts, opts)

    def __init__(self, opts={}):
        self.opts = defaults
        self.update(opts)

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        stroke = chord[0]
        if not containsNumber(stroke):
            raise KeyError

        match = re.fullmatch(
                r'([12K3W4R]*)([50]*)([*-]?)([EU]*)([6R7B8G9SDZ]*)',
                stroke)

        (start, mid_left, wild, inversion, end) = match.groups()

        direction = assertGetDirection(
                {"up": self.opts["up"], "down": self.opts["down"]},
                start, end)

        isInverted = assertGetInversion(inversion)
        repeat = assertGetNumber(start, mid_left, isInverted, end)
        repeat = assertDoubleValue(repeat, end)

        output = f"{{#{direction}{f' {direction}' * (repeat - 1)}}}"
        return output


def lookup(chord):
    return Lookup()(chord)
