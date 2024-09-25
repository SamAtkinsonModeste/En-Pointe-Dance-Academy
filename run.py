# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint


def print_blue_on_grey(x): return cprint(x, "red", "on_grey")


def print_red_on_cyan(x): return cprint(x, "red", "on_cyan")


def introduction():
    print_red_on_cyan("It is the first day back for the final year,")
    print_blue_on_grey("for the third year students of:")
    print_blue_on_grey(emoji.emojize(
        "En Pointe Dance Acacdemy :graduation_cap:"))
    cprint("Everyone was excited", "magenta")
    print("checking what color this will be.")


print_red_on_cyan("My story is what colour here?")
print_red_on_cyan("Hello, Universe!")
introduction()
