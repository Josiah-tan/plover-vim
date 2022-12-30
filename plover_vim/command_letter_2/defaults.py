from plover_vim.Josiah_modifier.defaults import shifted_symbols_aus, symbols, spelling

middles = {
        "": ""
        }

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "command_suffix": "{plover:clear_trans_state}",
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "middles": middles,
        "escape": "escape",
        "systems": []
            }
