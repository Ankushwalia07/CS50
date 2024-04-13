print("What is the answer to the Great Question of Life, the Universe, and Everything? ",end=" ")
ans = input().strip().lower()

match ans:
    case "42" | "Forty Two" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")