import unittest
from plover_vim.relative_number.builtins import Lookup, RelativeNumberLookup
from plover_vim.relative_number.Roman_numeral import number2Roman

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
    
    def test_zeroes_pinky(self):
        self.assertEqual(relative_number_lookup(("4-S",)), "{&40}")
        self.assertEqual(relative_number_lookup(("14-SZ",)), "{&1400}")
        self.assertEqual(relative_number_lookup(("1234-78Z",)), "{&123489000}")
        self.assertEqual(relative_number_lookup(("3-9S",)), "{&30000}")
        self.assertEqual(relative_number_lookup(("4-79SDZ",)), "{&4800000}")
        self.assertEqual(relative_number_lookup(("5DZ",)), "{&5000000}")
        self.assertEqual(relative_number_lookup(("789",)), "{&890000000}")
        self.assertEqual(relative_number_lookup(("U69D",)), "{&000000007}")
        self.assertEqual(relative_number_lookup(("340U7D",)), "{&0000000008643}")

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
    
    def test_zeroes(self):
        with self.assertRaises(KeyError):
            sample_lookup(("0R",))
            sample_lookup(("0B",))

    def test_too_many_repeat_digit(self):
        with self.assertRaises(KeyError):
            sample_lookup(("14-RD",))
    
    def test_asterisk(self):
        with self.assertRaises(KeyError):
            sample_lookup(("14*R",))

class TestRomanNumerals(unittest.TestCase):
    def test_default(self):
        self.assertEqual(number2Roman(35), "XXXV")
        self.assertEqual(number2Roman(994), "CMXCIV")
        self.assertEqual(number2Roman(1995), "MCMXCV")
        self.assertEqual(number2Roman(2015), "MMXV")
    
    def test_zeros(self):
        self.assertEqual(relative_number_lookup(("4R-S",)), "XL")
        self.assertEqual(relative_number_lookup(("34R-S",)), "CCCXL")
    
    def test_reverseU(self):
        self.assertEqual(relative_number_lookup(("12RU",)), "XXI")
        self.assertEqual(relative_number_lookup(("13RU",)), "XXXI")
   
    def test_doubleU(self):
        self.assertEqual(relative_number_lookup(("4RU",)), "XLIV")
        self.assertEqual(relative_number_lookup(("RU8",)), "XCIX")

class TestSymbols(unittest.TestCase):
    def test_decimal(self):
        self.assertEqual(relative_number_lookup(("4ES",)), "{&4.0}")
        self.assertEqual(relative_number_lookup(("34E7",)), "{&3.48}")
    
    def test_dollar(self):
        self.assertEqual(relative_number_lookup(("K4RES",)), "{&$4.0}")
        self.assertEqual(relative_number_lookup(("K34RE78",)), "{&$3.489}")

    def test_percentage(self):
        self.assertEqual(relative_number_lookup(("4-G",)), "{&4%}")
        self.assertEqual(relative_number_lookup(("23-G",)), "{&23%}")
        self.assertEqual(relative_number_lookup(("4UG",)), "{&44%}")
        self.assertEqual(relative_number_lookup(("4EUG",)), "{&4.4%}")

class TestVimUpDownSystem(unittest.TestCase):
    def test_yank_up(self):
        self.assertEqual(relative_number_lookup(("K4-B",)), "{#escape y 4 k}")
    
    def test_yank_down(self):
        self.assertEqual(relative_number_lookup(("K4UR",)), "{#escape y 4 4 j}")
    
    def test_visualize_up(self):
        self.assertEqual(relative_number_lookup(("W4-B",)), "{#escape shift(V) 4 k}")
    
    def test_visualize_down(self):
        self.assertEqual(relative_number_lookup(("W4UR",)), "{#escape shift(V) 4 4 j}")
    
    def test_remove_up(self):
        self.assertEqual(relative_number_lookup(("4R-B",)), "{#escape c 4 k}")
    
    def test_remove_down(self):
        self.assertEqual(relative_number_lookup(("4RUR",)), "{#escape c 4 4 j}")

class TestClock(unittest.TestCase):
    def test_clock(self):
        self.assertEqual(relative_number_lookup(("4-BG",)), "4:00")
        self.assertEqual(relative_number_lookup(("1UBG",)), "11:00")
        self.assertEqual(relative_number_lookup(("12UBG",)), "21:00")
        self.assertEqual(relative_number_lookup(("13BG",)), "13:00")
    
    def test_clock_append(self):
        self.assertEqual(relative_number_lookup(("3-RBG",)), "{^}:03")
        self.assertEqual(relative_number_lookup(("3-RB8G",)), "{^}:39")
        self.assertEqual(relative_number_lookup(("2URBG",)), "{^}:22")
        self.assertEqual(relative_number_lookup(("35URBG",)), "{^}:53")
    
    def test_clock_append_failure(self):
        with self.assertRaises(KeyError):
            sample_lookup(("3URB8G",))

    
# relative_number_lookup(("4ES",))
if __name__ == "__main__":
    unittest.main()
