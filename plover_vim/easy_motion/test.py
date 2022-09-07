import unittest
from plover_vim.easy_motion.builtins import lookup


class TestEasyMotionLookup(unittest.TestCase):
    def test_success(self):
        self.assertEqual(lookup(("STKPW-FBLTDZ", "STKPW-B")), "{#z b}{^}")
        self.assertEqual(lookup(("SKP*FBLTDZ",)), '{#escape space space f shift(ampersand)}{^}')

if __name__ == "__main__":
    unittest.main()
