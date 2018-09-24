import sys
import re
from tokenizer import *

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

    #{"type": "SPACE", "regex": re.compile(r" ")},
    Token("NEWLINE", re.compile(r"\n"))
]

matches = tokenize(TOKENS_TYPES, SOURCE_CODE)

print("")
[print(m.value.span()) for m in matches]