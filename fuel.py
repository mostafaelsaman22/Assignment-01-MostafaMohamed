while True:
    fraction = input("Fraction: ")
    try:
        parts = fraction.split("/")
        if len(parts) != 2:
            continue

        x = int(parts[0])
        y = int(parts[1])

        if x < 0 or y <= 0 or x > y:
            continue

        break
    except ValueError:
        continue

percent = round((x / y) * 100)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
