def main():
    time = input("What time is it? ")
    n_time = convert(time)
    if 7.0 <= n_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= n_time <= 13.0:
        print("lunch time")
    elif 18.0 <= n_time <= 19.0:
        print("dinner time")
    else:
        return



def convert(time):
    x, y = time.split(":")
    hour = float(x)
    mins = float(y) * 1 / 60
    time = float(hour+mins)
    return time

if __name__ == "__main__":
    main()
