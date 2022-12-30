from plover_vim.shared.util import addCommandSyntax
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_letter.util import (
        getSymbols, getCharacters
        )
from plover_vim.Josiah_modifier.config import LONGEST_KEY
from plover_vim.Josiah_modifier.defaults import defaults
from plover_vim.Josiah_modifier.util import getPrefixes
from plover_vim.Emily_modifier.util import getEnder, getModifiedChars


class Lookup(BaseLookup):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getLeftCommands(self):
        unique_ender = getEnder(self.opts["unique_ender"])
        # escape = getEscape(self.opts["escape"])
        prefixes = getPrefixes(self.opts["prefixes"])
        symbols = getSymbols(self.opts['symbols'], self.opts['shifted'])
        characters = getModifiedChars(
                getCharacters(self.opts['spelling'], symbols)
                )
        return (prefixes * unique_ender * characters)

    def getDictionary(self):
        return self.getLeftCommands().map(addCommandSyntax(self.opts["command_suffix"]))

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


lookup = Lookup()
