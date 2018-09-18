# Handles syntax tokenization.

import re

# Uses a dictionary where {"TOKEN_NAME": RE_COMPILE_OBJECT}, returns chronologically-ordered list of match objects.
def tokenize(token_dict, text_to_scan):
    matched_tokens = []
    accumulator = ""

    for char in text_to_scan:
        accumulator += char

        for token_name in token_dict:
            match_check = token_dict[token_name].match(accumulator)

            if match_check:
                matched_tokens.append({"match": match_check, "type": token_name})

                accumulator = ""

    return matched_tokens