import inflect
import sys

inf = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", inf.join(names))
        sys.exit()
