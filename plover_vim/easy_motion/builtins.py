# from plover_vim.shared.util import addCommandSyntax
from collections.abc import Callable
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_letter.builtins import SingleStrokeLeft
from plover_vim.easy_motion.util import getLeftRightHandLetters, combineStrokes
from plover_vim.easy_motion.defaults import (
        defaults, left_hand, right_hand,
        spelling, symbols, shifted_symbols_aus
        )
from plover_vim.easy_motion.config import LONGEST_KEY


# def addCommandSyntax(command_suffix = "") -> Callable[[str], str]:
#     def _addCommandSyntax(combo: str) -> str:
#         return f"{{#{combo}}}{command_suffix}"
#     return _addCommandSyntax
#     # return "{#" + combo + "}{plover:clear_trans_state}"
# # addCommandSyntax
def addCommandSyntax(command_suffix):
    def _addCommandSyntax(combo):
        return f"{{#{combo}}}{command_suffix}"
    return _addCommandSyntax

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
        # print(f"self.opts = {self.opts}")
        return single_stroke.map(addCommandSyntax("{^}")) | combineStrokes(single_stroke, letters).map(addCommandSyntax(self.opts["command_suffix"]))

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


lookup = Lookup()
# for i, j in lookup.dictionary.items():
#     if len(i) == 1:
#         print(i, j)
