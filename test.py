import relative_number.test as relative_number_test

RELOAD = True
TEST = {"relative_number"}

if RELOAD:
    import relative_number

    import importlib
    importlib.reload(relative_number)
    importlib.reload(relative_number_test)

if "relative_number" in TEST:
    relative_number_test.testAll()
