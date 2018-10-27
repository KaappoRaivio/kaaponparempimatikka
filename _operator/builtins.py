import operator
import math

from _operator._operator import BinaryOperator, UnaryOperator

OPERATOR_BINARY_ADD         = BinaryOperator("+", operator.add)
OPERATOR_BINARY_SUBTRACT    = BinaryOperator("-", operator.sub)
OPERATOR_BINARY_MULTIPLY    = BinaryOperator("*", operator.mul)
OPERATOR_BINARY_DIVIDE      = BinaryOperator("/", operator.truediv)
OPERATOR_BINARY_POWER       = BinaryOperator("^", operator.pow)

OPERATOR_UNARY_MINUS        = UnaryOperator ("-", operator.neg)
OPERATOR_UNARY_SQUARE_ROOT  = UnaryOperator ("√", math.sqrt)