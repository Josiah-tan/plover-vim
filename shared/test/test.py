from shared.test.builtins import Test


def testAdder(*args):
    return sum(args)


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


def testAll():
    testNoError()
    testRaiseKeyError()
