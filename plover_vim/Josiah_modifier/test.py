import unittest
from plover_vim.Josiah_modifier.builtins import lookup

##

class TestJosiahModifierLookup(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(lookup(("KPR*FLTZ",)), "{#control(shift(asciicircum))}{plover:clear_trans_state}")
        self.assertEqual(lookup(("KPR*FRLTZ",)), "{#control(shift(asciicircum))}{plover:clear_trans_state}")
    
    def test_lookup_success_control_J(self):
        self.assertEqual(lookup(("K3R*6R89Z",)), "{#control(j) control(shift(asciicircum))}{plover:clear_trans_state}")
        self.assertEqual(lookup(("K3R*689Z",)), "{#control(j) control(shift(asciicircum))}{plover:clear_trans_state}")

    def test_lookup_success_splits(self):
        self.assertEqual(lookup(("OEULTZ",)), "{#control(j) control(w) o}{plover:clear_trans_state}")
        self.assertEqual(lookup(("SREULTZ",)), "{#control(j) control(w) v}{plover:clear_trans_state}")
    
    def test_lookup_success_tmux(self):
        self.assertEqual(lookup(("HRULTZ",)), "{#control(b) l}{plover:clear_trans_state}")
        self.assertEqual(lookup(("WULTZ",)), "{#control(b) w}{plover:clear_trans_state}")


# @Test(flhs=lookup, frhs=addCommandSyntax)
# def lookupSuccess():
#     return (
#             ((("KPR*FLTZ",),), ("control(shift(asciicircum))",)),
#             ((("KPR*FRLTZ",),), ("control(shift(asciicircum))",)),
#            )


# @Test(flhs=lookup)
# def lookupFailure():
#     return (
#             ((("KWR-RBTZ",),), KeyError),
#            )


# @Test(flhs=lookup, frhs=addCommandSyntax)
# def lookupSuccessControlJ():
#     return (
#             ((("K3R*6R89Z",),), ("control(j) control(shift(asciicircum))",)),
#             ((("K3R*689Z",),), ("control(j) control(shift(asciicircum))",)),
#            )


# @Test(flhs=lookup, frhs=addCommandSyntax)
# def lookupSuccessSplits():
#     return (
#             ((("OEULTZ",),), ("control(j) control(w) o",)),
#             ((("SREULTZ",),), ("control(j) control(w) v",)),
#            )


# @Test(flhs=lookup, frhs=addCommandSyntax)
# def lookupSuccessTmux():
#     return (
#             ((("HRULTZ",),), ("control(b) l",)),
#             ((("WULTZ",),), ("control(b) w",)),
#            )


# def testAll():
#     lookupSuccess()
# #     lookupFailure()
#     lookupSuccessControlJ()
#     lookupSuccessSplits()
#     lookupSuccessTmux()
