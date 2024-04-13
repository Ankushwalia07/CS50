import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    rex = "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])"
    if match := re.search(r"^" + rex + "\." + rex + "\." + rex + "\." + rex + "$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
