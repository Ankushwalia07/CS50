import pyfiglet as fig
import sys
import random
figlet = fig.Figlet()
argv1 = ["-f", "--font"]

#Its a good idea to make a function for a specific task and call it under the main function

def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        fig("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        fig("Input: ", font)
    else:
        sys.exit("Invalid usage")


def fig(prompt, font):
    txt = input(prompt)
    figlet.setFont(font= font)
    print("Output:")
    print(figlet.renderText(txt))


main()
