from plover_vim.command_letter.defaults import spelling, shifted_symbols_aus, symbols

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "command_suffix": "{plover:clear_trans_state}",
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "escape": "",
        "unique_ender": "-LTZ",
        }
