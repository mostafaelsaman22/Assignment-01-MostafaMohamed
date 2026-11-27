name = input("camelCase: ")

snake = ""

for letter in name:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter

print(snake)
