from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.Josiah_modifier.builtins import lookup as JosiahLookup

LONGEST_KEY = 1


def lookup(key):
    for look in [JosiahLookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    JosiahLookup.generateJson()
