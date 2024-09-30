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


zoe = Student('Zoe', emoji.emojize(
    "A rebellious triple-threat dancer.:fire:"),
    'Torn between jazz and ballet,\n'
    'hiding her true dream\n'
    'to be a principal ballerina.')
# print_colour(zoe.description(), colours[3])

sara = Student('Sara', emoji.emojize(
    "A determined ballet dancer,:flexed_biceps:"),
    'struggling with technique and self-confidence,\n'
    'trying to reconnect with the passion\n'
    'for dance she has lost with her confidence.')
# print_colour(sara.description(), colours[5])

lily = Student('Lily', emoji.emojize(
    "A technically perfect ballerina, :ballet_shoes:"),
    'facing intense pressure from her overbearing mother\n'
    'to be a principle ballerina, when,'
    'secretly dreaming of a career in singing.')
# print_colour(lily.description(), colours[6])


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


# def choose_character():


def game_play():
    """
    Main game play function
    """
    print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Academy Game"), colours[4])


game_play()
