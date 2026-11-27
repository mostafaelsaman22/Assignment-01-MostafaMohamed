grocery = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        break

    if item != "":
        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1

for item in sorted(grocery):
    print(f"{grocery[item]} {item}")
