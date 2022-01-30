from josiah_modifier.builtins import lookup
from shared.test.builtins import Test
from shared.util.util import addCommandSyntax


##


@Test(flhs=lookup, frhs=addCommandSyntax)
def lookupSuccess():
    return (
            ((("KPR*FLTZ",),), ("control(shift(asciicircum))",)),
            ((("KPR*FRLTZ",),), ("control(shift(asciicircum))",)),
           )


# @Test(flhs=lookup)
# def lookupFailure():
#     return (
#             ((("KWR-RBTZ",),), KeyError),
#            )


@Test(flhs=lookup, frhs=addCommandSyntax)
def lookupSuccessControlJ():
    return (
            ((("K3R*6R89Z",),), ("control(j) control(shift(asciicircum))",)),
            ((("K3R*689Z",),), ("control(j) control(shift(asciicircum))",)),
           )


@Test(flhs=lookup, frhs=addCommandSyntax)
def lookupSuccessSplits():
    return (
            ((("OEULTZ",),), ("control(w) o",)),
            ((("SREULTZ",),), ("control(w) v",)),
           )

@Test(flhs=lookup, frhs=addCommandSyntax)
def lookupSuccessTmux():
    return (
            ((("HRULTZ",),), ("control(b) l",)),
            ((("WULTZ",),), ("control(b) w",)),
           )


def testAll():
    lookupSuccess()
#     lookupFailure()
    lookupSuccessControlJ()
    lookupSuccessSplits()
    lookupSuccessTmux()
