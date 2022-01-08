from easy_motion.builtins import lookup
from shared.test.builtins import Test


##


@Test(flhs=lookup)
def findLetterLookupSuccess():
    return (
            ((("STKPW-FBLTDZ", "STKPW-B"),), "{#z b}"),
           )


@Test(flhs=lookup)
def findLetterLookupInitialSuccess():
    return (
            ((("SKP*FBLTDZ",),), "{#escape space space f shift(ampersand)}"),
           )


##


def testAll():
    findLetterLookupSuccess()
    findLetterLookupInitialSuccess()

##


testAll()
