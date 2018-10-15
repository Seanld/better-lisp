# JUST FOR POSSIBLE FUTURE USE -- SINCE LISP IS ALREADY IN A TREE FORM, WE DON'T NEED SHUNTING-YARD
# TO GENERATE A STACK FOR CREATING A TREE. HOWEVER, IT MAY END UP BEING USED IN THE FUTURE, SO WE'LL
# KEEP IT HERE JUST IN CASE.

# Utilizes the Shunting-Yard algorithm to generate a queue of tokens, but in necessary order.
# Written in a separate file so that `syntaxtree.py` doesn't become cluttered and confusing.

from tokenizer import *
from syntaxtree import *

# Naive implementation of a queue (because I may need to alter how it works).
class Queue (object):
    def __init__(self, initial_values=[]):
        self.values = initial_values

    def push(self, value):
        self.values.append(value)
    
    def pop(self):
        return_value = self.values[0]

        self.values = self.values[1:]

        return return_value

    def look(self):
        return self.values[0]

# Naive implementation of a stack (because I may need to alter how it works).
class Stack (object):
    def __init__(self, initial_values=[]):
        self.values = initial_values

    def push(self, value):
        self.values.append(value)
    
    def pop(self):
        return_value = self.values[-1]
        
        self.values = self.values[:-1]

        return return_value
    
    def look(self):
        return self.values[-1]

# Defines what tokens are operators, and what precedence they have (lower number is a higher precedence).
OPERATORS = {
    "PLUS": 4,
    "MINUS": 3,
    "MULTIPLY": 2,
    "DIVIDE": 1,
    "POWER": 0,
    
    "R_PAREN": -1,
    "L_PAREN": -2,
}

def run(token_list):
    output_queue = Queue()
    operator_stack = Stack()

    for token in token_list:
        if token.type_name in OPERATORS: # Is an operator.
            if len(operator_stack.values) > 0:
                while OPERATORS[operator_stack.look().type_name] < OPERATORS[token.type_name]: # Stack has greater precedence.
                    output_queue.push(operator_stack.pop())
            
            output_queue.push(token)

        elif token.type_name == "L_PAREN":
            operator_stack.push(token)
        
        elif token.type_name == "R_PAREN":
            while operator_stack.look().type_name != "L_PAREN":
                output_queue.push(operator_stack.pop())
            
            operator_stack.pop()
        
        else: # Is an outputable value.
            output_queue.push(token)

    for operator in range(len(operator_stack.values)):
        output_queue.push(operator_stack.pop())
    
    return output_queue

tokens = [
    Token("L_PAREN", None),
    Token("PLUS", None),
    Token("INTEGER", None),
    Token("INTEGER", None),
    Token("R_PAREN", None)
]

print([v.type_name for v in run(tokens).values])