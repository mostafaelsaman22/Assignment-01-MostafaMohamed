months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").strip()

    if "/" in date:
        parts = date.split("/")
        if len(parts) != 3:
            continue
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        except ValueError:
            continue

    elif "," in date:
        parts = date.split(",")
        if len(parts) != 2:
            continue

        left = parts[0].strip().split()
        if len(left) != 2:
            continue

        month_name = left[0].capitalize()
        if month_name not in months:
            continue

        month = months.index(month_name) + 1

        try:
            day = int(left[1])
            year = int(parts[1].strip())
        except ValueError:
            continue

    else:
        continue

    if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
        continue

    print(f"{year:04d}-{month:02d}-{day:02d}")
    break
