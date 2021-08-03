#
# python: 3.6.4
#
# author: Michael
#
#
# Purpose the tech academy - python course, creating our first program together. Demonstrating how to pass variables
# from function to function
from colorama import init, Fore, Back, Style

# essential for Windows environment
init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def get_name():
    name = input("What is your name?")
    return name

def start(nice=0, mean=0, name=""):
    # get users name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    """
    check if this is a new game or not.
    if it is new, get the users name.
    if it is not a new game thank the player
    for playing again and continue with the game
    """
    if name != "":
        print("\n thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print_with_color("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be "
                          "nice or mean", color=Fore.GREEN, brightness=Style.BRIGHT)
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \n conversation. Will you be nice \n or mean? (N/M) \n>>>:").lower()
        if pick == "n":
            print_with_color("\nthe stranger walks away smiling...", color=Fore.CYAN, brightness=Style.BRIGHT)
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\n The stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:  # if condition is valid, call win function passing in the variable so it can use them
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)


def lose(nice, mean, name):
    print("\nAhhh too bad, game over! \n(), you live in a dirty beat-up \nvan by the river, wretched and alone!".format(
        name))
    again(nice, mean, name)


def win(nice, mean, name):
    print("\nNice job(), you win! \n Everyone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again(y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (y) for 'Yes', ( n ) for 'No':\n >>")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # notice i do not reset the name variable as that same user has elected to play again
    start(nice, mean, name)

if __name__ == "__main__":
    start()
