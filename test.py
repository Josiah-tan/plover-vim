import config
from config import Global
import importlib
import relative_number.test as relative_number_test
import shared.builtins.test as shared_builtins_test
import shared.test.test as shared_test_test

TEST = {
        relative_number_test,
        shared_builtins_test,
        shared_test_test,
        }

importlib.reload(config)

if Global.RELOAD:
    import shared
    import relative_number

    importlib.reload(shared)
    importlib.reload(relative_number)

for test in TEST:
    test.testAll()



