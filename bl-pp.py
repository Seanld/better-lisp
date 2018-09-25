# PyPEG2 implementation of the parser.

from pypeg2 import *
import sys

opened = open(sys.argv[1], "r")
SOURCE_CODE = opened.read()
opened.close()

class Integer (int):
    grammar = re.compile(r"\d+")
class Float (float):
    grammar = re.compile(r"\d+\.\d+")
class String (str):
    grammar = re.compile(r"\".+?\"")

class MathOperator (str):
    grammar = re.compile(r"\+|\-|\*|\/")

class Atom (str):
    grammar = re.compile(r"\w+")

class Statement (List):
    grammar = "(", [MathOperator, Atom], some([String, Float, Integer, Atom]), ")", endl

class Statements (List):
    grammar = maybe_some(Statement)

parsed = parse(SOURCE_CODE, Statements)

[print(p) for p in parsed]