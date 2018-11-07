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
        mastertemp = []
        index = 0
        while index < len(expr):
            for regex, token in self.regexIter(sorted(TOKENS, key=len, reverse=True)):
                # print(f"DEBUG: regex: {regex}")
                length = 1
                slice = expr[index:index + length]

                result = True
                while index + length <= len(expr):

                    if regex.match(slice):
                        # print(slice, regex.pattern)
                        break


                    length += 1
                    slice = expr[index:index + length]
                else:
                    result = False

                if result:
                    # import pdb; pdb.set_trace()
                    print(slice, regex.pattern)
                    index += len(slice) - 1
                    break
                # print("-------------")
                # index += len(slice) - 1
                # quit()
            index += 1
        print(index, len(expr))
        return mastertemp


        # already_itered = ()
        #
        # for regex, token in self.regexIter(sorted(TOKENS, key=len, reverse=True)): #searching for the longest tokens first
        #
        #     slice_len = len(token)
        #
        #     for index in self.smartIter(len(expr) - slice_len, already_itered):
        #         slice = expr[index:index + slice_len]
        #         try:
        #             value = self.tokens[slice]
        #             if value == self.tokens[token]:
        #                 print(f"Found: value: {value}, token: {token}, from {slice}, index: {index}")
        #                 already_itered += tuple(range(index, index + slice_len))
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

TESTEXPR = "(3 + 2) ** 3 * 2"

print(list(map(str, Tokenizer(TOKENS).tokenize(TESTEXPR))))