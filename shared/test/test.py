from shared.test.builtins import Test


def testAdder(*args):
    return sum(args)


def testMultiplier(*args):
    i = 1
    for a in args:
        i *= a
    return i


def raiseKeyError(*args):
    raise KeyError


@Test(flhs=testAdder)
def testNoError():
    return (
            ((1, 2, 3), 6),
            ((1, 5, -7), -1),
            )


@Test(flhs=raiseKeyError)
def testRaiseKeyError():
    return (
            ((1, 2, 3), KeyError),
            ((1, 5, -7), KeyError)
            )


@Test(flhs=testAdder, frhs=testMultiplier)
def testLhsRhs():
    return (
            ((1, 2, 3), (2, 3)),
            ((1, 5, -7), (-1, 1, 1))
            )


def testAll():
    testNoError()
    testRaiseKeyError()
    testLhsRhs()
