from config import RELOAD

if RELOAD:
    import importlib
    from shared import builtins, test, util
    importlib.reload(builtins)
    importlib.reload(test)
    importlib.reload(util)
