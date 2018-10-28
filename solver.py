import re
from typing import Optional, List, Union

from collections import Iterable

from _operatorD import builtins
from _operatorD.__operator import BinaryOperator, UnaryOperator



def flatten(_list):
    result = []
    if isinstance(_list, Iterable):
        for x in _list:
            result.extend(flatten(x))
    else:
        result.append(_list)
    return result


class Solver:
    MONOMIAL_REGEX = re.compile(r"^-?[0-9]+\.?[0-9]*[a-z]*$")
    # MONOMIAL_REGEX = re.compile(r"-?\d+(?:.\d+)?e\^-?\d+(?:.\d+)?x")

    def __init__(self, binaryoperators: Optional[List[Union[BinaryOperator, List[BinaryOperator]]]], unaryoperators: Optional[List[Union[UnaryOperator, List[BinaryOperator]]]]):
        self.binaryoperators = binaryoperators
        self.unaryoperators = unaryoperators

    def getUnaryRegexes(self):
        lst = []

        for i in self.unaryoperators:
            if isinstance(i, list):
                strings = list(map(str, i))
                strings = list(map(lambda x: f"\\{x}", strings))
                # print(strings)
                yield re.compile("|".join(strings)), i,
            elif isinstance(i, UnaryOperator):
                yield  re.compile(str(i)), i,
            else:
                raise Exception(f"Invalid thing {i} in self.unaryoperators!")

        raise StopIteration

    def getAllOperatorRegexes(self):
        strings = list(map(str, flatten(self.binaryoperators))) + list(map(str, flatten(self.unaryoperators)))
        strings = list(map(lambda x: f"\\{x}", strings))

        return re.compile("|".join(strings))



    def getOperatorFromString(self, string: str, operators: List[Union[BinaryOperator, UnaryOperator]]):
        for i in operators:
            if str(i) == string:
                return i
        else:
            return -1

    def expressionFromString(self, string: str):
        is_previous_part_of_monomial = False
        number_start_pos = -1
        number_end_pos = -1

        index = 0
        while index < len(string):
            character = string[index]
            # print(index, character)

            if self.MONOMIAL_REGEX.match(character) and not is_previous_part_of_monomial:
                number_start_pos = index
                number_end_pos = number_start_pos + 1
                while self.MONOMIAL_REGEX.match(string[number_start_pos:number_end_pos]):
                    if not number_end_pos < len(string):
                        break

                    number_end_pos += 1
                    # print(string[number_start_pos:number_end_pos])

                else:
                    number_end_pos -= 1

                print(string[number_start_pos:number_end_pos])
                index = number_end_pos

            # elif

            index += 1



a = Solver([[builtins.OPERATOR_BINARY_MULTIPLY, builtins.OPERATOR_BINARY_DIVIDE], [builtins.OPERATOR_BINARY_ADD, builtins.OPERATOR_BINARY_SUBTRACT]], list())
# print(a.getAllOperatorRegexes())
a.expressionFromString("12345.0xs +2")
# print(Solver.MONOMIAL_REGEX.match("-3.0 x"))