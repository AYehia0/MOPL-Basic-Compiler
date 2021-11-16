from scanner import Scanner
from parser import Parser

test_str = "3 + 4 + 3 - 2 / 2"

print(test_str)

sc = Scanner(test_str)

tokens, err = sc.generate_tokens()

print(tokens)

pr = Parser(tokens)
ast = pr.parse()

print(ast)

