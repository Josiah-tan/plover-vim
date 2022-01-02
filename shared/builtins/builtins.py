def containsNumber(stroke):
    return any(k.isnumeric() for k in stroke)

steno_order = "#STKPWHRAO*EUFRPBLGTSDZ"
steno_order_numbers = "#12K3W4R50*EU6R7B8G9SDZ"
vowels = {"A", "O", "*", "E", "U"}
