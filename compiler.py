# Generates code for https://github.com/Seanld/vm from an AST generated via `syntaxtree.py`.

from tokenizer import *
from syntaxtree import *

def walk(level):
    current_stack = []

    try:
        for node in level[1:]:
            if type(node) == list:
                current_stack += walk(node)
            else:
                current_stack.append(node)

    except TypeError:
        current_stack.append(level)
    
    current_stack.append(level[0])
    
    return current_stack

RENAMES = {
    "PLUS": "+",
    "MINUS": "-",
    "TIMES": "*",
    "DIVIDE": "/",
    "POWER": "^"
}

def rename(token):
    if token.type_name == "ATOM":
        print(token.value)
        if token.value.group() == "var":
            return "store"
        else:
            return token.value.group()
    
    elif token.type_name == "STRING":
        return token.value.group()

    elif token.type_name == "INTEGER":
        return "#" + token.value.group()
    
    elif token.type_name in RENAMES:
        return RENAMES[token.type_name]
    
    else:
        return token.type_name

def compile_ast(tree_list):
    print(tree_list)

    stack = []
    
    for tree in tree_list:
        stack += walk(tree)

    counter = 0

    for token in stack:
        stack = stack[:counter] + [rename(token)] + stack[counter + 1:]

        counter += 1
    
    return stack