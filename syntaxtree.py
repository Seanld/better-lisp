# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *
import json

GRAMMAR = json.load(open("grammar.json"))

class AST (object):
    def __init__(self, program_name, token_list):
        self.data = {program_name: {}}

        self.generate(token_list)
    
    def generate(self, token_list):
        splitted = split_tokens("NEWLINE", token_list)
        expressions = {}

        for split in splitted:
            expressions[match_grammar(split)] = split
        
        print(expressions)

# Splits a list of tokens using `token_type` as a delimiter.
def split_tokens(token_type, token_list):
    counter = 0
    splits = []

    for token in token_list:
        if token_type == token.type_name:
            splits.append(token_list[:counter])

            token_list = token_list[counter + 1:]
            counter = 0
        
        else:
            counter += 1
    
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

# Matches list of tokens to a grammar in `grammar.json`.
def match_grammar(token_list):
    # match_check_list = [] # Gradually accumulates all the tokens from `token_list`; used to brute-force match a grammar.
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
