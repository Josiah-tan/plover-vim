import copy
from plover_vim.shared.util import recursiveUpdate


class RecursiveUpdate:
    def update(self, opts={}):
        if opts.get("disable_defaults"):
            self.opts = opts
        elif opts:
            recursiveUpdate(self.opts, opts)

    def __init__(self, defaults, opts={}):
        self.opts = copy.deepcopy(defaults)  # ensure defaults not changed
        self.update(opts)


class BaseLookup(RecursiveUpdate):
    def generateJson(self):
        self.dictionary.print_items()

    def __call__(self, chord):
        res = self.dictionary.lookup_tuple(chord)
        if res:
            return res
        else:
            raise KeyError


def containsNumber(stroke):
    return any(k.isnumeric() for k in stroke)


steno_order = "#STKPWHRAO*EUFRPBLGTSDZ"
steno_order_numbers = "#12K3W4R50*EU6R7B8G9SDZ"
vowels = {"A", "O", "*", "E", "U"}

