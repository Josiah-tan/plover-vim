.PHONY: test all

test:
	python3 test.py

all:
	# python3 plover_dict.py
	# python3 templates/command_letter/customised.py > templates/command_letter/customised.json
	# python3 templates/easy_motion/customised.py > templates/easy_motion/customised.json
	# python3 templates/command_object/customised.py > templates/command_object/customised.json
	# python3 templates/emily_modifier/customised.py > templates/emily_modifier/customised.json
	# python3 templates/emily_modifier/simple.py > templates/emily_modifier/simple.json
	# python3 templates/josiah_modifier/customised.py > templates/josiah_modifier/customised.json
	# python3 templates/josiah_modifier/simple.py > templates/josiah_modifier/simple.json
	python3 templates/command_letter_2/simple.py > templates/command_letter_2/simple.json
	python3 templates/command_letter_2/customised.py > templates/command_letter_2/customised.json
