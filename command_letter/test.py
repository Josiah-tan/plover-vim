from command_letter.builtins import findLookup, miscLookup
from shared.test.builtins import Test
from shared.util.util import addCommandSyntax


##


@Test(flhs=findLookup, frhs=addCommandSyntax)
def findLookupSuccess():
    return (
            ((("HR*RPBLTDZ",),), ("escape shift(t) shift(exclam)",)),
           )


@Test(flhs=findLookup)
def findLookupFailure():
    return (
            ((("KWR-RBTZ",),), KeyError),
           )


@Test(flhs=miscLookup, frhs=addCommandSyntax)
def miscLookupSuccess():
    return (
            ((("KWR-RBTZ",),), ("escape m shift(y)",)),
           )


@Test(flhs=miscLookup)
def miscLookupFailure():
    return (
            ((("HR*RPBLTDZ",),), KeyError),
           )

##


def testAll():
    findLookupSuccess()
    findLookupFailure()
    miscLookupSuccess()
    miscLookupFailure()

##

