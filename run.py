# importing emoji library and coloured, cprint from termcolor
import emoji
import os
from termcolor import colored, cprint
from pyfiglet import Figlet
georgia11_font = Figlet(font="georgia11")
doom_font = Figlet(font="doom")
bolger_font = Figlet(font="bolger")

# colours for the print colour function
colours = ["light_grey", "light_red", "light_green",
           "light_blue", "light_magenta", "light_cyan", "light_yellow"]


# Colour Function
def print_colour(text, color):
    """
    Prints text in colours
    """
    return cprint(text, color, attrs=["bold"])


class Student:
    """
    Student class
    """

    def __init__(self, name, about, secret):
        self.name = name
        self.about = about
        self.secret = secret

    def description(self):
        """
        Describes the student
        """
        return f"{self.name}\n{self.about}\n{self.secret}"


# Dance Student Characters
zoe = Student('Zoe', emoji.emojize(
    "A rebellious triple-threat dancer.:fire:"),
    'Torn between jazz and ballet,\n'
    'hiding her true dream\n'
    'to be a principal ballerina.\n')

sara = Student('Sara', emoji.emojize(
    "A determined ballet dancer,:flexed_biceps:"),
    'struggling with technique and self-confidence,\n'
    'trying to reconnect with the passion\n'
    'for dance she has lost with her confidence.\n')

lily = Student('Lily', emoji.emojize(
    "A technically perfect ballerina, :ballet_shoes:"),
    'facing intense pressure from her overbearing mother\n'
    'to be a principle ballerina, when,'
    'secretly dreaming of a career in singing.\n')


class Reactions:
    """
    Character reactions which the player chooses.
    """

    def __init__(self, positive, neutral, negative):
        self.positive = positive
        self.neutral = neutral
        self.negative = negative

    def reaction_positive(self):
        return f'{self.positive}'

    def reaction_neutral(self):
        return f'{self.neutral}'

    def reaction_negative(self):
        return f'{self.negative}'


def check_errors(input_text, error_text):
    """
    Cheaks for errors in inputs and sends error meesages to the user
    also clears the terminal once enter is hit
    """
    while True:
        try:
            next_display = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            if next_display != f"{input_text}":
                print(type(next_display))
                print(next_display)
                raise ValueError(f"{error_text}")
            else:
                next_clear()
                break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])


def next_clear():
    """
    Clears the terminal as if turning the pages of a book
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def about_game():
    """
    Tells the player what is expected of them and how to play
    """
    print_colour(doom_font.renderText("How To Play"), colours[5])
    print_colour(
        "This is a story driven adventure,"
        "where every choice matters!\n"
        "You can choose to follow"
        " one of the three"
        " character dance students.\n"
        "You will be in control of"
        " their future through your choices!\n"
        "You decide if their thougts or answers are:", colours[4])
    print(colored("Positive,", "light_green", attrs=["bold"]),
          colored("Neutral,", "light_blue", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Negative\n", "light_red", attrs=["bold"]))
    print_colour("When does a dancer know"
                 " when to start dancing a rountine?\n"
                 "It would be the teacher who"
                 " shouts out 4 numbers"
                 " to the beat of the music.\n"
                 "Those numbers are:", colours[3])
    print_colour("5,6,7,8", colours[6])


def meet_the_characters():
    """
    Introduces the player to the characters.
    Player gets to choose which one to play as.
    """
    print_colour(doom_font.renderText("Students"), colours[5])
    print_colour("Meet the three dance student"
                 " charcters\n"
                 "to choose from:", colours[5])
    print_colour(zoe.description(), colours[3])
    print_colour(sara.description(), colours[4])
    print_colour(lily.description(), colours[6])

    while True:
        try:
            character = input(colored("Type character name:\n",
                                      "light_grey",
                                      attrs=["bold"])).lower()
            characters = ["zoe", "lily", "sara"]
            if character not in characters:
                raise ValueError("You typed "
                                 f"{character.capitalize()}.\n"
                                 "Please type one of the character's names "
                                 "and check the spelling.")
            print(character)
            next_clear()
            return character

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again.", colours[2])


def game_play():
    """
    Main game play function
    """
    print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Academy"), colours[5])
    print_colour('Step into the world of dance\n'
                 'and follow the journeys of three unique dancers\n'
                 'in their final year at the prestigious\n'
                 'En Pointe Dance Academy!', colours[4])

    while True:
        try:
            next_display = input(colored(
                "Type Next:\n", "light_grey", attrs=["bold"])).lower()
            if next_display != "next":
                raise ValueError("Did you type Next?")

            next_clear()
            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

    about_game()

    while True:
        try:
            next_display = input(colored(
                "To begin type: 5,6,7,8\n",
                "light_grey", attrs=["bold"])).lower()
            if next_display != "5,6,7,8":
                raise ValueError("Did you type 5,6,7,8?")

            next_clear()
            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

    meet_the_characters()


game_play()
