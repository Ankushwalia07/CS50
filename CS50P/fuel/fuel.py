while True:
    try:
        x,y = map(int, input("Fraction: ").split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

capacity = round(x / y * 100)
if capacity <= 1:
    print("E")
elif capacity >= 99:
    print("F")
else:
    print(f"{capacity}%")

