import sys
cookbook = []


class recipe:
    ingredients = []
    name = ""
    type = ""
    t_preparation = 0


def print_recipe():
    print(cookbook)


def print_details():
    print(1)


def delete_recipe():
    print(1)


def add_recipe():
    obj = recipe()
    print(">>> Enter a name:")
    obj.name = input()
    print(">>> Enter ingredients:")
    while(True):
        av = sys.stdin.readline()
        if av.empty:
            break
        obj.ingredients.insert(av)
    print(">>> Enter a meal type:")
    obj.type = input()
    print(">>> Enter a preparation time:")
    obj.t_preparation = int(input())
    print(1)


def info():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("   1: Add a recipe")
    print("   2: Delete a recipe")
    print("   3: Print a recipe")
    print("   4: Print the cookbook")
    print("   5: Quit")


info()
while(True):
    print("Please select an option:")
    index = input()
    if(index == '1'):
        add_recipe()
    if index == '3':
        print_recipe()
    exit(1)
