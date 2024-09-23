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
        return input()
    except EOFError:
        sys.exit("Should enter a text")
    except KeyboardInterrupt:
        sys.exit("Should enter a text")

def fliglet_text(text: str, font): 
    f = Figlet()
    all_fonts = f.getFonts()
    if font == True:
        font = choice(all_fonts)
    elif font not in all_fonts:
        sys.exit("Invalid usage")
    f.font = font      

    return f.renderText(text)

def print_text(text : FigletString):
    print(f'{text}')

if __name__ == '__main__':
    main()