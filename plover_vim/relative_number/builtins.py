from plover_vim.shared.builtins import BaseLookup

from plover_vim.relative_number.config import LONGEST_KEY
from plover_vim.relative_number.defaults import defaults_2
from plover_python_dictionary_lib import get_context_from_system, SingleDictionary, Dictionary

# ======== Boilerplate to set up objects.
from plover.system import english_stenotype as e
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation

import re
from plover_vim.shared.builtins import containsNumber
from plover_vim.relative_number.util import (
        assertGetDirection, assertGetInversion,
        assertGetNumber, assertDoubleValue
        )
from plover_vim.shared.builtins import RecursiveUpdate
from plover_vim.relative_number.defaults import defaults



class RelativeNumberLookup(BaseLookup):
    def __init__(self, opts={}):
        super().__init__(defaults_2, opts)
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self) -> Dictionary:
        # "keys": e.KEYS,
        # "numbers": {k: v.strip("-") for k, v in e.NUMBERS.items()},
        # if self.opts.get("keys") is None or self.opts["keys"] == {}:
        #     keys = e.KEYS
        # else: 
        #     keys = self.opts["keys"]
        self.keys = e.KEYS
        self.number_key = e.NUMBER_KEY
        if self.opts.get("numbers") is None or self.opts["numbers"] == {}:
            print("hello world this is Josiah")
            self.numbers = {k: v.strip("-") for k, v in e.NUMBERS.items()}
        else:
            self.numbers = self.opts["numbers"]
        # print(f"self.opts = {self.opts}")
        dictionary = self.getBaseNumbers()
        for identity, properties in self.opts["systems"].items():
            # print(f"identity = {identity}")
            # dictionary |= self.operateRecursively(identity, properties)
            dictionary |= self.operateRecursively(identity, properties)
            # if self.opts.get("apply_glue") and identity in self.opts["apply_glue"]:
            #     result = result.map(lambda x: f"{{&{x}}}")
            # dictionary |= result
        dictionary = dictionary.map(lambda x: x if x[0] == "{" else f"{{&{x}}}")
        return dictionary
    
    def filter(self, dictionary: dict, min_number: int, max_number: int) -> SingleDictionary:
        # just realized that this is in explicit form lol, probably should make it implicit
        # using the .filter method of the dictionary in the future
        result = {}
        for i, k in dictionary.items():
            int_k = int(k)
            if ((min_number is None or min_number <= int_k) and 
                    (max_number is None or max_number >= int_k)):
                result[i] = k
        return s(result)

    def operateRecursively(self, identity: str, properties: dict) -> SingleDictionary:
        dictionary = self.getBaseNumbers()
        if properties.get("dependencies"):
            for dependency in properties['dependencies']:
                dictionary |= self.operateRecursively(
                        dependency, self.opts["systems"][dependency])
        dictionary = self.filter(
                dictionary, properties.get("min_number"), properties.get("max_number"))
        if properties.get("stroke") and properties.get("callback"):
            dictionary = dictionary.map(properties["callback"])
            try:
                dictionary *= stroke(properties["stroke"])
            except AssertionError as assertion_error:
                silence_warnings = self.opts.get("silence_warnings")
                if silence_warnings is None or silence_warnings == False:
                    print(assertion_error)
                    print("""
                            even though there was an assertion error,
                            we will still try and continue,
                            see https://github.com/user202729/plover-python-dictionary-lib/issues/3 for more details
                            """)
                dictionary = s(dict(dictionary.items()))
                dictionary *= stroke(properties["stroke"])
        # NOTE: put this last, because dictionary *= stroke (from before), will make everything a pain, order actually matters
        if properties.get("additional_map"):
            dictionary |= stroke(self.number_key) * stroke(properties["stroke"]) * translation(properties["additional_map"])
        return dictionary

    def getBaseNumbers(self) -> SingleDictionary:
        dict = None
        for k in self.keys:
            if self.numbers.get(k):
                new = s({k: self.numbers[k]})
                if dict:
                    combined = dict * new
                    dict |= new
                    dict |= combined
                else:
                    dict = new
        # dict = dict.filter(lambda x: len(x) <= 2)
        return dict * stroke(self.number_key)

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        return super().__call__(chord)
    

relative_number_lookup = RelativeNumberLookup()
# relative_number_lookup.dictionary.items()
# for i, j in relative_number_lookup.dictionary.items():
#     print(i, j)

class Lookup(RecursiveUpdate):
    def __init__(self, opts={}):
        super().__init__(defaults, opts)

    def __call__(self, chord):
        assert len(chord) <= LONGEST_KEY
        stroke = chord[0]
        if not containsNumber(stroke):
            raise KeyError

        match = re.fullmatch(
                r'([12K3W4R]*)([50]*)([*-]?)([EU]*)([6R7B8G9SDZ]*)',
                stroke)

        (start, mid_left, wild, inversion, end) = match.groups()

        direction = assertGetDirection(
                {"up": self.opts["up"], "down": self.opts["down"]},
                start, wild, end)

        isInverted = assertGetInversion(inversion)
        repeat = assertGetNumber(start, mid_left, isInverted, end)
        repeat = assertDoubleValue(repeat, end)

        output = f"{{#{direction}{f' {direction}' * (repeat - 1)}}}"
        return output


lookup = Lookup()

# relative_number_lookup.dictionary.print_items()
# s(dict(relative_number_lookup.dictionary.items())).print_items()
# for i, j in relative_number_lookup.dictionary.items():
#     print(i, j)
#
# ##
#
# import importlib
# import relative_number
# importlib.reload(relative_number)
# from relative_number.util import double
#
# relative_number_lookup = RelativeNumberLookup({
#     "disable_defaults": True,
#     "numbers": {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '6', '-F': '7', '-P': '8', '-L': '9'},
#     "systems": {               
#         "doubleU": {
#             "stroke": "-U",
#             "callback": double,
#             "min_number": 0,
#             "max_number": 9,
#             },
#         "clock": {
#             "stroke": "-BG",
#             "callback": clock,
#             "dependencies": ["doubleU"],
#             "min_number": 1,
#             "max_number": 24,
#             }
#         }
#     })
#
# relative_number_lookup.dictionary.print_items()
#
# ##
#
#
# numbers = {k: v.strip("-") for k, v in e.NUMBERS.items()}
# keys = e.KEYS
# # >>> numbers
# # {'S-': '1', 'T-': '2', 'P-': '3', 'H-': '4', 'A-': '5', 'O-': '0', '-F': '6', '-P': '7', '-L': '8', '-T': '9'}
# # >>> keys
# # ('#', 'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-', 'A-', 'O-', '*', '-E', '-U', '-F', '-R', '-P', '-B' , '-L', '-G', '-T', '-S', '-D', '-Z')
#
# # dict = s({})
# # new = {"S": "1"}
# # dict * new
#
# dict = None
# for k in keys:
#     if numbers.get(k):
#         new = s({k: numbers[k]})
#         if dict:
#             combined = dict * new
#             dict |= new
#             dict |= combined
#         else:
#             dict = new
#
# # dict.print_items()
# assert len({i: k for i, k in dict.items()}) == 1023
#
# new_dict = {}
# for i, k in dict.items():
#     intk = int(k)
#     if 10 < intk and 100 > intk:
#         new_dict[i] = k
# new_dict
# ##
#
# new_dict = s({"S-": 10})
# for i, j in new_dict.items():
#     assert(len(i) == 1)
#     i = i[0]
#     print(i, j)
#
#
# ##
#
#
# def returnsNone(x):
#     if x[-1] == '0':
#         return None
#     else:
#         return x
#
# dictionary = s({"S-": "10", "P-": "20"})
# dictionary = dictionary.map(returnsNone)
# dictionary.print_items()
# ##
#
# dictionary = s({"S-": "10", "P-": "20"})
# dictionary.print_items()
# dictionary = dictionary.filter(lambda x: len(x) <= 2)
# dictionary.print_items()
# dictionary *= stroke("K-")
# dictionary.print_items()
#
# ##
#
# from plover_python_dictionary_lib import get_context_from_system
# from plover.system import english_stenotype as e
# context = get_context_from_system(e)
# s = context.SingleDictionary
# stroke = context.stroke
# translation = context.translation
#
# # should work, but leads to unexpected behaviour
# dictionary = s({"S-": "10", "K-": "100"})
# dictionary.print_items()
# # should remove the K?
# dictionary = dictionary.filter(lambda x: len(x) <= 2)
# try:
#     dictionary *= stroke("K-")
# except AssertionError as assertion_error:
#     print(assertion_error)
#     print("even though there was an assertion error, we will still try and continue, see https://github.com/user202729/plover-python-dictionary-lib/issues/3 for more details")
#     dictionary = s(dict(dictionary.items()))
#     dictionary *= stroke("K-")
# # adding the K back in (doesn't work)
# dictionary.print_items()
#
