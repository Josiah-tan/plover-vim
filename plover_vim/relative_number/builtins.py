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
        self._cache_base_numbers = None
        self._identity2dictionary = {}  # caching
        self.dictionary = self.getDictionary()
        assert self.dictionary.longest_key == LONGEST_KEY

    def getDictionary(self) -> Dictionary:
        self.keys = e.KEYS
        self.number_key = e.NUMBER_KEY
        if self.opts.get("numbers") is None or self.opts["numbers"] == {}:
            self.numbers = {k: v.strip("-") for k, v in e.NUMBERS.items()}
        else:
            self.numbers = self.opts["numbers"]
        dictionary = self.getBaseNumbers().map(self.postDefault)
        for identity, properties in self.opts["systems"].items():
            if properties.get("stroke"):  # e.g. handle the "zeroes" case, where there is no additional entry
                _dictionary = self.operateRecursively(identity, properties)
                if properties.get("post_callback"):
                    dictionary |= properties["post_callback"](_dictionary)
                else:  # default behaviour: adds a "&" using command syntax
                    dictionary |= _dictionary.map(self.postDefault)
        return dictionary
    
    def filter(self, dictionary: dict, min_number: int, max_number: int) -> SingleDictionary:
        return dictionary.filter(
            lambda x:
            (min_number is None or min_number <= int(x)) and
            (max_number is None or int(x) <= max_number)
            ).map(str)
        
        
    def operateRecursively(self, identity: str, properties: dict) -> SingleDictionary:
        if self._identity2dictionary.get(identity) is None:
            dictionary = self.getBaseNumbers()
            if properties.get("dependencies"):
                for dependency in properties['dependencies']:
                    dictionary |= self.operateRecursively(
                            dependency, self.opts["systems"][dependency])
            dictionary = self.filter(
                    dictionary, properties.get("min_number"), properties.get("max_number"))
            if properties.get("stroke"):
                if properties.get("callback"):
                    dictionary = dictionary.map(properties["callback"])
                if properties.get("additional_map"):
                    dictionary |= stroke(self.number_key) * translation(properties["additional_map"])
                dictionary = dictionary * stroke(properties["stroke"])
            self._identity2dictionary[identity] = dictionary
        return self._identity2dictionary[identity]

    def getBaseNumbers(self) -> SingleDictionary:
        if self._cache_base_numbers is None:
            dictionary = None
            if type(self.numbers) == SingleDictionary:
                dictionary = self.numbers
            elif type(self.numbers) is type({}):  # probably a dict
                for k in self.keys:
                    if self.numbers.get(k):
                        new = s({k: self.numbers[k]})
                        if dictionary:
                            combined = dictionary * new
                            dictionary |= new
                            dictionary |= combined
                        else:
                            dictionary = new
            self._cache_base_numbers = dictionary * stroke(self.number_key)
        return self._cache_base_numbers
        
    @staticmethod
    def postDefault(x: str) -> str:
        return x if x[0] == "{" else f"{{&{x}}}"
            
    @staticmethod
    def expand(dictionary: dict) -> SingleDictionary:
        return s(dict(dictionary.items()))
        

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

