
class Config:
    # Length of the longest supported key (number of strokes).
    LONGEST_KEY = 1

    UP = "B"
    DOWN = "-R"


# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
    assert len(key) <= Config.LONGEST_KEY
    raise KeyError
