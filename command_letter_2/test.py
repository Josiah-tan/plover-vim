from command_letter_2.builtins import (
        findLookup2, miscLookup2, commandObjectLookup2
        )
from shared.test.builtins import Test
from shared.util.util import addCommandSyntax


##

# need one for no middle
# need one for cool "replace"

@Test(flhs=findLookup2, frhs=addCommandSyntax)
def findLookupSuccess():
    return (
            ((("HR*ERPBLTDZ",),), ("escape c shift(t) shift(exclam)",)),
            ((("HR*RPBLTDZ",),), ("escape shift(t) shift(exclam)",)),
           )


@Test(flhs=miscLookup2, frhs=addCommandSyntax)
def miscLookupSuccess():
    return (
            ((("KWR-RBTZ",),), ("escape m shift(y)",)),
           )


@Test(flhs=commandObjectLookup2, frhs=addCommandSyntax)
def commandObjectLookup2Success():
    return (
            ((("WBTDZ",),), ("escape c w",)),
            ((("#PEFTDZ",),), ("escape v i p p",)),
            ((("TPUFPBTDZ",),), ("escape equal a f",)),
           )

##


def testAll():
    findLookupSuccess()
    miscLookupSuccess()
    commandObjectLookup2Success()

##

