# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *
import json

GRAMMAR = json.load(open("grammar.json"))

class Node (object):
    def __init__(self, token):
        self.token = token
        self.sub_nodes = []

class AST (object):
    def __init__(self, program_name, token_list):
        self.tree = [{program_name: []}]

        self.generate(token_list)
    
    def generate(self, token_list):
        splitted = split_tokens(["NEWLINE"], token_list)

        for split in splitted:
            expression = match_grammar(split)

            pass

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

        print(token.type_name)

        if token.type_name == "L_PAREN":
            print("LEFTY!")

            if seeking == True: # Sub-node to parse!
                recursed = construct(tokens[index:])

                print("BEFORE:", recursed[1])

                index += recursed[1]

                sub_tokens.append(recursed[0])
            else:
                seeking = True

        elif token.type_name == "R_PAREN": # Found an end, return results.
            seeking = False

            print("RETURNING")

            return (sub_tokens, index)

        else:
            sub_tokens.append(token)
        
        print("AFTER:", index)

        index += 1
    
    return None

# Helper function for `generate_ast`, just to make life easier.
def construct(tokens):
    return generate_ast(tokens)[0]

# Matches list of tokens to a grammar in `grammar.json`.
def match_grammar(token_list): # TODO LATER Not necessary anymore; deprecated.
    for grammar_def in GRAMMAR:
        grammar_contents = GRAMMAR[grammar_def]

        token_list_counter = 0
        grammar_list_counter = 0

        matching = True

        while grammar_list_counter < len(grammar_contents):
            row_count_tokens = row(token_list, token_list_counter)
            token = token_list[token_list_counter]

            if grammar_contents[grammar_list_counter][0] == "one":
                if token.type_name in grammar_contents[grammar_list_counter][1]:
                    token_list_counter += 1;

                else:
                    matching = False
                    break
            
            elif grammar_contents[grammar_list_counter][0] == "many":
                grammar_data = grammar_contents[grammar_list_counter]

                while token.type_name not in grammar_contents[grammar_list_counter + 1][1]:
                    if token.type_name in grammar_data[1]:
                        amount = row(token_list, token_list_counter)

                        token_list_counter += amount

                    token = token_list[token_list_counter]
            
            else:
                print("Invalid grammar amount specifier!")

            grammar_list_counter += 1
        
        if matching == True:
            if token_list_counter < len(token_list) - 1:
                return None
            else:
                return grammar_def
