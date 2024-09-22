import sys

if len(sys.argv) == 3:
    if sys.argv[1] != '-f' or sys.argv[1] != '--font':
        sys.exit("incorrect argv")
    FONT = sys.argv[2]
elif len(sys.argv) != 1: 
    sys.exit("too many or too few argv")