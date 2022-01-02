from relative_number.main import testLookup
import relative_number.globals as Config
from shared.test.builtins import Test


##


@Test(flhs=testLookup)
def testSingleDigitDown():
    return (
            ((("-7R",), "-R", "B"), f"{{#down{' down' * 6}}}"),
           )


@Test(flhs=testLookup)
def testSingleDigitUp():
    return (
            ((("2B",), "-R", "B"), "{#up up}"),
           )


@Test(flhs=testLookup)
def testMultipleDigit():
    return (f"1-6{Config.UP}",), f"{{#up{' up' * 15}}}"


@Test(flhs=testLookup)
def testReverseDown():
    return (f"1EU{Config.DOWN}7",), f"{{#down{' down' * 70}}}"

##


def testAll():
    testSingleDigitDown()
    testSingleDigitUp()
    # testMultipleDigit()
    # testReverseDown()
##

if __name__ == "__main__":
    testAll()
