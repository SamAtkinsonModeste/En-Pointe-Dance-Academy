# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint
from pyfiglet import Figlet
dance_title = Figlet(font="georgia11", justify="center")
game_title = Figlet(font="doom", justify="center")

# colours for the print colour function
colours = ["light_grey", "light_red", "light_green",
           "light_blue", "light_magenta", "light_cyan", "light_yellow"]


# Colour Function
def print_colour(text, color):
    """
    Prints text in colours
    """
    return cprint(text, color, attrs=["bold"])


def game_title_intro_text():
    """
    Game Title and game intro text
    """
    print_colour(dance_title.renderText("En Pointe"), colours[3])
    print_colour(game_title.renderText("Dance Game"), colours[4])
    print_colour("En Pointe Dance Academy Adventure Game", colours[4])
    # print_color_light_blue("Step into the world of dance.")
    # print_color_light_blue(
    #     "Follow the journey of one of three unique dancers,")
    # print_color_light_blue("in their final year of En Pointe Dance Academy.")
    # print_color_light_magenta(
    #     "This is a story driven adventure, where every choice matters!")
    while True:
        try:
            print_colour("Ready to start your adventure?", colours[0])
            print_colour(
                "When the music starts, a dancer knows when to start dancing,", colours[4])
            print_colour(
                "because the teacher shouts 4 numbers to the beat of the music.", colours[4])
            start_game = input(colored("So Type: 5, 6, 7, 8\n",
                               "light_grey", attrs=["bold"]))
            if start_game != "5,6,7,8":
                raise ValueError("Error: Did you type the right numbers?")

            print_colour(
                "Great, lets introduce you to the adventure.", colours[2])
            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])


game_title_intro_text()
