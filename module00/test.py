
import sys

def affich():
    print("no")

def affich(*av):
    print("asdf")
    if(len(av) == 0):
        return
    print(av[1])

