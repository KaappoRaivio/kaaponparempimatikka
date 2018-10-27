from typing import List

from _operatorD import builtins
from _operatorD.__operator import BinaryOperator, UnaryOperator
from monomial import Monomial


class Unsolvable:
    def __init__(self, expr: List[BinaryOperator or UnaryOperator or Monomial]):
        self.expr = expr

    def solve(self):
        raise Exception("Cannot solve Unsolvable!")

    def __str__(self):
        mastertemp = ""

        for i in range(len(self.expr)):


            if len(mastertemp) > 0 and isinstance(self.expr[i - 1], UnaryOperator):
                mastertemp += f"({str(self.expr[i])})"
            else:
                mastertemp += f" {str(self.expr[i])}"


        return mastertemp.lstrip()


a = Unsolvable([Monomial(3, "x"), builtins.OPERATOR_BINARY_ADD, builtins.OPERATOR_UNARY_SQUARE_ROOT, Monomial(4, "a")])
print(a)