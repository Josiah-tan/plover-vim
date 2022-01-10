from easy_motion.builtins import lookup
from shared.test.builtins import Test
from shared.util.util import addCommandSyntax


##


@Test(flhs=lookup, frhs=addCommandSyntax)
def findLetterLookupSuccess():
    return (
            ((("STKPW-FBLTDZ", "STKPW-B"),), ("z b",)),
           )


@Test(flhs=lookup, frhs=addCommandSyntax)
def findLetterLookupInitialSuccess():
    return (
            ((("SKP*FBLTDZ",),), ("escape space space f shift(ampersand)",)),
           )


##


def testAll():
    findLetterLookupSuccess()
    findLetterLookupInitialSuccess()

##


if __name__ == '__main__':
    testAll()
