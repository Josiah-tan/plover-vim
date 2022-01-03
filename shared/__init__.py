from config import RELOAD

if RELOAD:
    import importlib
    from shared import builtins, test
    importlib.reload(builtins)
    importlib.reload(test)
