.PHONY: test all

test:
	python3 test.py

all:
	# python3 plover_dict.py
	python3 command_letter/builtins.py > command_letter/builtins.json
