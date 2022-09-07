from plover_vim.shared.util import addCommandSyntax
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_letter.defaults import (
        spelling, symbols, shifted_symbols_aus
        )
from plover_vim.command_letter.builtins import SingleStrokeLeft
from plover_vim.easy_motion.util import getLeftRightHandLetters, combineStrokes
from plover_vim.easy_motion.defaults import (
        defaults, left_hand, right_hand
        )
from plover_vim.easy_motion.config import LONGEST_KEY


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
