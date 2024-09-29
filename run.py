# importing emoji library and coloured, cprint from termcolor
import emoji
from termcolor import colored, cprint
from pyfiglet import Figlet
georgia11_font = Figlet(font="georgia11")
doom_font = Figlet(font="doom")
bolger_font = Figlet(font="bolger")


lily_positive_react = [emoji.emojize(
    "I've got this! Maybe I'll get to sing too :microphone:")]
lily_neutral_react = [emoji.emojize(
    "Is ballet being true to myself :thinking_face:")]
lily_negative_react = [emoji.emojize(
    "I don't want to let my mum down :anxious_face_with_sweat:")]


# colours for the print colour function
colours = ["light_grey", "light_red", "light_green",
           "light_blue", "light_magenta", "light_cyan", "light_yellow"]


# Colour Function
def print_colour(text, color):
    """
    Prints text in colours
    """
    return cprint(text, color, attrs=["bold"])


# starting functioning
def game_title_intro_text():
    """
    Game Title and game intro text
    """
    # print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Game"), colours[4])
    print_colour("En Pointe Dance Academy Adventure Game", colours[4])
    while True:
        try:
            print_colour(
                "Ready to step into the world of dance?", colours[0])
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


# Start the adventure leads to introduction of characters function
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


# STUDENT Character Functions
def student_zoe():
    """
    Student Zoe's character description
    """
    print_colour("Zoe", colours[5])
    print_colour(emoji.emojize(
        "A rebellious :fire: triple-threat dancer,"), colours[3])
    print_colour("torn between jazz and ballet,", colours[3])
    print_colour(
        "hiding her true dream to be a principal ballerina.\n", colours[3])


def student_sara():
    """
    Student Sara's character description
    """
    print_colour("Sara", colours[4])
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
        "secretly dreaming of a career in singing.\n", colours[6])


def choose_character():
    """
    Player chooses which character's journey they will follow.
    """
    print_colour("Which charcter's journey", colours[0])
    print_colour("would you like to follow?", colours[0])
    while True:
        try:
            print_colour("Zoe?", colours[3])
            print_colour("Sara?", colours[4])
            print_colour("Lily?", colours[6])

            character_choice = input(
                colored("Enter the name of the character:\n", "light_grey",
                        attrs=["bold"])).lower()
            print(character_choice)
            characters = ["zoe", "sara", "lily"]
            if character_choice not in characters:
                raise ValueError(
                    f"Error:{character_choice.capitalize()} is not correct?")

            print_colour(
                f"You chose: {character_choice.capitalize()}\n", colours[0])
            first_day()

            student_reaction(character_choice)

            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])


def first_day():
    """
    The character Derek St James the director of the academy talks to the third years.
    """
    print_colour(
        "Derek St James the director of En Pointe Academy.", colours[0])
    print_colour("Gives a speech to the third years,", colours[0])
    print_colour("about their final year.\n", colours[0])
    f = open("teachers/derek.txt", "r")
    lines = f.read()
    f.close()
    print_colour(lines, colours[5])


def student_reaction(student):
    print_colour(f"What is {student} thinking?", colours[5])
    while True:
        try:
            print_colour("Is it Positive?", colours[2])
            print_colour("Is it Neutral?", colours[0])
            print_colour("Is it Negative?", colours[1])
            decision = input(colored("Type: Pos, Neut or Neg\n",
                             "light_cyan", attrs=["bold"])).lower()
            reactions = ["pos", "neut", "neg"]
            if decision not in reactions:
                raise ValueError(
                    f"Error: Your reaction was {decision.capitalize()}.")
            if student == "lily":
                print_colour(f"{student.capitalize()} says:\n",
                             colours[6])
            elif student == "zoe":
                print_colour(f"{student.capitalize()} says:\n",
                             colours[5])
            elif student == "sara":
                print_colour(f"{student.capitalize()} says:\n",
                             colours[4])

            if student == "lily" and decision == "pos":
                print_colour(lily_positive_react[0], colours[6])
            elif student == "lily" and decision == "neut":
                print_colour(lily_neutral_react[0], colours[6])
            elif student == "lily" and decision == "neg":
                print_colour(lily_negative_react[0], colours[6])
            elif student == "zoe" and decision == "pos":
                print_colour(lily_positive_react[0], colours[6])

            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[6])


game_title_intro_text()
start_adventure()
student_zoe()
student_sara()
student_lily()
choose_character()
