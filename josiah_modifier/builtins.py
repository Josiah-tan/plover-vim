from shared.util.util import addCommandSyntax
from shared.builtins import BaseLookup
from command_letter.util import (
        getSymbols, getCharacters
        )
from josiah_modifier.config import LONGEST_KEY
from josiah_modifier.defaults import defaults
from josiah_modifier.util import getPrefixes
from emily_modifier.util import getEnder, getModifiedChars


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
        return self.getLeftCommands().map(addCommandSyntax)

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


lookup = Lookup()
