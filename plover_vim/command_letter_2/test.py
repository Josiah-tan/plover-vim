import unittest
from plover_vim.command_letter_2.builtins import (
        findLookup2, miscLookup2, commandObjectLookup2
        )


class TestFindLookup2(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(findLookup2(("WRULTDZ",)), '{#escape f u}{plover:clear_trans_state}')
        self.assertEqual(findLookup2(("WR*ULTDZ",)), '{#escape f semicolon}{plover:clear_trans_state}')
        self.assertEqual(findLookup2(("WR*UBLTDZ",)), '{#escape c f semicolon}{plover:clear_trans_state}')
        self.assertEqual(findLookup2(("WR*UPLTDZ",)), '{#escape y f semicolon}{plover:clear_trans_state}')
        self.assertEqual(findLookup2(("WR*UFLTDZ",)), '{#escape v f semicolon}{plover:clear_trans_state}')

class TestMiscLookup2(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(miscLookup2(("KWR-RBTZ",)), '{#escape m shift(y)}{plover:clear_trans_state}')

class TestCommandObjectLookup2(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(commandObjectLookup2(("WBTDZ",)), "{#escape c w}{plover:clear_trans_state}")
        self.assertEqual(commandObjectLookup2(("#PEFTDZ",)), "{#escape v i p p}{plover:clear_trans_state}")
        self.assertEqual(commandObjectLookup2(("TPUFPBTDZ",)), "{#escape equal a f}{plover:clear_trans_state}")

# ##
#
# # need one for no middle
# # need one for cool "replace"
#
# @Test(flhs=findLookup2, frhs=addCommandSyntax)
# def findLookupSuccess():
#     return (
#             ((("HR*ERPBLTDZ",),), ("escape c shift(t) shift(exclam)",)),
#             ((("HR*RPBLTDZ",),), ("escape shift(t) shift(exclam)",)),
#            )
#
#
# @Test(flhs=miscLookup2, frhs=addCommandSyntax)
# def miscLookupSuccess():
#     return (
#             ((("KWR-RBTZ",),), ("escape m shift(y)",)),
#            )
#
#
# @Test(flhs=commandObjectLookup2, frhs=addCommandSyntax)
# def commandObjectLookup2Success():
#     return (
#             ((("WBTDZ",),), ("escape c w",)),
#             ((("#PEFTDZ",),), ("escape v i p p",)),
#             ((("TPUFPBTDZ",),), ("escape equal a f",)),
#            )
#
# ##
#
#
# def testAll():
#     findLookupSuccess()
#     miscLookupSuccess()
#     commandObjectLookup2Success()
#
# ##
#
