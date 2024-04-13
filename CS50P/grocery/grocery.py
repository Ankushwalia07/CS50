grocery = []
tally = {}

while True:
    try:
        item = input("")
        item = item.upper()

        grocery.append(item)
        grocery.sort()

    except EOFError:
        for item in grocery:
            if item in tally:
                tally[item] += 1
            else:
                tally[item] = 1
        for i in tally:
            print(str(tally[]) + " " + i)
        break
    else:
        continue