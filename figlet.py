import sys
from random import choice
from pyfiglet import Figlet

if len(sys.argv) == 3:
    if sys.argv[1] != '-f' or sys.argv[1] != '--font':
        sys.exit("incorrect argv")
    FONT = sys.argv[2]
elif len(sys.argv) != 1: 
    sys.exit("too many or too few argv")
    

def main():
    # Get imput text
    text = get_text()

    # Get text to print
    text = fliglet_text(text)

    # print text
    print_text(text)

def get_text():
    try: 
        return input("Input: ")
    except EOFError:
        sys.exit("Should enter a text")

def fliglet_text(text: str): 
    f = Figlet()
    if FONT == None:
        FONT = choice(f.getFonts())
    f.font = FONT
    return f.renderText(text)

if __name__ == '__main__':
    main()