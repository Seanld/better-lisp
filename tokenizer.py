# Handles syntax tokenization.

import re
import time

class ansi:
    red = "\033[31m"
    end = "\033[0m"

class Token (object):
    def __init__(self, type_name, value):
        self.type_name = type_name
        self.value = value

def sortTokensBySpan(token_list): # Bubble-sorts the list by span.
    new_token_list = [t for t in token_list]

    [print(t.value.span()) for t in new_token_list]

    counter = 0

    while counter < len(new_token_list) - 1:
        #print(new_token_list)

        token = new_token_list[counter]
        next_token = new_token_list[counter + 1]

        if counter == len(new_token_list) - 1: # We've hit the end; it's now sorted.
            break
        else: # Keep scanning.
            if token.value.span() > next_token.value.span(): # Move up the line.
                #previous = new_token_list
                new_token_list = new_token_list[:counter] + [next_token, token] + new_token_list[counter + 2:]
                
                counter = 0
            else:
                counter += 1
        
        #time.sleep(1)
    
    return new_token_list

def cut(target_string, span_tuple):
    return target_string[:span_tuple[0]] + (" " * (span_tuple[1] - span_tuple[0])) + target_string[span_tuple[1]:]

# Uses a dictionary where {"TOKEN_NAME": RE_COMPILE_OBJECT}, returns chronologically-ordered list of match objects.
def tokenize(tokens_list, text_to_scan):
    text_block = text_to_scan

    matched_tokens = []

    for token in tokens_list:
        matched = token.value.search(text_block)

        while matched != None: # We are still finding matches, keep looping.
            new_token = Token(token.type_name, matched)

            matched_tokens.append(new_token)
            text_block = cut(text_block, matched.span())

            matched = token.value.search(text_block)
    
    return sortTokensBySpan(matched_tokens)
