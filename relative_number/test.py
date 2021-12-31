from .main import lookup, Config
# from shared.test.builtins import testFunction  # this works (when run as a module from a script in the root directory)!

##
VERBOSE = True
ASSERTION = False


class Test:
    def __init__(self, mode="universal"):
        self.mode = mode

    def universal(self):
        lhs, rhs = self.func()
        if VERBOSE:
            print(f"testing: {self.func.__qualname__}")
            print(f"lhs: {lhs}")
            print(f"rhs: {rhs}")
        if ASSERTION:
            assert lookup(lhs) == rhs

    def __call__(self, func):
        self.func = func
        if self.mode == "universal":
            return self.universal


##


@Test()
def testSingleDigitDown():
    return f"7{Config.DOWN}", f"{{#down{' down' * 6}}}"


@Test()
def testSingleDigitUp():
    return f"2{Config.UP}", "{{#up up}}"


@Test()
def testMultipleDigit():
    return f"1-6{Config.UP}", f"{{#up{' up' * 15}}}"


##


@Test()
def testReverseDown():
    return f"1EU{Config.DOWN}7", f"{{#down{' down' * 70}}}"


##


def testAll():
    testSingleDigitDown()
    testSingleDigitUp()
    testMultipleDigit()
    testReverseDown()


##

if __name__ == "__main__":
    testAll()
