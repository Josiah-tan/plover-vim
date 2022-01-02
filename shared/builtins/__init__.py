from config import Global

if Global.RELOAD:
    import importlib
    from shared.builtins import test, builtins
    importlib.reload(test)
    importlib.reload(builtins)
