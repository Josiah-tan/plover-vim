from config import RELOAD


if RELOAD:
    import importlib
    from command_letter_2 import builtins, config, defaults, test, util
    importlib.reload(builtins)
    importlib.reload(config)
    importlib.reload(defaults)
    importlib.reload(test)
    importlib.reload(util)
