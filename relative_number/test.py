from relative_number.builtins import Lookup
from shared.test.builtins import Test


def testLookup(chord, down, up):
    return Lookup({"up": up, "down": down})(chord)

##


@Test(flhs=testLookup)
def singleDigitDown():
    return (
            ((("-7R",), "-R", "B"), f"{{#down{' down' * 6}}}"),
           )


@Test(flhs=testLookup)
def singleDigitUp():
    return (
            ((("2B",), "-R", "B"), "{#up up}"),
            ((("5B",), "-R", "B"), "{#up up up up up}"),
           )


@Test(flhs=testLookup)
def multipleDigit():
    return (
            ((("1-6B",), "-R", "B"), f"{{#up{' up' * 15}}}"),
            ((("1R-6",), "R", "B"), f"{{#down{' down' * 15}}}"),
           )


@Test(flhs=testLookup)
def reverseDown():
    return (
            ((("1EUR7",), "-R", "B"), f"{{#down{' down' * 70}}}"),
           )


@Test(flhs=testLookup)
def repeatDigit():
    return (
            ((("-R7D",), "-R", "B"), f"{{#down{' down' * 76}}}"),
            ((("3-BD",), "-R", "B"), f"{{#up{' up' * 32}}}"),
           )


##


@Test(flhs=testLookup)
def tooManyNumbers():
    return (
            ((("10R789",), "-R", "B"), KeyError),
           )


@Test(flhs=testLookup)
def incorrectChord():
    return (
            ((("1R-6",), "-R", "B"), KeyError),
            ((("1-RB8",), "-R", "B"), KeyError),
           )


@Test(flhs=testLookup)
def zeroes():
    return (
            ((("0R",), "-R", "B"), KeyError),
            ((("0B",), "-R", "B"), KeyError),
           )


@Test(flhs=testLookup)
def tooManyRepeatDigit():
    return (
            ((("14-RD",), "-R", "B"), KeyError),
           )


##


def testNoErrors():
    singleDigitDown()
    singleDigitUp()
    multipleDigit()
    reverseDown()
    repeatDigit()


def testKeyError():
    tooManyNumbers()
    incorrectChord()
    zeroes()
    tooManyRepeatDigit()


def testAll():
    testNoErrors()
    testKeyError()

##


if __name__ == "__main__":
    testAll()

##
