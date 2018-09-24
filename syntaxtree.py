# Facilitates the creation of ASTs for BetterLISP using generated token lists.

from tokenizer import *

class Tree (object):
    def __init__(self, program_name):
        self.data = {program_name: {}}

def generate_tree(token_list):
    for token in token_list:
        pass