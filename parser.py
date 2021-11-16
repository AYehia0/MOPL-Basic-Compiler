"""
Language Grammar : 

    This is called an expression : 3 + 2 * 5
    Expression is multiple Terms + or - other terms 3, (2 * 5), each term contains factors (3, 2, 5) the factor can be INT or FLOAT

    so : 
        Expression : Term((PLUS|MINUS) term)*
        Term : Factor((MUL|DIV) factor)*
        Factor : INT|FLOAT

       +
      / \
     3   *
        / \
       5   2

    This is used to build the parsed tree, the tree has nodes (Operation node (MUL|DIV|ADD|SUB) and Number node (2,3,5))

"""

from lang_words import *

class Node:
    """This is the node holds the values : NUMBERS aka Factors"""
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str(self.token)


class OperationNode:
    """The operation node has 2 childerns leftNode and rightNode"""
    def __init__(self, left_node, op_value, right_node):
        self.left_node = left_node
        self.op_value = op_value 
        self.right_node = right_node 

    def __repr__(self):
        return f"({self.left_node}, {self.op_value}, {self.right_node})"

class Parser:
    """
    The parser takes a list of tokens and return the correct parse tree.

    The parser has 3 parts : Factor, Term and Expression

    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_ind = -1
        self.current_token = None

        ## Getting the first token
        self.get_next_token()

    def get_next_token(self):
        """Get the next token"""
        self.current_ind += 1

        # TODO : Check if the token is EOF
        self.current_token = self.tokens[self.current_ind] if self.current_ind < len(self.tokens) else None


    def parse_factor(self):
        """Extract the factor from the tokens"""
        token = self.current_token

        # check if the token is valid one
        if token.token_type in DATA_TYPES.values():

            # move 
            self.get_next_token()

            # create a node 
            return Node(token)

    def parse_term(self):
        return self.parse_op(self.parse_factor, [TOKEN_TYPES['/'], TOKEN_TYPES['*']])

    def parse_expr(self):
        return self.parse_op(self.parse_term, [TOKEN_TYPES['-'], TOKEN_TYPES['+']])

    def parse_op(self, get, ops):
        """Parses a term and expression, based on the get function (term, expr), and ops : TOKEN_TYPES"""

        # the first factor is the one in the left of the node
        first_factor = get()

        while self.current_token is not None and self.current_token.token_type in ops:
            # getting the op token (MUL,....)
            op_token = self.current_token

            # moving
            self.get_next_token()

            # the right one
            second_factor = get()

            first_factor = OperationNode(first_factor, op_token, second_factor)

        return first_factor 

    def parse(self):
        """Return the final parsed tree which is the expression after all"""
        return self.parse_expr()
