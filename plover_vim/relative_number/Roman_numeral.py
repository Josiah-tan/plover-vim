#  [NullDev] [so/q/28777219] [cc by-sa 3.0]
from collections import OrderedDict
roman = OrderedDict()
roman[1000] = "M"
roman[900] = "CM"
roman[500] = "D"
roman[400] = "CD"
roman[100] = "C"
roman[90] = "XC"
roman[50] = "L"
roman[40] = "XL"
roman[10] = "X"
roman[9] = "IX"
roman[5] = "V"
roman[4] = "IV"
roman[1] = "I"

def number2Roman(num):
    assert (type(num) == int) or (type(num) == str and num.isnumeric())
    num = int(num)
    assert (num < 4000)
    ans = ""
    for r in roman.keys():
        x, _ = divmod(num, r)
        ans += roman[r] * x
        num -= (r * x)
        if num <= 0:
            break
    return ans

# number2Roman(3999)
# number2Roman("3999")
#
# int("3999")
