# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *
import json

GRAMMAR = json.load(open("grammar.json"))

# Splits a list of tokens using `token_type` as a delimiter.
def split_tokens(excluder_types, token_list):
    counter = 0

    splits = []
    accumulator = []

    for token in token_list:
        if token.type_name not in excluder_types:
            accumulator.append(token)
        else:
            splits.append(accumulator)
            accumulator = []
    
    if len(accumulator) > 0:
        splits.append(accumulator)
    
    return splits

# Counts how many tokens of the same `type_name` occur in a row in `token_list`, starting at `starting_index`.
def row(token_list, starting_index):
    counter = 1

    # print("INDEX: {}, MAX: {}".format(starting_index, len(token_list) - 1))

    token_type = token_list[starting_index].type_name

    for token in token_list[starting_index + 1:]:
        if token.type_name == token_type:
            counter += 1
        else:
            break
    
    return counter

OPERATORS = [
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "POWER",
    "ATOM"
]

def is_operator(t):
    if t in OPERATORS:
        return True
    else:
        return False

# Constructs an AST data structure that can then be used to generate VM code.
def generate_ast(tokens):
    index = 0

    seeking = False

    sub_tokens = []

    while index < len(tokens):
        token = tokens[index]

        if token.type_name == "L_PAREN":
            if seeking == True: # Sub-node to parse!
                recursed = generate_ast(tokens[index:])

                index += recursed[1]

                sub_tokens.append(recursed[0])
            
            else:
                seeking = True

        elif token.type_name == "R_PAREN": # Found an end, return results.
            seeking = False

            return (sub_tokens, index)

        else:
            sub_tokens.append(token)

        index += 1
    
    return None