from shared.builtins.builtins import containsNumber
from shared.test.builtins import Test


@Test(flhs=containsNumber)
def testContainsNumber():
    return (
            (("hello world",), False),
            (("hello 6world",), True),
            (("1234",), True)
            )


def testAll():
    testContainsNumber()
