import unittest
from plover_vim.command_letter.builtins import findLookup, miscLookup


class TestFindLookup(unittest.TestCase):
    def test_find_lookup_success(self):
        self.assertEqual(findLookup(("HR*RPBLTDZ",)), '{#escape shift(t) shift(exclam)}{^}')
    
    def test_find_lookup_failure(self):
        with self.assertRaises(KeyError):
            findLookup(("KWR-RBTZ",))

    def test_misc_lookup_success(self):
        self.assertEqual(miscLookup(("KWR-RBTZ",)), '{#escape m shift(y)}{^}')
    
    def test_misc_lookup_failure(self):
        with self.assertRaises(KeyError):
            miscLookup(("HR*RPBLTDZ",))


if __name__ == "__main__":
    unittest.main()
