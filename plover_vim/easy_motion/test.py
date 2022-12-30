import unittest
from plover_vim.easy_motion.builtins import lookup


class TestEasyMotionLookup(unittest.TestCase):
    def test_success(self):
        self.assertEqual(lookup(("SKP*EULTDZ", "STKPW-B")), "{#z b}{plover:clear_trans_state}")
        self.assertEqual(lookup(("SKP*EULTDZ",)), '{#escape space space f shift(ampersand)}{^}')

if __name__ == "__main__":
    unittest.main()
