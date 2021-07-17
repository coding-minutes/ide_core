import string
import random


class IDCodec:
    """ Encoder / Decoder for database ID's  """

    def __init__(self) -> None:
        chars = list(string.ascii_lowercase)
        random.Random(4).shuffle(chars)
        self.base10to26 = {}
        self.base26to10 = {}

        for (i, c) in enumerate(chars):
            self.base10to26[i] = c
            self.base26to10[c] = i

    def convertIntToString(self, number: int) -> str:
        """ Returns the base 26 string key for a given base 10 integer. """
        result = ""
        while number > 0:
            quotient, remainder = divmod(number, 26)
            result += self.base10to26[remainder]
            number = quotient

        # Return the reversed string
        return result[::-1]

    def convertStringToInt(self, string: str) -> int:
        """ Returns the base 10 integer for a given base 26 string key. """
        ans = 0
        power = 0
        for c in string[::-1]:
            ans += self.base26to10[c] * (26 ** power)
            power += 1

        return ans


def get_id_codec():
    return IDCodec()
