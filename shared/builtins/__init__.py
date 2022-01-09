from config import RELOAD
from shared.builtins.builtins import (
        RecursiveUpdate, BaseLookup
        )

if RELOAD:
    import importlib
    from shared.builtins import test, builtins
    importlib.reload(test)
    importlib.reload(builtins)
