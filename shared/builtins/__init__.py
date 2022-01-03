from config import RELOAD

if RELOAD:
    import importlib
    from shared.builtins import test, builtins
    importlib.reload(test)
    importlib.reload(builtins)
