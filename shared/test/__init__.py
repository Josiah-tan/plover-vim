from config import RELOAD

if RELOAD:
    import importlib
    from shared.test import config, builtins
    importlib.reload(config)
    importlib.reload(builtins)
