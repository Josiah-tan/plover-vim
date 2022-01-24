from emily_modifier.builtins import emilyLookup, escapedLookup
from shared.test.builtins import Test
from shared.util.util import addCommandSyntax


##


@Test(flhs=emilyLookup, frhs=addCommandSyntax)
def emilyLookupSuccess():
    return (
            ((("KPR*FLTZ",),), ("control(shift(asciicircum))",)),
            ((("KPR*FRLTZ",),), ("control(shift(asciicircum))",)),
           )


# @Test(flhs=emilyLookup)
# def emilyLookupFailure():
#     return (
#             ((("KWR-RBTZ",),), KeyError),
#            )


@Test(flhs=escapedLookup, frhs=addCommandSyntax)
def escapedLookupSuccess():
    return (
            ((("K3R*6R89Z",),), ("escape control(shift(asciicircum))",)),
            ((("K3R*689Z",),), ("escape control(shift(asciicircum))",)),
           )


# @Test(flhs=escapedLookup)
# def escapedLookupFailure():
#     return (
#             ((("HR*RPBLTDZ",),), KeyError),
#            )
#
# ##
#
#
def testAll():
    emilyLookupSuccess()
#     emilyLookupFailure()
    escapedLookupSuccess()
#     escapedLookupFailure()
#
##

