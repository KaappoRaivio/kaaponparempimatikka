from typing import Callable

from _operatorD.infix import UnaryInfix, BinaryInfix


class UnaryOperator(UnaryInfix):
    def __init__(self, string_representation: str, _function: Callable):
        super().__init__(_function)

        self.repr = string_representation

    def __str__(self):
        return self.repr

class BinaryOperator(BinaryInfix):
    def __init__(self, string_representation: str, _function: Callable):
        super().__init__(_function)

        self.repr = string_representation

    def __str__(self):
        return self.repr
