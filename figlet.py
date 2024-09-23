import sys
from random import choice
from pyfiglet import Figlet, FigletString

if len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid usage")
    FONT = sys.argv[2]
elif len(sys.argv) != 1: 
    sys.exit("Invalid usage")
else:
    FONT = True

def main(font = FONT):
    # Get imput text
    text = get_text()

    # Get text to print
    text = fliglet_text(text, font)

    # print text
    print_text(text)

def get_text():
    try: 
        return input("Input: ")
    except EOFError:
        sys.exit("Should enter a text")
    except KeyboardInterrupt:
        sys.exit("Should enter a text")

def fliglet_text(text: str, font): 
    f = Figlet()
    if font:
        font = choice(f.getFonts())
    f.font = font
    return f.renderText(text)

def print_text(text : FigletString):
    print(f'Output: {text}')

if __name__ == '__main__':
    main()