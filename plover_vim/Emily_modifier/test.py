import unittest
from plover_vim.Emily_modifier.builtins import EmilyLookup, escapedLookup
# from shared.test.builtins import Test
# from shared.util.util import addCommandSyntax


##

class TestEmilyLookup(unittest.TestCase):
    def test_success(self):
        self.assertEqual(EmilyLookup(("KPR*FLTZ",)), "{#control(shift(asciicircum))}{plover:clear_trans_state}")
        self.assertEqual(EmilyLookup(("KPR*FRLTZ",)), "{#control(shift(asciicircum))}{plover:clear_trans_state}")

class TestEscapedLookup(unittest.TestCase):
    def test_success(self):
        self.assertEqual(escapedLookup(("K3R*6R89Z",)), "{#escape control(shift(asciicircum))}{plover:clear_trans_state}")
        self.assertEqual(escapedLookup(("K3R*689Z",)), "{#escape control(shift(asciicircum))}{plover:clear_trans_state}")

if __name__ == "__main__":
    unittest.main()


# @Test(flhs=emilyLookup, frhs=addCommandSyntax)
# def emilyLookupSuccess():
#     return (
#             ((("KPR*FLTZ",),), ("control(shift(asciicircum))",)),
#             ((("KPR*FRLTZ",),), ("control(shift(asciicircum))",)),
#            )


# @Test(flhs=emilyLookup)
# def emilyLookupFailure():
#     return (
#             ((("KWR-RBTZ",),), KeyError),
#            )


# @Test(flhs=escapedLookup, frhs=addCommandSyntax)
# def escapedLookupSuccess():
#     return (
#             ((("K3R*6R89Z",),), ("escape control(shift(asciicircum))",)),
#             ((("K3R*689Z",),), ("escape control(shift(asciicircum))",)),
#            )


# @Test(flhs=escapedLookup)
# def escapedLookupFailure():
#     return (
#             ((("HR*RPBLTDZ",),), KeyError),
#            )
#
# ##
#
#
# def testAll():
#     emilyLookupSuccess()
# #     emilyLookupFailure()
#     escapedLookupSuccess()
# #     escapedLookupFailure()
# #
# ##
#
