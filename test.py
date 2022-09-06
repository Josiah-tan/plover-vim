import config
from config import RELOAD
import importlib
import command_letter.test as command_letter_test
import command_object.test as command_object_test
import easy_motion.test as easy_motion_test
import emily_modifier.test as emily_modifier_test
import josiah_modifier.test as josiah_modifier_test
import command_letter_2.test as command_letter_2_test

TEST = [
        command_letter_test,
        command_object_test,
        easy_motion_test,
        emily_modifier_test,
        josiah_modifier_test,
        command_letter_2_test
        ]

importlib.reload(config)

if RELOAD:
    import command_letter
    import command_object
    import easy_motion
    import emily_modifier
    import josiah_modifier
    import command_letter_2

    importlib.reload(command_letter)
    importlib.reload(command_object)
    importlib.reload(easy_motion)
    importlib.reload(emily_modifier)
    importlib.reload(josiah_modifier)
    importlib.reload(command_letter_2)

for test in TEST:
    test.testAll()
