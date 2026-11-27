text = input("Input: ")

for letter in "aeiouAEIOU":
    text = text.replace(letter, "")

print("Output:", text)
