from shared.builtins import RecursiveUpdate
from command_object.defaults import defaults
from command_object.config import LONGEST_KEY
from command_object.util import (
        getMods, getStarters, combineModsStarters,
        getEscape, getMiddle, getSymbols,
        addCommandSyntax
        )


class SingleStrokeRight:
    def getRightCommands(self):
        mods = getMods(system["mods"] for system in self.opts["systems"])
        starters = getStarters(system["unique_starter"] for system in self.opts["systems"])
        systems = combineModsStarters(mods, starters)
        escape = getEscape(self.opts["escape"])
        middle = getMiddle(self.opts['middle'])
        symbols = getSymbols(self.opts['symbols'], self.opts['objects'], self.opts['shifted'])
        # characters = getCasedCharacters(getCharacters(self.opts['spelling'], symbols))
        return (escape * systems * middle * symbols)


class Lookup(RecursiveUpdate, SingleStrokeRight):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self):
        return self.getRightCommands().map(addCommandSyntax)

    def generateJson(self):
        self.dictionary.print_items()

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return self.dictionary.lookup_tuple(chord)


lookup = Lookup()
