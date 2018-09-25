import sys
import re
from tokenizer import *
from syntaxtree import *

opened = open(sys.argv[1], "r")
SOURCE_CODE = opened.read()
opened.close()

TOKENS_TYPES = [
    Token("STRING", re.compile(r"\".+?\"")),
    Token("FLOAT", re.compile(r"\d+\.\d+")),
    Token("INTEGER", re.compile(r"\d+")),

    Token("ATOM", re.compile(r"\w+")),

    Token("COMMA", re.compile(r",")),
    Token("DOT", re.compile(r"\.")),
    Token("L_PAREN", re.compile(r"\(")),
    Token("R_PAREN", re.compile(r"\)")),
    Token("PLUS", re.compile(r"\+")),
    Token("MINUS", re.compile(r"\-")),
    Token("TIMES", re.compile(r"\*")),
    Token("DIVIDE", re.compile(r"\/")),

    #{"type": "SPACE", "regex": re.compile(r" ")},
    Token("NEWLINE", re.compile(r"\n"))
]

tokens = tokenize(TOKENS_TYPES, SOURCE_CODE)

[print(token.type_name) for token in tokens]

print(match_grammar(tokens))