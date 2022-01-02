from config import Global

if Global.RELOAD:
    import importlib
    from relative_number import test, main
    importlib.reload(test)
    importlib.reload(main)
