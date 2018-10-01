# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *
import json

GRAMMAR = json.load(open("grammar.json"))

class AST (object):
    def __init__(self, program_name, token_list):
        self.data = {program_name: {}}
    
    def generate(self):
        pass

def row(token_list, starting_index):
    counter = 1
    token_type = token_list[starting_index].type_name

    for token in token_list[starting_index + 1:]:
        if token.type_name == token_type:
            counter += 1
        else:
            break
    
    return counter

def split_tokens(token_type, token_list):
    counter = 0
    splits = []

    while counter < len(token_list) - 1:
        token = token_list[counter]

        if token_type == token[0]:
            splits.append(token_list[:counter])

            token_list = token_list[counter:]
            counter = 0
        
        counter += 1
    
    return splits

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
                    pass
                else:
                    matching = False
                    break
            
            elif grammar_contents[grammar_list_counter][0] == "many":
                if row_count_tokens >= 1:
                    if token.type_name in grammar_contents[grammar_list_counter][1]:
                        token_list_counter += row_count_tokens - 1
                    else:
                        matching = False
                        break
                else:
                    matching = False
                    break
            else:
                print("Invalid grammar amount specifier!")

            token_list_counter += 1; grammar_list_counter += 1
        
        if matching == True:
            return grammar_def