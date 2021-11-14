"""This file holds the whole language"""

# Token types 

TOKEN_TYPES = {
    "*":"MUL",
    "/":"DIV",
    "+":"ADD",
    "-":"SUB",
    "(":"L_P",
    ")":"R_P",
}

# Data types 
DATA_TYPES = {
    "T_INT" : "INT",
    "T_FLOAT" : "FLOAT",
}

DIGITS = "1234567890"

# Creating the Tokenizer
class Token:
    # Some tokens don't have a value like : +,*,/ ,,, etc
    def __init__(self, token_type, token_value=None): 
        self.token_type = token_type
        self.value = token_value

    def __repr__(self):
        if self.value:
            return f"({self.token_type}, {self.value})"
        return self.token_type

# Errors 
class Error:
    def __init__(self, name, details):
        self.error_name = name
        self.details = details
    def __str__(self):
        return f"Error ({self.error_name}) : {self.details} "

class IllegalChar(Error):
    def __init__(self, details):
        super().__init__("Illegal Character", details)

# Creating the Scanner
class Scanner:
    """
    The scanner gets the text/stream of chars and make tokens of it.

    ex :  30 + 3.5 / 2  ----> [(30, INT), (+, PLUS), (3.5, FLOAT), (/, DIV), (2, INT)]
    """
    def __init__(self, string):
        self.chars = string
        self.current_pos = -1
        self.current_char = None
        self.move()

    def move(self):
        """Get the next char"""
        self.current_pos += 1
        self.current_char = self.chars[self.current_pos] if self.current_pos < len(self.chars) else None

    def generate_tokens(self):
        """Extract the tokens of of the string by looping"""

        tokens = []

        while self.current_char is not None:
            # ignoring spaces and tabs , ,,,etc

            if not self.current_char in " \t" :
                if self.current_char in "+*/-()":
                    tokens.append(Token(TOKEN_TYPES[self.current_char], self.current_char))
                    self.move()
                # checking for numbers
                elif self.current_char is not None:
                    if self.current_char in DIGITS + '.':
                        tokens.append(self.get_full_number())
                    # Error
                    else:
                        return [], str(IllegalChar(f"{self.current_char} at position {self.current_pos}"))
            else:
                self.move()

        return tokens, None

    def get_full_number(self):
        """Extracting the full number from 1234 + 23"""

        # string holding the number
        number = ""

        # checking for dots in float numbers
        dots = 0

        while self.current_char is not None and self.current_char in DIGITS + ".":
            if self.current_char == '.':

                # float can only have one dot
                if dots == 1:
                    break

                dots += 1
                number += self.current_char

            else:
                number += self.current_char
            # It's important to move to the next location
            self.move()

        # int
        if dots == 0:
            return Token(DATA_TYPES['T_INT'], int(number))

        return Token(DATA_TYPES['T_FLOAT'], float(number))
