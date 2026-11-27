def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    found_num = False
    for c in s:
        if c.isdigit():
            if not found_num and c == "0":
                return False
            found_num = True
        else:
            if found_num:
                return False

    return True


main()
