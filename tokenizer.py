import re
from typing import Dict, Any

from _operatorD import builtins


class Tokenizer:
    def __init__(self, tokens: Dict[str, Any]):
        self.tokens = tokens

    def getRegex(self):
        return re.compile(r"|".join(list(map(lambda x: f"\{x}", self.tokens))))

    def tokenize(self, expr: str):
        for token in self.tokens:
            print(f"token: {token}")
            slice_len = len(token)
            # print(len(expr) - slice_len)
            for a in range(len(expr) - slice_len):
                slice = expr[a:a + slice_len]
                # print(slice)
                try:
                    value = self.tokens[slice]
                    if value == self.tokens[token]:
                        print(f"Found: value: {value}, token: {token}, from {slice}, index: {a}")
                except KeyError:
                    continue


TOKENS = {
    "+": builtins.OPERATOR_BINARY_ADD,
    "-": builtins.OPERATOR_BINARY_SUBTRACT,
    "**": builtins.OPERATOR_BINARY_POWER,
    "/": builtins.OPERATOR_BINARY_DIVIDE,
    "*": builtins.OPERATOR_BINARY_MULTIPLY,
    "(": 5,
    ")": 6
}

TESTEXPR = "(3 + 2) * 3"

Tokenizer(TOKENS).tokenize(TESTEXPR)