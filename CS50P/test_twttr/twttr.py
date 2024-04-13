def main():
    string = input("Enter the string ")
    result = shorten(string)
    print(result)

def shorten(st):
    vow = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    shortened_string = ""
    for char in st:
        if char not in vow:
            shortened_string += char
    return shortened_string

if __name__ == "__main__":
    main()
