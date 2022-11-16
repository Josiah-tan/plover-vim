# Plover_vim
- This is an ambitious project that aims to make vim faster and more ergonomic for plover users
- A Python library to create custom dictionaries for generating (mostly) single stroke vim commands
	- e.g. ciw, gcip, ya}

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

# Prerequisites
- Download plover and find the executable
	- see this [website](https://plover.readthedocs.io/en/latest/cli_reference.html) for finding the location of plover depending on which platform you are using (Linux, Windows, etc.)

# Installation

- Now run this command to install the library
``` bash
<plover_executable> -s plover_plugins install plover_vim
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
- It is recommended to remap top left S key as #
- note there is a version 2 of this currently in the making
    - see [templates/Aerick/customised.py](templates/Aerick/customised.py) and [templates/Josiah/customised.py](templates/Josiah/customised.py) for examples of this new version

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
        -   H =\> h, using Josiah\'s modifier symbols for the left hand
        -   -FB =\> \<leader\>\<leader\>f
        -   -LTDZ =\> unique ender for finders
        -   T-BG =\> tk, this is the second stroke that takes you to the
            location

| Unique Ender | Modifiers | Command           | How To Memorize   |
|--------------|-----------|-------------------|-------------------|
| -LTDZ        | -EU       | <leader><leader>f | Forward Backwards |

### How does the double sided fingerspelling work?

- This plugin activates double sided fingerspelling after you stroke the starter, for a single stroke
- Here are some examples (see [plover_vim/easy_motion/defaults.py](plover_vim/easy_motion/defaults.py) for the full list):

| letter | right hand | left hand |
|--------|------------|-----------|
| b      | PW         | -B        |
| x      | KP         | -BGS      |
| j      | SKWR       | -PBLG     |

### Usage:
- put this line of code somewhere in your vimrc

``` vim
let g:EasyMotion_keys = 'bdfgjklmnprstxz'
```

- copy [templates/easy_motion/simple.py](templates/easy_motion/simple.py) and add it to your dictionaries for a simple configuration
- copy [templates/easy_motion/customised.py](templates/easy_motion/customised.py) and add it to your dictionaries for a customisable configuration
- see note on [Control(j)](#Control(J))


### Easy_motion (Advanced):

- You can use the left hand versions of the right hand vowels as follows:
- (Recommended by Abby)

| Letter | Old Version | New Remapped |
|--------|-------------|--------------|
| e      | E           | SK           |
| i      | EU          | SKW          |
| u      | U           | WR           |

- You can also use right hand fingerspelling
- This will require some time to memorize
- (ideas originate from realtime/realwrite and Magnum)

| Letter | Map   |
|--------|-------|
| a      | -RB   |
| c      | -SZ   |
| h      | -FD   |
| o      | -GS   |
| q      | -LGTS |
| v      | -FB   |
| w      | -FRP  |
| y      | -FPL  |

### Usage (Advanced)

- Put this line of code somewhere in your vimrc 
	- If you want to take advantage of the full alphabet

``` vim
let g:EasyMotion_keys = 'abcdefghijklmnopqrstuvwxyz'
```


## Josiah_modifier

### how does this module work?

- This is basically Emily modifiers, but it supports extra functionality
- The main idea is to remap these right hand fingerspelling commands to the left hand versions:

| Letter | Old Version | New Remapped |
|--------|-------------|--------------|
| e      | E           | SK           |
| i      | EU          | SKW          |
| u      | U           | WR           |

- This leaves more space for commands using the E and U keys
- The number key is also used to create more space for more options (8 altogether)

### Some ideas of what you can do with this extra space

- So you can prepend a command before an Emily modifier command:
	- ctrl-w ctrl-o = OULTZ
	- breaking it down:
		- OF = ctrl-o
		- U = ctrl-w
		- -LTZ = unique Emily modifier ender (ring finger on LT and pinky on Z)
- the table below shows default settings

| Chord | Prefix Command        | How To Memorize                  |
|-------|-----------------------|----------------------------------|
| #     | control(j)            |                                  |
| E     | escape                | EscapE                           |
| EU    | control(j) control(w) | vim splIt or wIndow              |
| #EU   | control(r)            | regIster                         |
| U     | control(b)            | tmUx                             |
| #E    | control(x)            | Ex command                       |
| NA    | NA                    | (used in a normal Emily command) |
| #U    | NA                    |                                  |

### Usage

- copy [templates/Josiah_modifier/simple.py](templates/Josiah_modifier/simple.py) and add it to your dictionaries for a simple configuration
- copy [templates/Josiah_modifier/customised.py](templates/Josiah_modifier/customised.py) and add it to your dictionaries for a customisable configuration
- see note on [Control(j)](#Control(j))

## Command_letter_2

### How does this module improve on command_letter and command_object?

- Basically it replaces the need for either of them using Josiah's modifiers as a base.
-   It can perform a complex finder operation:
    -   df) = KWR\*UBLTDZ
    -   breaking it down:
        -   KWR\* = ), using Josiah\'s / Emily's modifier for the left hand
        -   U = f (because it is the right key for the right thumb)
        -   B = c (B -> "blot", and hence delete)
        -   -LTDZ = unique ender for finders (ring finger on LT and
            pinky on DZ)
-   It can perform a miscellaneous operation:
    -   \[m = PHUTZ
    -   Breaking it down:
        -   PH = m, using Josiah\'s modifier for the left hand
        -   U = \[, idea from tpope\'s unimpaired
        -   -TZ = unique ender for miscellaneous (ring finger on T and
            pinky on Z)
-   It can perform a \"command-object\" operation:
    -   caw = WUBTDZ
    -   Breaking it down:
        -   W = w, using Josiah\'s modifier for the left hand
        -   U = a, U is more \"outside\" in position than E, so we use E
            = i cause it is more \"inner\" in position
        -   B = c, \"blot\" hence delete
        -   TDZ = unique ender for command object (ring finger on T,
            pinky on DZ)
-   The table below shows default settings
    -   \"Customisable\" commands can be filled in for personal useage

| category         | Unique Ender   | Modifiers   | Command        | How To Memorise          |
| ---------------- | -------------- | ----------- | -------------- | ------------------------ |
| finders          | -LTDZ          | -FPB        | customisable   |                          |
|                  |                | -FP         | customisable   |                          |
|                  |                | -FB         | customisable   |                          |
|                  |                | -PB         | customisable   |                          |
|                  |                | -F          | v              | Visualize                |
|                  |                | -P          | y              | coPy                     |
|                  |                | -B          | c              | Blot                     |
|                  | U              |             | f              | the right key            |
|                  | E              |             | shift(F)       | the left key             |
|                  | EU             |             | customisable   |                          |
|                  | #E             |             | shift(T)       | the left key with #      |
|                  | #U             |             | t              | the right key with #     |
|                  | #EU            |             | customisable   |                          |
|                  | #              |             | customisable   |                          |
| miscallaneous    | -TZ            | -FPB        | q              | liSeN                    |
|                  |                | -FP         | shift(at)      | macros                   |
|                  |                | -FB         | customisable   |                          |
|                  |                | -PB         | z              | zeN                      |
|                  |                | -F          | g              | the good Spot            |
|                  |                | -P          | r              | rePlace                  |
|                  |                | -B          | m              | marBg                    |
|                  |                |             | customisable   |                          |
|                  |                | #-B         | apostrophe     | similar to mark          |
|                  |                | #-P         | repeat         | rePeat                   |
|                  |                | -E          | [              | E is to the left of U    |
|                  |                | -U          | ]              | U is to the right of E   |
| command object   | -TDZ           | -FPB        | equal          |                          |
|                  |                | -FP         | ys             | coPy Furround            |
|                  |                | -FB         | cs             | Blot Furround            |
|                  |                | -PB         | gc             | commeNt                  |
|                  |                | -F          | v              | Fisualize                |
|                  |                | -P          | y              | coPy                     |
|                  |                | -B          | c              | Blot                     |
|                  |                | ""          | gU             |                          |
|                  |                | #-FPB       | v~             |                          |
|                  |                | #-FP        | S              |                          |
|                  |                | #-FB        | ds             |                          |
|                  |                | #-PB        | gb             |                          |
|                  |                | #-F         | vp             | visualize and paste!     |
|                  |                | #-P         | "              | y                        |
|                  |                | #-B         | customisable   |                          |
|                  |                | #           | gu             |                          |
|                  | E              |             | i              | Inner                    |
|                  | EU             |             | O              |                          |
|                  | U              |             | a              | Around                   |
|                  |                |             | ""             |                          |

### Usage
- First, make sure to install plover_vim into plover
	- see [Installation](#Installation) for more instructions
- copy [templates/command_letter_2/simple.py](templates/command_letter_2/simple.py) and add it to your dictionaries for a simple configuration
- copy [templates/command_letter_2/customised.py](templates/command_letter_2/customised.py) and add it to your dictionaries for a customisable configuration
- It is recommended to remap top left S key as #

## Command-letter (deprecated)

### How does this module improve vim?

-   You can perform any command followed by a letter in a single stroke
    for example:
    -   f\) = KWR\*FLTDZ
    -   breaking it down:
        -   KWR\* = ), using emily\'s modifier symbols for the left hand
        -   F = f
        -   -LTDZ = unique ender for finders (ring finger on LT and
            pinky on DZ)
-   The table below shows default settings
    -   \"Customisable\" commands can be filled in for personal useage

| category        | Unique Ender   | Modifiers   | Command        | How To Memorise        |
| --------------- | -------------- | ----------- | -------------- | ---------------------- |
| finders         | -LTDZ          | -FPB        | customisable   |                        |
|                 |                | -FP         | customisable   |                        |
|                 |                | -FB         |                | (used in easymotion)   |
|                 |                | -PB         | shift(t)       | Previous Backwards     |
|                 |                | -F          | f              | Forwards               |
|                 |                | -P          | t              | Previous               |
|                 |                | -B          | shift(f)       | Backwards              |
|                 |                |             | ""             | escaped commands       |
| miscallaneous   | -TZ            | -FPB        | q              | liSeN                  |
|                 |                | -FP         | shift(at)      | macros                 |
|                 |                | -FB         | customisable   |                        |
|                 |                | -PB         | z              | zeN                    |
|                 |                | -F          | g              | the good Spot          |
|                 |                | -P          | r              | rePlace                |
|                 |                | -B          | m              | marBg                  |
|                 |                |             | customisable   |                        |

### Usage

-   copy templates/command_letter/simple.py and add it to your
    dictionaries for default configuration
-   copy templates/command_letter/customised.py for a more
    customised experience
    -   note that (shift(at)) is required to output @ because raw
        keyboard input is
        [weird](https://github.com/openstenoproject/plover/issues/1465)
    -   See note on [control(j)](#Control(j))

## command-object (deprecated)

### How does this module improve vim?

-   You can perform any command followed by a text \"object\" in a
    single stroke for example:
    -   daw = STPRARLD
    -   breaking it down:
        -   STPR = unique starter
        -   A = a
        -   -RL = w, (see \"objects\" in
            command_object/defaults.py)
        -   -D = d
    -   yi( = STPROFPLZ
        -   STPR = unique starter
        -   O = i
        -   -FPL = (, using emily\'s symbols for the right hand
        -   -Z = y
-   The table below shows the default mappings
    -   \"Customisable\" commands can be filled in for personal useage
    -   note: AO combinations can be combined with other modifiers

| Unique starter | Modifiers | Command      | How To Memorise | Plugin Requirements   |
|----------------|-----------|--------------|-----------------|-----------------------|
| STPR           | -T        | g c          | commenTary      | tpope/vim-commentary  |
|                | -D        | d            | Delete          |                       |
|                | -S        | y s          | Surround        | tpope/vim-surround    |
|                | -Z        | y            | xyZ             |                       |
|                | -TD       | customisable |                 |                       |
|                | -DZ       | d s          | Delete Surround | tpope/vim-surround    |
|                | -SZ       | v            | viSualiZe       |                       |
|                | -TS       | customisable |                 |                       |
|                | *T        | g b          | commenTary      | numToStr/Comment.nvim |
|                | *D        | customisable |                 |                       |
|                | *S        | shift(s)     | Surround        | tpope/vim-surround    |
|                | *Z        | customisable |                 |                       |
|                | *TD       | customisable |                 |                       |
|                | *DZ       | customisable |                 |                       |
|                | *SZ       | customisable |                 |                       |
|                | *TS       | customisable |                 |                       |
|                |           | customisable |                 |                       |
|                | A         | a            | around          |                       |
|                | O         | i            |                 |                       |
|                | AO        | customisable |                 |                       |
|                |           | ""           |                 |                       |


### Limitations

-   some command + motion combinations must be stroked in two, for
    example:
    -   ct=

### Usage

-   copy templates/command_object/simple.py and add it to your
    dictionaries for default configuration
-   copy templates/command_object/customised.py for a more
    customised experience
    -   note that (shift(s)) is required to output S because raw
        keyboard input is
        [weird](https://github.com/openstenoproject/plover/issues/1465)
    -   See note on [control(j)](#Controlj)

## Emily-modifier (deprecated)

### How does this module improve upon the [original](https://github.com/EPLHREU/emily-modifiers)?

-   You can prepend an escape to the command
-   Commands like ctrl\^ no longer require shift to be pressed [related
    issue](https://github.com/openstenoproject/plover/issues/1465)

### Usage

-   copy templates/Emily_modifier/simple.py and add it to your
    dictionaries for a simple configuration
-   copy templates/Emily_modifier/customised.py for a more
    customised experience
    -   see note on [control(j)](#Control(J))


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
