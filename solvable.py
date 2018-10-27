from typing import List

from _operatorD import builtins
from _operatorD.__operator import BinaryOperator, UnaryOperator
from monomial import Monomial


class Solvable:
    def __init__(self, expr: List[BinaryOperator or UnaryOperator or Monomial]):
        self.expr = expr

    def solve(self):
        ...


    def __str__(self):
        mastertemp = ""

        for i in range(len(self.expr)):


            if len(mastertemp) > 0 and isinstance(self.expr[i - 1], UnaryOperator):
                mastertemp += f"({str(self.expr[i])})"
            else:
                mastertemp += f" {str(self.expr[i])}"

        return mastertemp.lstrip()

