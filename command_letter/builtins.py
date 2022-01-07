from shared.builtins import RecursiveUpdate
from command_letter.defaults import defaults
from command_letter.config import LONGEST_KEY
from command_letter.util import (
        getMods, getEnders, combineModsEnders,
        getEscape, getSymbols, getCharacters,
        getCasedCharacters, addCommandSyntax
        )


class Lookup(RecursiveUpdate):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self):
        mods = getMods(system["mods"] for system in self.opts["systems"])
        enders = getEnders(system["unique_ender"] for system in self.opts["systems"])
        systems = combineModsEnders(mods, enders)
        escape = getEscape(self.opts["escape"])
        symbols = getSymbols(self.opts['symbols'], self.opts['shifted'])
        characters = getCasedCharacters(getCharacters(self.opts['spelling'], symbols))
        return (escape * systems * characters).map(addCommandSyntax)

    def generateJson(self):
        self.dictionary.print_items()

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return self.dictionary.lookup_tuple(chord)
