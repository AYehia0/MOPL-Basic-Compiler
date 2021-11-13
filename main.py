from scanner import Scanner

test_str = "(.5 / 30 )+ 3"

sc = Scanner(test_str)

print(test_str)
print(sc.generate_tokens())

