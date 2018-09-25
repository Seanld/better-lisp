# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *
import json

GRAMMAR = json.load(open("ast.json"))

class Tree (object):
    def __init__(self, program_name):
        self.data = {program_name: {}}

def row(token_list, starting_index):
    counter = 1
    token_type = token_list[starting_index].type_name

    for token in token_list[starting_index + 1:]:
        if token.type_name == token_type:
            counter += 1
        else:
            break
    
    return counter

def match_grammar(token_list):
    # match_check_list = [] # Gradually accumulates all the tokens from `token_list`; used to brute-force match a grammar.

    for grammar_def in GRAMMAR:
        grammar_contents = GRAMMAR[grammar_def]

        token_list_counter = 0
        grammar_list_counter = 0

        matching = True

        while grammar_list_counter < len(grammar_contents):
            print("TLC: {} | GLC: {}".format(str(token_list_counter), str(grammar_list_counter)))

            row_count_tokens = row(token_list, token_list_counter)
            token = token_list[token_list_counter]

            if grammar_contents[grammar_list_counter][0] == "one":
                print("CHECKING ONE")
                print("IS `{}` IN {}?".format(token.type_name, grammar_contents[grammar_list_counter][1]))
                if token.type_name in grammar_contents[grammar_list_counter][1]:
                    print("MOVING ON")
                else:
                    print("NOT INSIDE")
                    matching = False
                    break
            elif grammar_contents[grammar_list_counter][0] == "many":
                print("CHECKING MANY")
                if row_count_tokens >= 1:
                    print("IS MULTIPLE")
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