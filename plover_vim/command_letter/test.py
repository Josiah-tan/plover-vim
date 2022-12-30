import unittest
from plover_vim.command_letter.builtins import findLookup, miscLookup


class TestFindLookup(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(findLookup(("HR*RPBLTDZ",)), '{#escape shift(t) shift(exclam)}{plover:clear_trans_state}')
    
    def test_lookup_failure(self):
        with self.assertRaises(KeyError):
            findLookup(("KWR-RBTZ",))

class TestMiscLookup(unittest.TestCase):
    def test_lookup_success(self):
        self.assertEqual(miscLookup(("KWR-RBTZ",)), '{#escape m shift(y)}{plover:clear_trans_state}')
    
    def test_lookup_failure(self):
        with self.assertRaises(KeyError):
            miscLookup(("HR*RPBLTDZ",))


if __name__ == "__main__":
    unittest.main()
