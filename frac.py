import math


class Frac:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0 or not (isinstance(numerator, int) and isinstance(denominator, int)) :
            raise Exception(f"Invalid arguments {numerator} and {denominator}!")

        self.numerator = numerator
        self.denominator = denominator

    def __expand(self, expander: int):
        return Frac(self.numerator * expander, self.denominator * expander)

    def __reduce(self, reducor):
        if  self.numerator % reducor or self.denominator % reducor:
            raise Exception(f"Can't reduce with {reducor}!")
        else:
            return Frac(self.numerator // reducor, self.denominator // reducor)


    def __add__(self, other):
        if isinstance(other, Frac):
            expandedself = self.__expand(self.__lcm(self.denominator, other.denominator) // self.denominator)
            expandedother = other.__expand(self.__lcm(self.denominator, other.denominator) // other.denominator)

            temp = Frac(expandedother.numerator + expandedself.numerator, expandedself.denominator)
            return temp.__reduce(self.__gcd(temp.numerator, temp.denominator))

        elif isinstance(other, int):
            temp = Frac(self.numerator + other * self.denominator, self.denominator)

            return temp.__reduce(self.__gcd(temp.numerator, temp.denominator))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Frac):
            temp = Frac(other.numerator * self.numerator, self.denominator * other.denominator)

            return temp.__reduce(self.__gcd(temp.numerator, temp.denominator))

        elif isinstance(other, int):
            temp = Frac(self.numerator * other, self.denominator)
            print(temp)

            return temp.__reduce(self.__gcd(temp.numerator, temp.denominator))


    def __rmul__(self, other):
        return self.__mul__(other)



    def __truediv__(self, other):
        if isinstance(other, Frac):
            temp = self * ~other
            return temp.__reduce(self.__gcd(temp.numerator, temp.denominator))

    def __sub__(self, other):
        if isinstance(other, Frac):
            return self + (-other)
        elif isinstance(other, int):
            tempfrac = Frac(other, 1)
            return tempfrac + (-self)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __invert__(self):
        return Frac(self.denominator, self.numerator)

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"({self.numerator} / {self.denominator})"

    def __neg__(self):
        return Frac(-self.numerator, self.denominator)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return self * self.__pow__(power - 1) if power != 1 else self
        else:
            raise Exception(f"Power must be int, not {type(power)}")

    def __rpow__(self, other):
        if not ( isinstance(other, int) or isinstance(other, float) ):
            raise Exception(f"Base must be int, not {type(other)}!")

        return self.__nth_root(other ** self.numerator, self.denominator)

    @staticmethod
    def __nth_root(base, n):
        return base ** (1 / n)


    @staticmethod
    def __gcd(x, y):
        return math.gcd(x, y)


    @staticmethod
    def __lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y

        while True:

            if greater % x == 0 and greater % y == 0:
                lcm = greater
                break
            greater += 1

        return lcm


if __name__ == "__main__":
    print(Frac(5, 4) * Frac(2, 11))



