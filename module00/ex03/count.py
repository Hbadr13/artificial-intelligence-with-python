
import sys

def text(*argv):
    if(len(argv) == 0):
        argv[0] = "hello"
    print(argv[0])
    exit()
    lower = 0
    upper = 0
    spaces = 0
    punctuation = 0
    for i in range(0, len(arg[0])):
        if(arg[i].islower()):
            lower += 1
        elif(arg[i].isupper()):
            upper += 1
        elif(arg[i].isspace()):
            spaces += 1
        else:
            punctuation += 1
    print(upper, " upper letter(s)")
    print(lower, " lower letter(s)")
    print(punctuation, " punctuation mark(s)")
    print(spaces, " space(s)")

