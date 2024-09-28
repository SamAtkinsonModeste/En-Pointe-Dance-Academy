# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint
from pyfiglet import Figlet
dance_title = Figlet(font="georgia11", justify="center")
game_title = Figlet(font="doom", justify="center")


# Colour Functions


def print_color_light_magenta(text):
    """
    Colours text a light magenta
    """
    return cprint(text, "light_magenta", attrs=["bold"])


def print_color_light_blue(text):
    """
    Colours text a light blue
    """
    return cprint(text, "light_blue")


def print_color_light_red(text):
    """
    Colours text a light red
    """
    return cprint(text, "light_red", attrs=["bold"])


def print_color_light_yellow(text):
    """
    Colours text a light yellow
    """
    return cprint(text, "light_yellow", attrs=["bold"])


def print_color_light_grey(text):
    """
    Colours text a light grey
    """
    return cprint(text, "light_grey", attrs=["bold"])


def print_color_light_green(text):
    """
    Colours text a light green
    """
    return cprint(text, "light_green", attrs=["bold"])


def game_title_intro_text():
    """
    Game Title and game intro text
    """
    print_color_light_blue(dance_title.renderText("En Pointe"))
    print_color_light_magenta(game_title.renderText("Dance Game"))
    print_color_light_magenta("En Pointe Dance Academy Adventure Game")
    print_color_light_blue("Step into the world of dance.")
    print_color_light_blue(
        "Follow the journey of one of three unique dancers,")
    print_color_light_blue("in their final year of En Pointe Dance Academy.")
    print_color_light_magenta(
        "This is a story driven adventure, where every choice matters!")
    while True:
        try:
            print_color_light_grey("Ready to start your adventure?")
            print_color_light_magenta(
                "When the music starts, a dancer knows when to start dancing,")
            print_color_light_magenta(
                "because the teacher shouts 4 numbers to the beat of the music.")
            start_game = input(colored("So Type: 5, 6, 7, 8\n",
                               "light_grey", attrs=["bold"]))
            if start_game != "5,6,7,8":
                raise ValueError("Error: Did you type the right numbers?")

            print_color_light_green(
                "Great, lets introduce you to our three dance characters.")
            break

        except ValueError as e:
            print_color_light_red(e)
            print_color_light_yellow("Try again")


game_title_intro_text()
