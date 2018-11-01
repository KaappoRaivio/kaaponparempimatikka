import re
from typing import Dict, Any, Iterable

from _operatorD import builtins


OPENING_BRACE = 5
CLOSING_BRACE = 6

class Tokenizer:
    def __init__(self, tokens: Dict[str, Any]):
        self.tokens = tokens

    def getRegex(self):
        return re.compile(r"|".join(list(map(lambda x: f"\{x}", self.tokens))))


    @staticmethod
    def regexIter(iterable: Iterable[str]):
        for i in iterable:
            yield re.compile(re.escape(i)), i

    @staticmethod
    def smartIter(end, already_itered=()):
        for i in range(end):
            if i not in already_itered:
                yield i
            else:
                continue

    def tokenize(self, expr: str):
        already_itered = ()

        for regex, token in self.regexIter(sorted(TOKENS, key=len, reverse=True)): #searching for the longest tokens first

            slice_len = len(token)

            for a in self.smartIter(len(expr) - slice_len, already_itered):
                slice = expr[a:a + slice_len]
                try:
                    value = self.tokens[slice]
                    if value == self.tokens[token]:
                        print(f"Found: value: {value}, token: {token}, from {slice}, index: {a}")
                        already_itered += tuple(range(a, a + slice_len))
                except KeyError:
                    continue


TOKENS = {
    "+": builtins.OPERATOR_BINARY_ADD,
    "-": builtins.OPERATOR_BINARY_SUBTRACT,
    "**": builtins.OPERATOR_BINARY_POWER,
    "*": builtins.OPERATOR_BINARY_MULTIPLY,
    "/": builtins.OPERATOR_BINARY_DIVIDE,
    "(": 5,
    ")": 6
}


TESTEXPR = "(3 + 2) ** 3"

Tokenizer(TOKENS).tokenize(TESTEXPR)