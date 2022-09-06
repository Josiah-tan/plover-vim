import unittest
from plover_vim.shared.builtins import containsNumber


class ContainsNumber(unittest.TestCase):
    def test_contains_number(self):
        self.assertFalse(containsNumber("hello world",))
        self.assertTrue(containsNumber("hello 6world",))
        self.assertTrue(containsNumber("1234",))

if __name__ == "__main__":
    unittest.main()
