def convert(word):
    result = word.replace(":)","🙂").replace(":(", "🙁")
    return result

def main():
    word = input("Enter the sentence with Emoji: ")
    converted = convert(word)
    print(converted)

main()
