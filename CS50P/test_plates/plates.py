def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    li = []
    for i in s:
        li.append(i)
    if len(li) < 2 or len(li) > 6:
        return False
    if not li[0].isalpha() or not li[1].isalpha():
        return False
    if not all(s.isalnum() for s in li):
        return False

    flag = False
    for s in li:
        if s.isdigit():
            flag = True
        if s.isalpha() and flag:
            return False

    for s in li:
        if s.isdigit():
            return s != "0"

    return True



if __name__ == "__main__":
    main()
