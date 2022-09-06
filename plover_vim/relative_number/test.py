import unittest
from plover_vim.relative_number.builtins import Lookup, RelativeNumberLookup

relative_number_lookup = RelativeNumberLookup()

# relative_number_lookup = RelativeNumberLookup({ #just for a small sample test
#     "silence_warnings": False,
#     "disable_defaults": True,
#     "numbers": {'S-': '1', 'T-': '2'},
#     "systems": {
#         "0": {
#             "stroke": "-S",
#             "callback": Zeroes(1),
#             "additional_map": "0",
#             }
#         }
#     })
# dict(relative_number_lookup.dictionary.items())

sample_lookup = Lookup({"up": "-B", "down": "-R"})

class TestRelativeNumberLookup(unittest.TestCase):
    def test_additional_map(self):
        self.assertEqual(relative_number_lookup(("#-S",)), "{&0}")
        self.assertEqual(relative_number_lookup(("-9SDZ",)), "{&00000}")
        self.assertEqual(relative_number_lookup(("#-D",)), "{&000000000}")
        self.assertEqual(relative_number_lookup(("#-SZ",)), "{&00}")
    
    def test_clock(self):
        self.assertEqual(relative_number_lookup(("4-BG",)), "{&4:00}")
        self.assertEqual(relative_number_lookup(("1UBG",)), "{&11:00}")
        self.assertEqual(relative_number_lookup(("12UBG",)), "{&21:00}")
        self.assertEqual(relative_number_lookup(("13BG",)), "{&13:00}")

    def test_zeros_pinky(self):
        self.assertEqual(relative_number_lookup(("4-S",)), "{&40}")
        self.assertEqual(relative_number_lookup(("14-SZ",)), "{&1400}")
        self.assertEqual(relative_number_lookup(("1234-78Z",)), "{&123489000}")
        self.assertEqual(relative_number_lookup(("3-9S",)), "{&30000}")
        self.assertEqual(relative_number_lookup(("4-79SDZ",)), "{&4800000}")
        self.assertEqual(relative_number_lookup(("5DZ",)), "{&5000000}")
        self.assertEqual(relative_number_lookup(("789",)), "{&890000000}")
        self.assertEqual(relative_number_lookup(("U69D",)), "{&7700000000}")
        self.assertEqual(relative_number_lookup(("340U7D",)), "{&8643000000000}")

    def test_relative_number(self):
        self.assertEqual(relative_number_lookup(("1-6B",)), f"{{#up{' up' * 16}}}")
        self.assertEqual(relative_number_lookup(("1-6R",)), f"{{#down{' down' * 16}}}")
        self.assertEqual(relative_number_lookup(("4U6R",)), f"{{#down{' down' * 73}}}")
        self.assertEqual(relative_number_lookup(("1-RS",)), f"{{#down{' down' * 9}}}")
        self.assertEqual(relative_number_lookup(("2-RS",)), f"{{#down{' down' * 19}}}")
    
    def test_double_U_number(self):
        self.assertEqual(relative_number_lookup(("4U",)), "{&44}")
        self.assertEqual(relative_number_lookup(("U6",)), "{&77}")
    
    def test_normal_number(self):
        self.assertEqual(relative_number_lookup(("1340",)), "{&1346}")
        self.assertEqual(relative_number_lookup(("123478",)), "{&123489}")
    
    def test_reverse_number(self):
        self.assertEqual(relative_number_lookup(("1340U",)), "{&6431}")
        self.assertEqual(relative_number_lookup(("1234U78",)), "{&984321}")


class TestLookup(unittest.TestCase):
    def test_single_digit_down(self):
        self.assertEqual(sample_lookup(("-R7",)), f"{{#down{' down' * 6}}}")
    
    def test_single_digit_up(self):
        self.assertEqual(sample_lookup(("2B",)), "{#up up}")
        self.assertEqual(sample_lookup(("5B",)), "{#up up up up up}")
    
    def test_multiple_digit(self):
        self.assertEqual(sample_lookup(("1-6B",)), f"{{#up{' up' * 15}}}")

    def test_reverse_down(self):
        self.assertEqual(sample_lookup(("1EUR7",)), f"{{#down{' down' * 70}}}")

    def repeat_digit(self):
        self.assertEqual(sample_lookup(("-R7D",)), f"{{#down{' down' * 76}}}")
        self.assertEqual(sample_lookup(("-3BD",)), f"{{#up{' up' * 32}}}")

    def test_too_many_numbers(self):
        with self.assertRaises(KeyError):
            sample_lookup(("10R789",))

    def test_incorrect_chord(self):
        with self.assertRaises(KeyError):
            sample_lookup(("1R-6",))
            sample_lookup(("1-RB8",))
    
    def test_zeros(self):
        with self.assertRaises(KeyError):
            sample_lookup(("0R",))
            sample_lookup(("0B",))

    def test_too_many_repeat_digit(self):
        with self.assertRaises(KeyError):
            sample_lookup(("14-RD",))
    
    def test_asterisk(self):
        with self.assertRaises(KeyError):
            sample_lookup(("14*R",))


if __name__ == "__main__":
    unittest.main()
