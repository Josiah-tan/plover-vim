import config
from config import RELOAD
import importlib
import relative_number.test as relative_number_test
import command_letter.test as command_letter_test
import command_object.test as command_object_test
import easy_motion.test as easy_motion_test
import shared.builtins.test as shared_builtins_test
import shared.test.test as shared_test_test
import emily_modifier.test as emily_modifier_test
import josiah_modifier.test as josiah_modifier_test

TEST = [
        shared_test_test,
        shared_builtins_test,
        relative_number_test,
        command_letter_test,
        command_object_test,
        easy_motion_test,
        emily_modifier_test,
        josiah_modifier_test
        ]

importlib.reload(config)

if RELOAD:
    import shared
    import relative_number
    import command_letter
    import command_object
    import easy_motion
    import emily_modifier
    import josiah_modifier

    importlib.reload(shared)
    importlib.reload(relative_number)
    importlib.reload(command_letter)
    importlib.reload(command_object)
    importlib.reload(easy_motion)
    importlib.reload(emily_modifier)
    importlib.reload(josiah_modifier)

for test in TEST:
    test.testAll()
