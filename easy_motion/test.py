from easy_motion.builtins import findLetterLookup
from shared.test.builtins import Test


##


@Test(flhs=findLetterLookup)
def findLetterLookupSuccess():
    return (
            ((("STKPW-FBLTDZ", "STKPW-B"),), "{#z b}"),
           )


@Test(flhs=findLetterLookup)
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
