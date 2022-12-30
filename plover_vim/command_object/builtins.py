from plover_vim.shared.util import getMods, addCommandSyntax
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_object.defaults import defaults
from plover_vim.command_object.config import LONGEST_KEY
from plover_vim.command_object.util import (
        getStarters, combineModsStarters,
        getEscape, getMiddles, getSymbols
        )


class SingleStrokeRight:
    def getRightCommands(self):
        mods = getMods(system["mods"] for system in self.opts["systems"])
        starters = getStarters(system["unique_starter"] for system in self.opts["systems"])
        systems = combineModsStarters(mods, starters)
        escape = getEscape(self.opts["escape"])
        middles = getMiddles(self.opts['middles'])
        symbols = getSymbols(self.opts['symbols'], self.opts['objects'], self.opts['shifted'])
        # characters = getCasedCharacters(getCharacters(self.opts['spelling'], symbols))
        return (escape * systems * middles * symbols)


class Lookup(BaseLookup, SingleStrokeRight):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self):
        return self.getRightCommands().map(addCommandSyntax(self.opts["command_suffix"]))

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


lookup = Lookup()
