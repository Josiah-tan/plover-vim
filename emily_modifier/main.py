#!/bin/python
# Emily's Modifier Dictionary
# (rewritten with plover_python_dictionary_lib)

from typing import List

from plover.system import english_stenotype as e  # type: ignore
from plover_python_dictionary_lib import get_context_from_system

context=get_context_from_system(e)
s=context.SingleDictionary
stroke=context.stroke
subset=context.subsets
translation=context.translation

# ========

# define your ender here
uniqueEnders = stroke("LTZ")

# fingerspelling dictionary entries for relevant theories 
spelling = s({
        "A"     : "a",
        "PW"    : "b",
        "KR"    : "c",
        "TK"    : "d",
        "E"     : "e",
        "TP"    : "f",
        "TKPW"  : "g",
        "H"     : "h",
        "EU"    : "i",
        "AOEU"    : "i", # magnum
        "SKWR"  : "j",
        "SKWRAEU" : "j", # magnum
        "K"     : "k",
        "HR"    : "l",
        "PH"    : "m",
        "TPH"   : "n",
        "O"     : "o",
        "P"     : "p",
        "KW"    : "q",
        "R"     : "r",
        "S"     : "s",
        "T"     : "t",
        "U"     : "u",
        "SR"    : "v",
        "W"     : "w",
        "KP"    : "x",
        "KWR"   : "y",
        "STKPW" : "z",
        "STKPWHR" : "z", # magnum 
        })

# same as emily-symbols format, but modified for use on the left hand
symbols = s({
        "TR"    : ["tab", "delete", "backspace", "escape"],
        "KPWR"  : ["up", "left", "right", "down"],
        "KPWHR" : ["pageup", "end", "home", "pagedown"],
        ""      : ["", "tab", "return", "space"],

        # typable symbols
        "HR"     : ["exclam", "", "notsign", "exclamdown"],
        "PH"     : ["quotedbl", "", "", ""],
        "TKHR"   : ["numbersign", "registered", "copyright", ""],
        "KPWH"   : ["dollar", "euro", "yen", "sterling"],
        "PWHR"   : ["percent", "", "", ""],
        "SKP"    : ["ampersand", "", "", ""],
        "H"      : ["apostrophe", "", "", ""],
        "TPH"    : ["parenleft", "less", "bracketleft", "braceleft"],
        "KWR"    : ["parenright", "greater", "bracketright", "braceright"],
        "T"      : ["asterisk", "section", "", "multiply"],
        "K"      : ["plus", "paragraph", "", "plusminus"],
        "W"      : ["comma", "", "", ""],
        "TP"     : ["minus", "", "", ""],
        "R"      : ["period", "periodcentered", "", ""],
        "WH"     : ["slash", "", "", "division"],
        "TK"     : ["colon", "", "", ""],
        "WR"     : ["semicolon", "", "", ""],
        "TKPW"   : ["equal", "", "", ""],
        "TPW"    : ["question", "", "questiondown", ""],
        "TKPWHR" : ["at", "", "", ""],
        "PR"     : ["backslash", "", "", ""],
        "KPR"    : ["asciicircum", "guillemotleft", "guillemotright", "degree"],
        "KW"     : ["underscore", "", "", "mu"],
        "P"      : ["grave", "", "", ""],
        "PW"     : ["bar", "", "", "brokenbar"],
        "TPWR"   : ["asciitilde", "", "", ""]
        }).named("symbol")

symbol_variant = (s({"A": 1, "": 0}) * s({"O": 2, "": 0})).named("symbol_variant")

# left-hand bottom row counts in binary for numbers 0-9
count = (
		s({"R": 1, "": 0}) *
		s({"W": 2, "": 0}) *
		s({"K": 4, "": 0}) *
		s({"S": 8, "": 0})
		)

def accumulate_modifiers(character: str, mods: List[str])->str:
	# apply those modifiers
	combo = character
	for mod in mods:
		combo = mod + "(" + combo + ")"

	# package it up with the syntax
	ret = "{#" + combo + "}"

	# all done! :D
	return ret

dictionary = (
		(
			# use * to distinguish symbol input from numerical or character input
			(symbols * symbol_variant * stroke("*")).map(
				lambda symbol, symbol_variant:
				(symbol[symbol_variant] or None) if type(symbol) == list else symbol
				)
			|

			# AO is unused in finger spelling, thus used to disginguish numerical input
			stroke("AO") * 

			(
				# if TP is being held as well, then user is inputting a Fx key - like alt+F4
				# add the 'F' if F number
				s({"TP": "F"}) * count.filter(lambda x: 1 <= x <= 12).map(str) |
				count.filter(lambda x: x <= 9).map(str)
				)
			|

			# finger spelling input
			# if there is no entry, pass the error
			spelling.filter(lambda character: character!="")

			).named("character") *

		# accumulate list of modifiers to be added to the character
		# may need to reorder?
		(
			s({"-R": ["shift"], "": []}) *
			s({"-F": ["control"], "": []}) *
			s({"-B": ["alt"], "": []}) *
			s({"-P": ["super"], "": []})
			).named("mods") *

		uniqueEnders
		).map(accumulate_modifiers)

lookup=lambda strokes: dictionary.lookup_tuple(strokes)
LONGEST_KEY=dictionary.longest_key
assert LONGEST_KEY==1

if __name__=="__main__":
	dictionary.print_items()
