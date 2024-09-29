# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint
from pyfiglet import Figlet
georgia11_font = Figlet(font="georgia11")
doom_font = Figlet(font="doom")
bolger_font = Figlet(font="bolger")

# colours for the print colour function
colours = ["light_grey", "light_red", "light_green",
           "light_blue", "light_magenta", "light_cyan", "light_yellow"]

# STUDENT Character Functions


def student_zoe():
    """
    Student Zoe's character description
    """
    print_colour("Zoe", colours[3])
    print_colour(emoji.emojize(
        "A rebellious :fire: triple-threat dancer,"), colours[3])
    print_colour("torn between jazz and ballet,", colours[3])
    print_colour(
        "hiding her true dream to be a principal ballerina.\n", colours[3])


def student_sara():
    """
    Student Sara's character description
    """
    print_colour("Sara", colours[5])
    print_colour(emoji.emojize(
        "A determined ballet dancer,:flexed_biceps:"), colours[5])
    print_colour("struggling with technique and self-confidence,", colours[5])
    print_colour(
        "trying to rediscover the passion in her movements.\n", colours[5])


def student_lily():
    """
    Student Lily's character description
    """
    print_colour("Lily", colours[6])
    print_colour(emoji.emojize(
        "A technically perfect ballerina, :ballet_shoes:"), colours[6])
    print_colour(
        "facing intense pressure from her overbearing mother,", colours[6])
    print_colour(
        "secretly dreaming of a career in singing.", colours[6])


def start_adventure():
    """
    Information about the adventure storyline
    """
    print_colour(doom_font.renderText("Dance Academy"), colours[5])
    print_colour(
        "Follow the journey of one of", colours[3])
    print_colour(
        "three unique dance students,", colours[3])
    print_colour("in their final year of En Pointe Dance Academy.", colours[3])
    print_colour(
        "This is a story driven adventure,", colours[4])
    print_colour(" where every choice matters!", colours[4])
    print_colour("Lets meet our three student dance characters!\n", colours[5])


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
    # print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Game\n\n"), colours[4])
    print_colour("En Pointe Dance Academy Adventure Game\n\n", colours[4])
    while True:
        try:
            print_colour(
                "Ready to step into the world of dance?\n", colours[0])
            print_colour(
                "When the music starts,", colours[4])
            print_colour(
                "a dancer knows when to start dancing,", colours[4])
            print_colour(
                "because the teacher shouts 4 numbers,", colours[4])
            print_colour(
                "to the beat of the music.", colours[4])
            start_game = input(colored("So Type: 5, 6, 7, 8\n",
                               "light_grey", attrs=["bold"]))
            if start_game != "5,6,7,8":
                raise ValueError(
                    "Error: Did you type 5,6,7,8  ?")

            print_colour(
                "Great, lets introduce you to the adventure.\n", colours[2])
            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])


game_title_intro_text()
start_adventure()
student_zoe()
student_sara()
student_lily()
