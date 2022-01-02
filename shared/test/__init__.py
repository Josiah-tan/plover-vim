from config import Global

if Global.RELOAD:
    import importlib
    from shared.test import config, builtins
    importlib.reload(config)
    importlib.reload(builtins)
