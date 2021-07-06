base10to26 = {
    0: "u",
    1: "w",
    2: "b",
    3: "c",
    4: "m",
    5: "v",
    6: "j",
    7: "r",
    8: "q",
    9: "e",
    10: "k",
    11: "i",
    12: "p",
    13: "h",
    14: "x",
    15: "f",
    16: "n",
    17: "t",
    18: "o",
    19: "y",
    20: "a",
    21: "g",
    22: "l",
    23: "z",
    24: "d",
    25: "s",
}

base26to10 = {v: k for k, v in base10to26.items()}


def convertIntToString(number: int) -> str:
    """ Returns the base 26 string key for a given base 10 integer. """
    result = ""
    while number > 0:
        quotient, remainder = divmod(number, 26)
        result += base10to26[remainder]
        number = quotient

    # Return the reversed string
    return result[::-1]


def convertStringToInt(string: str) -> int:
    """ Returns the base 10 integer for a given base 26 string key. """
    ans = 0
    power = 0
    for c in string[::-1]:
        ans += base26to10[c] * (26 ** power)
        power += 1

    return ans
