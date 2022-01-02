from config import Global

if Global.RELOAD:
    import importlib
    from shared import builtins, test
    importlib.reload(builtins)
    importlib.reload(test)
