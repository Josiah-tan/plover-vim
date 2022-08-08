from relative_number.builtins import Lookup, RelativeNumberLookup
from shared.test.builtins import Test
# from vim import relative_number

relative_number_lookup = RelativeNumberLookup()


def testLookup(chord, down, up):
    # this is just there for compatibility with the old version
    return Lookup({"up": up, "down": down})(chord)

##

@Test(flhs=relative_number_lookup)
def testClock():
    return(
            ((("4-BG",),), "4:00"),
            ((("1UBG",),), "11:00"),
            ((("12UBG",),), "21:00"),
            ((("13BG",),), "13:00"),
            )


@Test(flhs=relative_number_lookup)
def testZerosPinky():
    return(
            ((("4-S",),), "40"),
            ((("14-SZ",),), "1400"),
            ((("1234-78Z",),), "123489000"),
            ((("3-9S",),), "30000"),
            ((("4-79SDZ",),), "4800000"),
            ((("5DZ",),), "5000000"),
            ((("789",),), "890000000"),
            ((("U69D",),), "7700000000"),
            ((("340U7D",),), "8643000000000"),
            )


@Test(flhs=relative_number_lookup)
def relativeNumber():
    return (
            ((("1-6B",),), f"{{#up{' up' * 16}}}"),
            ((("1-6R",),), f"{{#down{' down' * 16}}}"),
            ((("4U6R",),), f"{{#down{' down' * 73}}}"),
            ((("1-RS",),), f"{{#down{' down' * 9}}}"),
            ((("2-RS",),), f"{{#down{' down' * 19}}}"),
            )

@Test(flhs=relative_number_lookup)
def doubleUNumber():
    return (
            ((("4U",),), "44"),
            ((("U6",),), "77"),
            )
    
    
@Test(flhs=relative_number_lookup)
def normalNumber():
    return (
            ((("1340",),), "1346"),
            ((("123478",),), "123489"),
            )


@Test(flhs=relative_number_lookup)
def reverseUNumber():
    return (
            ((("1340U",),), "6431"),
            ((("1234U78",),), "984321"),
           )

##

@Test(flhs=testLookup)
def singleDigitDown():
    return (
            ((("-R7",), "-R", "-B"), f"{{#down{' down' * 6}}}"),
           )


@Test(flhs=testLookup)
def singleDigitUp():
    return (
            ((("2B",), "-R", "-B"), "{#up up}"),
            ((("5B",), "-R", "-B"), "{#up up up up up}"),
           )


@Test(flhs=testLookup)
def multipleDigit():
    return (
            ((("1-6B",), "-R", "-B"), f"{{#up{' up' * 15}}}"),
            ((("1R-6",), "R", "-B"), f"{{#down{' down' * 15}}}"),
           )


@Test(flhs=testLookup)
def reverseDown():
    return (
            ((("1EUR7",), "-R", "-B"), f"{{#down{' down' * 70}}}"),
           )


@Test(flhs=testLookup)
def repeatDigit():
    return (
            ((("-R7D",), "-R", "-B"), f"{{#down{' down' * 76}}}"),
            ((("3-BD",), "-R", "-B"), f"{{#up{' up' * 32}}}"),
           )


##


@Test(flhs=testLookup)
def tooManyNumbers():
    return (
            ((("10R789",), "-R", "-B"), KeyError),
           )


@Test(flhs=testLookup)
def incorrectChord():
    return (
            ((("1R-6",), "-R", "-B"), KeyError),
            ((("1-RB8",), "-R", "-B"), KeyError),
           )


@Test(flhs=testLookup)
def zeroes():
    return (
            ((("0R",), "-R", "-B"), KeyError),
            ((("0B",), "-R", "-B"), KeyError),
           )


@Test(flhs=testLookup)
def tooManyRepeatDigit():
    return (
            ((("14-RD",), "-R", "-B"), KeyError),
           )


@Test(flhs=testLookup)
def asterisk():
    return (
            ((("14*R",), "-R", "-B"), KeyError),
           )


##

def testRelativeNumber():
    testClock()
    testZerosPinky()
    relativeNumber()
    doubleUNumber()
    normalNumber()
    reverseUNumber()

def testNoErrorsRelativeDeprecated():
    singleDigitDown()
    singleDigitUp()
    multipleDigit()
    reverseDown()
    repeatDigit()


def testKeyErrorRelativeDeprecated():
    tooManyNumbers()
    incorrectChord()
    zeroes()
    tooManyRepeatDigit()
    asterisk()


def testAll():
    testRelativeNumber()
    testNoErrorsRelativeDeprecated()
    testKeyErrorRelativeDeprecated()

##


if __name__ == "__main__":
    testAll()

