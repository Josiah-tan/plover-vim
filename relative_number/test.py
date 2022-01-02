from relative_number.main import testLookup
# import relative_number.globals as Config
from shared.test.builtins import Test


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


def testNoErrors():
    singleDigitDown()
    singleDigitUp()
    multipleDigit()
    reverseDown()


def testKeyError():
    tooManyNumbers()
    incorrectChord()


def testAll():
    testNoErrors()
    testKeyError()

##


if __name__ == "__main__":
    testAll()

##


