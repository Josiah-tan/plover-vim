# Plover_vim

- This is an ambitious project that aims to make vim faster and more ergonomic for plover users
- A Python library to create custom dictionaries for generating (mostly) single stroke vim commands
	- e.g. 2caw, gcip, ya}

# Quick links

- See [speedrun video](https://www.youtube.com/watch?v=8-oDPhmpN9g) (2:50 min).
- For installation instructions interactive learning (`highly recommended`) see [plover-vim-tutor](https://github.com/Josiah-tan/plover-vim-tutor).

# Aims:
- highly extensible and customisable commands and translations
- (mostly) single chords for virtually every vim command combination
- Ability to do everything in insert mode (doesn't matter if you are in normal mode)

# Motivation
- Slowness of changing between insert and normal mode
- slowness of fingerspelling everything
- Emily's [modifiers](https://github.com/EPLHREU/emily-modifiers)
	- contains all control, alt, windows, etc. combined with every symbol possible
- Emily's [symbols](https://github.com/EPLHREU/emily-symbols)
	- symbols with full control over spacing, capitalization, and repetition
- User202729's [python dictionary library](https://github.com/user202729/plover-python-dictionary-lib)
	- makes coding a python dictionary significantly easier
	- highly recommend you check this out if you want to create your own dictionaries from scratch

# Developers

- This section shows how you can have an editable version of this project
- Firstly, fork this repository (in GitHub), then clone it:

``` bash
git clone https://github.com/your_user_name/plover_vim
```

- cd into this repo
- Then install for use!
	- Note that "plover" is the executable that you downloaded to make Plover work in the first place
	- See this [[https://plover.readthedocs.io/en/latest/cli_reference.html][website]] for the different locations depending on which platform you are using (Linux, Windows, etc)

``` bash
cd plover_vim
plover -s plover_plugins install -e .
```
