from plover_vim.shared.util import getMods, addCommandSyntax
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_letter.defaults import (
        defaults  # , spelling , symbols, shifted_symbols_aus
        )
from plover_vim.command_letter.config import LONGEST_KEY
from plover_vim.command_letter.util import (
        getEnders, combineModsEnders,
        getEscape, getSymbols, getCharacters,
        getCasedCharacters
        )


class SingleStrokeLeft:
    def getLeftCommands(self):
        mods = getMods(system["mods"] for system in self.opts["systems"])
        enders = getEnders(system["unique_ender"] for system in self.opts["systems"])
        systems = combineModsEnders(mods, enders)
        escape = getEscape(self.opts["escape"])
        symbols = getSymbols(self.opts['symbols'], self.opts['shifted'])
        characters = getCasedCharacters(getCharacters(self.opts['spelling'], symbols))
        return (escape * systems * characters)


class Lookup(BaseLookup, SingleStrokeLeft):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self):
        return self.getLeftCommands().map(addCommandSyntax(self.opts["command_suffix"]))

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)


findLookup = Lookup({
    # "disable_defaults": True,
    # "spelling": spelling,
    # "symbols": symbols,
    # "shifted": shifted_symbols_aus,
    "escape": "escape",
    "systems": [
        {
            "unique_ender": "LTDZ",
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",  #
                # "-FB": "space space f",  # Forward Back (moving this to another module)
                "-PB": "shift(t)",  # Previous Backwards
                "-F": "f",  # Forwards
                "-P": "t",  # Previous
                "-B": "shift(f)",  # Backwards
                "": ""  # for normal commands
                }
            }
        ]
    })


miscLookup = Lookup({
    # "disable_defaults": True,
    # "spelling": spelling,
    # "symbols": symbols,
    # "shifted": shifted_symbols_aus,
    "escape": "escape",
    "systems": [
        {
            "unique_ender": "-TZ",
            "mods": {
                "-FPB": "q",  # liSten
                "-FP": "shift(at)",  # at
                # "-FB": "",
                "-PB": "z",  # zeN
                "-F": "g",  # the good Spot (primeagen youtube video on the g command)
                # "-P": "",
                "-B": "m"
                }
            }
        ]
   })
