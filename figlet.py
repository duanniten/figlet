import sys
import pyfiglet

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



if __name__ == '__main__':
    main()