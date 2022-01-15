from contextlib import suppress
import sys
import platform

linux_repository_location = "/home/josiah/.dotfiles/plover/.config/plover/vim"
windows_repository_location = "c:\\users\\josia\\appdata\\local\\plover\\plover\\vim"
on_wind = "windows" in platform.uname()[0].lower()
if on_wind:
    repository_location = windows_repository_location
else:
    repository_location = linux_repository_location

sys.path.append(repository_location)

# import the modules that you want for your python experience here
from command_letter.builtins import findLookup, miscLookup
from command_object.builtins import lookup as command_object_lookup
from relative_number.builtins import lookup as relative_number_lookup

LONGEST_KEY = 1


def lookup(key):
    for look in [
            findLookup,
            miscLookup,
            command_object_lookup,
            relative_number_lookup
            ]:
        with suppress(KeyError):
            return look(key)
