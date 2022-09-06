import unittest
from plover_vim.command_object.util import mergeDictList


##

class TestMergeDictLists(unittest.TestCase):
    def test_success(self):
        a1 = {"-P": ["", "", "", "P"]}
        b1 = {"-P": "grave"}
        b2 = {"-P": ["grave"]}
        b3 = {"-P": ['', "grave"]}
        c1 = {'-P': ['grave', '', '', 'P']}
        c2 = {'-P': ['grave', '', '', 'P']}
        c3 = {'-P': ['', 'grave', '', 'P']}
        self.assertEqual(mergeDictList(a1, b1), c1)
        self.assertEqual(mergeDictList(a1, b2), c2)
        self.assertEqual(mergeDictList(a1, b3), c3)

    def test_failure(self):
        a1 = {"-P": ["P", "", "", "P"]}
        b1 = {"-P": "grave"}
        c1 = {'-P': ['grave', '', '', 'P']}
        self.assertEqual(mergeDictList(a1, b1), c1)

if __name__ == "__main__":
    unittest.main()


        

# @Test(flhs=mergeDictList)
# def mergeDictListsSuccess():
#     a1 = {"-P": ["", "", "", "P"]}
#     b1 = {"-P": "grave"}
#     b2 = {"-P": ["grave"]}
#     b3 = {"-P": ['', "grave"]}
#     c1 = {'-P': ['grave', '', '', 'P']}
#     c2 = {'-P': ['grave', '', '', 'P']}
#     c3 = {'-P': ['', 'grave', '', 'P']}
#     return (
#             ((a1, b1,), c1),
#             ((a1, b2,), c2),
#             ((a1, b3,), c3),
#            )
#
#
# @Test(flhs=mergeDictList)
# def mergeDictListsFailure():
#     a1 = {"-P": ["P", "", "", "P"]}
#     b1 = {"-P": "grave"}
#     c1 = {'-P': ['grave', '', '', 'P']}
#     return (
#             ((a1, b1,), c1),
#            )

# @Test(flhs=findLookup, frhs=addCommandSyntax)
# def findLookupSuccess():
#     return (
#             ((("HR*RPBLTDZ",),), ("escape shift(t) shift(exclam)",)),
#            )
#
#
# @Test(flhs=findLookup)
# def findLookupFailure():
#     return (
#             ((("KWR-RBTZ",),), KeyError),
#            )
#
#
# @Test(flhs=miscLookup, frhs=addCommandSyntax)
# def miscLookupSuccess():
#     return (
#             ((("KWR-RBTZ",),), ("escape m shift(y)",)),
#            )
#
#
# @Test(flhs=miscLookup)
# deuf miscLookupFailure():
#     return (
#             ((("HR*RPBLTDZ",),), KeyError),
#            )
#
##


# def testAll():
#     mergeDictListsSuccess()
#     mergeDictListsFailure()
    # findLookupSuccess()
    # findLookupFailure()
    # miscLookupSuccess()
    # miscLookupFailure()

##

