# Plover_vim
- This is an ambitious project that aims to make vim faster and more ergonomic for plover users
- a vim library for (mostly) single stroke vim commands

# Aims:
- highly extensible and customisable commands and translations
- (mostly) single chords for virtually everything of every vim command combination
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

# Prerequisites
- Download plover and find the executable
	- see this [website](https://plover.readthedocs.io/en/latest/cli_reference.html) for finding the location of plover depending on which platform you are using (Linux, Windows, etc.)

# Installation

- Now run this command to install the library
``` bash
plover -s plover_plugins install plover_vim
```

# Modules
- This repository shows you how you can import different modules from the plover_vim package to use
- This provides you with control over which modules to include for your plover + vim experience!

## Summary
| Module           | # Strokes | Short Description                                       | Examples                           |
|------------------|-----------|---------------------------------------------------------|------------------------------------|
| relative number  | 1         | jump to different lines (1 to 100)                      | 14j, 31k                           |
| easy motion      | 2         | command letter, but another stroke required for jumping | <leader><leader>fp st              |
| Josiah modifier  | 1         | Emily's modifiers but only left hand fingerspelling     | ctrl-w ctrl-w (change vim window), |
|                  |           |                                                         | ctrl-b w (tmux)                    |
| command letter 2 | 1         | any command followed by any text object                 | ciw, gcip, yii,                    |
|                  |           | (characters same as Josiah's modifiers)                 | vif, dt(, zz, viwp                 |
| command letter   | 1         | any command followed by any character                   | fu, T?, @q, gv                     |
| (deprecated)     |           | (characters same as Emily's modifiers)                  |                                    |
| command object   | 1         | any command followed by any text object                 | ciw, gcip, yi(                     |
| (deprecated)     |           | (characters same as Emily's symbols)                    |                                    |
| emily modifier   | 1         | Emily's modifiers but for vim                           | esc ctrl ^                         |
| (deprecated)     |           |                                                         |                                    |

## Relative-number

### What is relative numbering in vim?

- relative numbering is a numbering system that allows you to move quickly between any line in the code
- I recommend checking out the help menu in vim to learn more with it:
``` 
:help relativenumber
```
- it is good stuff

### How does this module improve vim?

- You can jump to different lines (up and down) in a single stroke
- this is achieved by stroking a number like usual in addition to another chord
    -   \'-7R\' =\> down 7 times
    -   \'1-6B\' =\> up 16 times
    -   \'1EUR7\' =\> down 71 times
- note that "R" and "B" are the same keys as what you'd use in Qwerty for up and down
- By default, the values for relative numbers do not go past 99 lines at a time

### Usage

- First, make sure to install plover_vim into plover
	- see [Installation](#Installation) for more instructions
- copy [templates/relative_number/simple.py](templates/relative_number/simple.py) and add it to your dictionaries for a simple configuration
- copy [templates/relative_number/customised.py](templates/relative_number/customised.py) and add it to your dictionaries for a customisable configuration
- It is recommended to remap top left S key as #

## Easy_motion

### what is easy_motion in vim?

-   easy motion is a
    [plugin](https://github.com/easymotion/vim-easymotion) that enables
    \"vim motions on speed!\"
-   Aims to optimise text navigation

### How does this module improve vim?

-   You can perform a search for a letter h as follows
    -   \<leader\>\<leader\>fhtk =\> H-FBLTDZ/T-BG
    -   breaking it down:
        -   H =\> h, using emily\'s modifier symbols for the left hand
        -   -FB =\> \<leader\>\<leader\>f
        -   -LTDZ =\> unique ender for finders
        -   T-BG =\> tk, this is the second stroke that takes you to the
            location

| Unique Ender | Modifiers | Command           | How To Memorize   |
|--------------|-----------|-------------------|-------------------|
| -LTDZ        | -FB       | <leader><leader>f | forward backwards |

### Usage

- put this line of code somewhere in your vimrc

``` vim
let g:EasyMotion_keys = 'bdfgjklmnprstxz'
```

- copy [templates/easy_motion/simple.py](templates/easy_motion/simple.py) and add it to your dictionaries for a simple configuration
- copy [templates/easy_motion/customised.py](templates/easy_motion/customised.py) and add it to your dictionaries for a customisable configuration
- see note on [control(j)](#control(j))

# Control(J)
-   Allows you to execute any (most) commands as if you are from normal
    mode
-   Sample .vimrc config (thanks
    [User202729](https://github.com/openstenoproject/plover/discussions/1350#discussioncomment-1905781))!

``` vim
"do nothing in normal mode
nore <c-j> <nop> 
"escape insert mode, then return to insert mode afterwards
inore <c-j> <c-\><c-o>
"escape command mode
cnoremap <c-j> <esc>

if !has('nvim')
    " escape terminal mode, then return to terminal mode
    set termwinkey=<c-j>
else
    " escape terminal mode, does not return to terminal mode :<
    tnoremap <c-j> <C-\><C-n>
endif
```


