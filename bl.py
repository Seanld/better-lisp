import sys
import re
import tokenizer

opened = open(sys.argv[1], "r")
SOURCE_CODE = opened.read()
opened.close()

TOKENS_TYPES = {
    "STRING": re.compile(r"\".+\""),
    "FLOAT": re.compile(r"\d+\.\d+"),
    "INTEGER": re.compile(r"\d+"),
    "COMMA": re.compile(r",")
}

matches = tokenizer.tokenize(TOKENS_TYPES, SOURCE_CODE)