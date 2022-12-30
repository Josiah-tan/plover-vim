from plover_vim.shared.util import addCommandSyntax
from plover_vim.shared.builtins import BaseLookup
from plover_vim.command_letter_2.defaults import defaults
from plover_vim.command_letter_2.config import LONGEST_KEY
from plover_vim.command_letter.util import (
        getEnders, getSymbols
        )
from plover_vim.command_letter_2.util import (
        getMods, getEscape, getObjects,
        getMiddles, getSystems,
        cleanWhiteSpace, applyFormat
        )


class SingleStrokeLeft:
    def getLeftCommands(self):
        mods = getMods(system["mods"] for system in self.opts["systems"])
        enders = getEnders(system["unique_ender"] for system in self.opts["systems"])
        systems = getSystems(mods, enders)
        escape = getEscape(self.opts["escape"])
        symbols = getSymbols(self.opts['symbols'], self.opts['shifted'])
        # characters = getCasedCharacters(getCharacters(self.opts['spelling'], symbols))
        objects = getObjects(self.opts['spelling'], symbols)
        middles = getMiddles(self.opts['middles'])
        return cleanWhiteSpace(
                applyFormat(systems, [escape, middles, objects])
                )
        # return (escape * systems * characters)


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


findLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "#E": "shift(t)",  # "#" to denote go to just before the letter
        "#U": "t",  
        "E": "shift(f)",    # E (because it is more to the left)
        "U": "f",    # U (because it is more to the right)
        },  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-LTDZ",
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                # "-FPB": "",  # left empty for you to customise!
                # "-FP": "",
                # "-FB": "",
                # "-PB": "",
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "<escape> <middles> <objects>",
                # "": ""  # for normal commands (done in josiah-modifers)
                }
            }]
        })


miscLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    # "middles": {},  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-TZ",
            "mods": {  # 64 total possibilities from #EURPB
                "-FPB": "<escape> q <objects>",  # liSten
                "-FP": "<escape> shift(at) <objects>",  # @
                # "-FB": "",
                "-PB": "<escape> z <objects>",  # zeN
                "-F": "<escape> g <objects>",  # the good Spot (primeagen youtube video on the g command)
                "-P": "<escape> r <objects>",
                "-B": "<escape> m <objects>"
                }
            }]
        })


commandObjectLookup2 = Lookup({
    # "disable_defaults": False,
    # # any dictionary entry overiddes the defaults
    # "spelling": {},  # dict: right finger spelling
    # "symbols": {},  # dict: left hand symbols
    # "shifted": {},  # set: any symbols that should be shifted
    "middles": {
        "E": "i",  # physically located closer to keyboard centre
        "EU": "O",  # used in Org mode?
        "U": "a",  # physically localed away from the keyboard centre
        "": ""
        },  # dict: middles
    "escape": "escape",  # default: "escape"
    "systems": [
        {
            "unique_ender": "-TDZ",  # ring finger on T, pinky on DZ
            # some ideas for others if you ever run out: -TZ, -SD, -TDZ, -SDZ, -TSZ, -TSD, or -TSDZ
            "mods": {
                "-FPB": "<escape> equal <middles> <objects>",
                "-FP": "<escape> y s <middles> <objects>",  # coPy Furround
                "-FB": "<escape> c s <objects>",  # Blot Furround
                "-PB": "<escape> g c <middles> objects>",  # commeNt
                "-F": "<escape> v <middles> <objects>",  # Fisualise
                "-P": "<escape> y <middles> <objects>",  # coPy
                "-B": "<escape> c <middles> <objects>",  # Blot
                "": "",

                "#-FPB": "",
                "#-FP": "shift(s) <objects>",
                "#-FB": "<escape> d s <objects>",
                "#-PB": "<escape> g b <middles> <objects>",
                "#-F": "<escape> v <middles> <objects> p",  # visualise and paste!
                "#-P": "",
                "#-B": "",
                "#": ""
                }
            }]
    })
