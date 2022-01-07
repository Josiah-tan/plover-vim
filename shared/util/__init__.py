from config import RELOAD
from shared.util.util import recursiveUpdate

if RELOAD:
    import importlib
    from shared.util import test, util
    importlib.reload(test)
    importlib.reload(util)
