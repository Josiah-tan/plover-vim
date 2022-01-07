from shared.util import recursiveUpdate


class RecursiveUpdate:
    def update(self, opts={}):
        if opts.get("disable_defaults"):
            self.opts = opts
        if opts:
            recursiveUpdate(self.opts, opts)

    def __init__(self, defaults, opts={}):
        self.opts = defaults
        self.update(opts)


def containsNumber(stroke):
    return any(k.isnumeric() for k in stroke)


steno_order = "#STKPWHRAO*EUFRPBLGTSDZ"
steno_order_numbers = "#12K3W4R50*EU6R7B8G9SDZ"
vowels = {"A", "O", "*", "E", "U"}
