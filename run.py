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
        game_title.renderText("En Pointe Dance Academy Game"))
    print_color_light_blue("Step into the world of dance")
    print_color_light_blue("and follow the journeys of three unique dancers,")
    print_color_light_blue("in their final year of En Pointe Dance Academy")


game_title_intro_text()
