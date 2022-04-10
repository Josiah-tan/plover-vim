from contextlib import suppress
# change this to be the location of where you installed this respository
import sys
import os.path

# note that this assumes that you cloned this repository with the name "vim" in your config files, feel free to change this though!
from plover.oslayer.config import CONFIG_DIR
repository_location = os.path.join(CONFIG_DIR, "vim")
sys.path.append(repository_location)

# import the modules that you want for your vim experience here
from emily_modifier.builtins import emilyLookup, escapedLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [emilyLookup, escapedLookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    emilyLookup.generateJson()
    # escapedLookup.generateJson()
