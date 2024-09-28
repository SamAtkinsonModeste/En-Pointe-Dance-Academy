# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint
from pyfiglet import Figlet
game_title = Figlet(font="georgia11", justify="center")


# Colour Functions


def print_color_light_magenta(text):
    """
    Colours text a light magenta
    """
    return cprint(text, "light_magenta")


def print_color_light_blue(text):
    """
    Colours text a light blue
    """
    return cprint(text, "light_blue")


def game_title_intro_text():
    """
    Game Title and game intro text
    """
    print_color_light_magenta(
        game_title.renderText("En Pointe Dance"))
    print_color_light_magenta("En Pointe Dance Academy Adventure Game")
    print_color_light_blue("Step into the world of dance")
    print_color_light_blue(
        "and follow the journeys of three unique dancers,")
    print_color_light_blue(
        "in their final year of En Pointe Dance Academy")
    print_color_light_magenta(
        "This is a story driven adventure, where every choice matters!")
    while True:
        try:
            print("Ready to start your adventure?")
            print("Dancers start routines with 4 numbers")
            start_game = input("Enter 5,6,7,8: ")
            if start_game != "5,6,7,8":
                raise ValueError("Did you call the right numbers?")

            print("Great, lets introduce you to our three dancers.")
            break

        except ValueError as e:
            print(e)
            print("Try again")


game_title_intro_text()
