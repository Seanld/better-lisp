import sys
import re
from tokenizer import *
from syntaxtree import *
from compiler import *

opened = open(sys.argv[1], "r")
SOURCE_CODE = opened.read()
opened.close()

TOKENS_TYPES = [
    Token("COMMENT", re.compile(r"\/\/.+")),

    Token("STRING", re.compile(r"\".+?\"")),
    Token("FLOAT", re.compile(r"\d+\.\d+")),
    Token("INTEGER", re.compile(r"-?\d+")),

    Token("ATOM", re.compile(r"\w+")),

    Token("COMMA", re.compile(r",")),
    Token("DOT", re.compile(r"\.")),
    Token("L_PAREN", re.compile(r"\(")),
    Token("R_PAREN", re.compile(r"\)")),
    Token("PLUS", re.compile(r"\+")),
    Token("MINUS", re.compile(r"\-")),
    Token("TIMES", re.compile(r"\*")),
    Token("DIVIDE", re.compile(r"\/")),
    Token("POWER", re.compile(r"\^"))
]

full_vm_code = []

tokens = tokenize(TOKENS_TYPES, SOURCE_CODE)

print(tokens)

tree = generate_ast(tokens)

print(tree)

vm_code = compile_ast(tree[0])

for token in vm_code:
    print(token)

opened = open(sys.argv[2], "w")
for item in vm_code:
    opened.write(str(item) + "\n")
opened.close()