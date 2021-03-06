from shared.util.util import addCommandSyntax
from shared.builtins import BaseLookup
from command_letter.defaults import (
        spelling, symbols, shifted_symbols_aus
        )
from command_letter.builtins import SingleStrokeLeft
from easy_motion.util import getLeftRightHandLetters, combineStrokes
from easy_motion.defaults import (
        defaults, left_hand, right_hand
        )
from easy_motion.config import LONGEST_KEY


class Lookup(BaseLookup, SingleStrokeLeft):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self):
        single_stroke = self.getLeftCommands()
        letters = getLeftRightHandLetters(
                self.opts['left_hand'],
                self.opts['right_hand'])
        return combineStrokes(single_stroke, letters).map(addCommandSyntax)

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


lookup = Lookup()
