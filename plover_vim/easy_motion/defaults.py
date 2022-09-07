from plover_vim.command_letter.defaults import (
        spelling, symbols, shifted_symbols_aus
        )

left_hand = {
        'PW': 'b',
        'TK': 'd',
        'TP': 'f',
        'TKPW': 'g',
        'SKWR': 'j',
        'K': 'k',
        'HR': 'l',
        'PH': 'm',
        'TPH': 'n',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'T': 't',
        'KP': 'x',
        'STKPW': 'z',
        #to complete left hand (thanks abby!)
        'A': 'a',
        'O': 'o',
        'WR': 'u',
        'SK': 'e',
        'SKW': 'i',
        'KR': 'c',
        'H': 'h',
        'KW': 'q',
        'SR': 'v',
        'W': 'w',
        'KWR': 'y'
        }

right_hand = {
        '': '',
        '-B': 'b',
        '-D': 'd',
        '-F': 'f',
        '-G': 'g',
        '-PBLG': 'j',
        '-BG': 'k',
        '-L': 'l',
        '-PL': 'm',
        '-PB': 'n',
        '-P': 'p',
        '-R': 'r',
        '-S': 's',
        '-T': 't',
        '-BGS': 'x',
        '-Z': 'z',
        # to complete right hand! (thanks abby!)
        '-EU': 'i',
        '-E': 'e',
        '-U': 'u',
        '-RB': 'a',
        '-SZ': 'c',
        '-FD': 'h',
        '-GS': 'o',
        '-LGTS': 'q',
        '-FB': 'v',
        '-FRP': 'w',
        '-FRPB': 'x',
        '-FPL': 'y'
        }


defaults = {
        "disable_defaults": True,
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "escape": "escape",
        "right_hand": right_hand,  # dict: easymotion finger spelling (right hand)
        "left_hand": left_hand,  # dict: easymotion finger spelling (left hand)
        "systems": [
            {
                "unique_ender": "LTDZ",
                "mods": {
                    # "-FPB": "",  # left empty for you to customise!
                    # "-FP": "",  #
                    "-FB": "space space f",  # Forward Back (moving this to another module)
                    # "-PB": "shift(t)",  # Previous Backwards
                    # "-F": "f",  # Forwards
                    # "-P": "t",  # Previous
                    # "-B": "shift(f)",  # Backwards
                    # "": ""  # for normal commands
                    }
                }
            ]
        }
