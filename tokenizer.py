import re
import _token
from typing import Dict, Any, Iterable, List, Sized

from _operatorD import builtins
from regexdict import RegexDict

OPENING_BRACE = 5
CLOSING_BRACE = 6
NUMBER = 7

class Tokenizer:
    def __init__(self, tokens: Dict[str, Any]):
        self.tokens = tokens

    def getRegex(self):
        return re.compile(r"|".join(list(map(lambda x: f"\{x}", self.tokens))))


    @staticmethod
    def regexIter(iterable: List[Sized]):
        for i in iterable:
            yield re.compile(i), i

    @staticmethod
    def smartIter(end, already_itered=()):
        for i in range(end):
            if i not in already_itered:
                yield i
            else:
                continue

    def tokenize(self, expr: str):
        a = 0
        while a < len(expr):
            for regex, token in self.regexIter(sorted(TOKENS, key=len, reverse=True)):
                # print(f"DEBUG: regex: {regex}")
                length = 1
                slice = expr[a:a + length]

                while True:
                    slice = expr[a:a + length]
                    length += 1
                    if regex.match(slice):
                        print(slice, self.tokens[slice])
                        a += len(slice)
                        break
                    if a + len(slice) >= len(expr):
                        break



            a += 1
        # already_itered = ()
        #
        # for regex, token in self.regexIter(sorted(TOKENS, key=len, reverse=True)): #searching for the longest tokens first
        #
        #     slice_len = len(token)
        #
        #     for a in self.smartIter(len(expr) - slice_len, already_itered):
        #         slice = expr[a:a + slice_len]
        #         try:
        #             value = self.tokens[slice]
        #             if value == self.tokens[token]:
        #                 print(f"Found: value: {value}, token: {token}, from {slice}, index: {a}")
        #                 already_itered += tuple(range(a, a + slice_len))
        #         except KeyError:
        #             continue


TOKENS = RegexDict({
    re.escape("+"): builtins.OPERATOR_BINARY_ADD,
    re.escape("-"): builtins.OPERATOR_BINARY_SUBTRACT,
    re.escape("*"): builtins.OPERATOR_BINARY_MULTIPLY,
    re.escape("**"): builtins.OPERATOR_BINARY_POWER,
    re.escape("/"): builtins.OPERATOR_BINARY_DIVIDE,
    re.escape("("): OPENING_BRACE,
    re.escape(")"): CLOSING_BRACE,
    r"[\-0-9.]": NUMBER
})

# TOKENS = (
#     token.Token(re.escape("+"), )
# )

TESTEXPR = "(3 + 2) ** 3"

Tokenizer(TOKENS).tokenize(TESTEXPR)