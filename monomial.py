import collections
from typing import Union, List

from collections import Counter

def first(_list):
    return next(iter(_list), None)


def last(_list):
    try:
        return _list[-1]
    except IndexError:
        return None

class Monomial:
    superscript = {
        "0": "⁰",
        "1": "¹",
        "2": "²",
        "3": "³",
        "4": "⁴",
        "5": "⁵",
        "6": "⁶",
        "7": "⁷",
        "8": "⁸",
        "9": "⁹"
    }

    @staticmethod
    def getSuperscript(string):
        asd = []

        for i in string:
            asd.append(Monomial.superscript[i])

        return "".join(asd)

    def combineSameVars(self):

        combinedexponents = collections.Counter()

        for var, exponent in zip(self.vars, self.exponents):
            combinedexponents[var] += exponent

        temp_vars = []
        temp_exponents = []
        for key, value in combinedexponents.items():
            temp_vars.append(key)
            temp_exponents.append(value)

        self.vars = temp_vars
        self.exponents = temp_exponents

    def removeZeroExponents(self):
        index = 0
        while index < len(self.vars):
            if self.exponents[index] == 0:
                del self.vars[index]
                del self.exponents[index]

            index += 1

    def correctExponents(self):

        if first(self.exponents) is ... and last(self.exponents) is ...:
            raise Exception("Cannot have an Ellipsis on both ends!")

        if first(self.exponents) is ...:
            unique = len(self.exponents[1:])

            for i in range(len(self.vars) - unique):
                self.exponents.insert(0, 1)
        elif last(self.exponents) is ...:
            unique = len(self.exponents[:-1])

            for i in range(len(self.vars) - unique):
                self.exponents.append(1)
        else:
            for i in range(len(self.vars) - len(self.exponents)):
                self.exponents.append(1)

        try:
            self.exponents.remove(...)
        except ValueError:
            pass

    def __init__(self, coeff: int or float, vars: str="", *exponents):

        if len(vars) != len(exponents) and not all(map(lambda x: True if x == 1 else False, exponents)) and exponents[0] is not Ellipsis and exponents[-1] is not Ellipsis:
            raise Exception("Not all exponents provided!")


        self.coeff = coeff
        self.vars = list(vars)
        self.exponents = list(exponents)

        self.correctExponents()
        self.combineSameVars()
        self.removeZeroExponents()


        self.solvable = True

    def __str__(self):
        temp = []
        temp.append(str(self.coeff))
        for letter, exponent in zip(self.vars, self.exponents):
            temp.append(letter)
            if exponent != 1:
                temp.append(self.getSuperscript(str(exponent)))

        return "".join(temp)




a = Monomial(2, "x", 2)
b = Monomial(2)
c = Monomial(3, "ab")
d = Monomial(4, "abc", ..., 3)
e = Monomial(-3.0, "xyzabc", 1, 2, 3, ...)




print(a, b, c, d, e)
