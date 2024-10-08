# importing json, emoji library and coloured, cprint from termcolor
import json
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

with open("dialog-reactions.json", "r") as file:
    data = json.load(file)

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
        about_me = print_colour(f"My name is {self.name}"
                                f" My secret talent is {self.secret}",
                                colours[3])
        return about_me

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


def check_errors_inputs(input_text, value_text, error_text):
    """
    Cheaks for errors in inputs and sends error meesages to the user
    also clears the terminal once enter is hit
    """
    while True:
        try:
            next_display = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            if next_display != f"{value_text}":
                raise ValueError(f"{error_text}")

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

        else:
            next_clear()
            return value_text


def check_errors_list_inputs(input_text, options, error_text):
    """
    Cheaks for errors in inputs and checks if
    input value is in a list. Sends error message to the user
    also clears the terminal once enter is hit
    """
    while True:
        try:
            value_text = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()

            if value_text not in options:
                raise ValueError(f"{error_text}")

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

        else:
            return value_text


def next_clear():
    """
    Clears the terminal as if turning the pages of a book
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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
    check_errors_inputs("To continue type: Next",
                        "next", "Did you type: Next?")


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

    check_errors_inputs("To begin type: 5,6,7,8", "5,6,7,8",
                        "Did you type:  5,6,7,8 ?")


def chose_gender():
    """
   Gives the player a choice of gender for their character
   The player is asked a yes or no queston so they can change
   the gender if they wish.
    """
    male_female = ["male", "female"]
    yes_no = ["y", "n"]
    agree = "y"
    disagree = True

    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour(doom_font.renderText("Gender"), colours[5])
    print_colour("You can create your own character.\n"
                 "Let's start by choosing:", colours[5])
    print(colored("Male", "light_cyan", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Female", "light_magenta", attrs=["bold"]))

    while disagree:
        chose_gender = check_errors_list_inputs(
            "Type Male or Female", male_female, "Did You type Male or Female?")

        if chose_gender == "male":
            male = chose_gender
            print_colour(f"You chose {male}", colours[5])

        if chose_gender == "female":
            female = chose_gender
            print_colour(f"You chose {female}", colours[4])

        agree_disagree = check_errors_list_inputs(
            f"Is {chose_gender} correct?\n"
            "Type Y for Yes or N for No:", yes_no, "Did you type Y or N")
        if agree_disagree == agree:
            disagree = False
            return chose_gender

        print_colour("Please reselect:", colours[6])


def student_name():
    yes_no = ["y", "n"]
    agree = "y"
    disagree = "n"
    f_names = ["zoe", "maya", "lily"]
    m_names = ["liam", "jordan", "ethan"]

    next_clear()
    while disagree:
        print_colour(doom_font.renderText("Character Build"), colours[5])
        print_colour(doom_font.renderText("Name"), colours[5])
        print_colour(
            f"You can create a name for your {gender} student", colours[2])
        print_colour("Or select one from suggested names.", colours[2])
        name_character = check_errors_list_inputs("Would you like "
                                                  "to create a name?\n"
                                                  " Type Y for Yes"
                                                  " and N for No",
                                                  yes_no,
                                                  "Did you type Y or N")

        if name_character == agree:
            create_name = name_character
            create_name = input(
                colored("Type a first name only: ", "light_yellow",
                        attrs=["bold"]))
            if gender == "female":
                create_name = colored(
                    create_name.capitalize(), "light_magenta", attrs=["bold"])

            if gender == "male":
                create_name = colored(
                    create_name.capitalize(), "light_cyan", attrs=["bold"])
            print_colour("You have chosen the name:", colours[0])
            print(f" {create_name} ")
            next_clear()
            return create_name

        else:

            if gender == "female":
                names = colored(
                    f_names, "light_magenta", attrs=["bold"])

            if gender == "male":
                names = colored(m_names, "light_cyan", attrs=["bold"])

            if disagree:
                choose_name = check_errors_list_inputs("Choose from these"
                                                       f" {gender} names:"
                                                       f"{names}",
                                                       names,
                                                       "Did you type"
                                                       " the name correctly?")

                if gender == "female":
                    choose_name = colored(
                        choose_name.capitalize(), "light_magenta",
                        attrs=["bold"])
                else:
                    choose_name = colored(
                        choose_name.capitalize(), "light_cyan", attrs=["bold"])

            print_colour("You have chosen the name:", colours[0])
            print(f"{choose_name}")
            next_clear()
            return choose_name


def students_info():
    choice = ["a", "b", "c"]

    if gender == "female":
        people = "female-students"
    if gender == "male":
        people = "male-students"

    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour(doom_font.renderText("Characteristics"), colours[5])
    print_colour(
        "You will be shown three characteristics to choose from.", colours[2])
    print_colour("Each one will consist of:", colours[2])
    print_colour("Background:", colours[5])
    check_errors_inputs("Are you ready to view them? Type: OK", "ok",
                        "Did you type:  Ok ?")

    next_clear()

    for student in data[people]:
        print(colored(
            f"Background:\n {student['background']}\n",
            "light_cyan",
            attrs=['bold']),)
    chosen_person = check_errors_list_inputs(
        "What character traits would you like to chose from: A, B or C ",
        choice, "Did you type A, B or C?")

    if chosen_person == "a":
        chosen_person = print(colored(
            f"Background:\n {data[people][0]['background']}\n",
            "light_cyan",
            attrs=['bold']))

    elif chosen_person == "b":
        chosen_person = print(colored(
            f"Background:\n {data[people][1]['background']}\n",
            "light_cyan",
            attrs=['bold']))
    elif chosen_person == "c":
        chosen_person = print(colored(
            f"Background:\n {data[people][2]['background']}\n",
            "light_cyan",
            attrs=['bold']))

    return chosen_person


def secrets():
    # next_clear()
    choices = ["a", "b", "c", "d"]
    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour(doom_font.renderText("Secret Talents"), colours[5])
    print_colour(
        "You will be shown four secret talents to choose from.", colours[2])
    check_errors_inputs("Are you ready to view them? Type: OK", "ok",
                        "Did you type:  Ok ?")

    hidden_talent = data["secrets"]

    for talent in hidden_talent:
        print(colored(
            f"{talent['secret']}\n",
            "light_yellow",
            attrs=['bold']),)
    secret_talent = check_errors_list_inputs(
        "What character traits would you like to chose from: A, B, C or D ",
        choices, "Did you type A, B, C, or D ?")

    if secret_talent == "a":
        secret_talent = print_colour(hidden_talent[0]["secret"], colours[3])

    elif secret_talent == "b":
        secret_talent = print_colour(hidden_talent[1]["secret"], colours[3])

    elif secret_talent == "c":
        secret_talent = print_colour(hidden_talent[2]["secret"], colours[3])

    elif secret_talent == "d":
        secret_talent = print_colour(hidden_talent[3]["secret"], colours[3])

    return secret_talent


def create_character():
    """

    """
    name = student_name()
    about = students_info()
    secret = secrets()
    student_character = Student(f"{name}",
                                f"{about}", f"{secret}")

    return student_character


if __name__ == "__main__":
    game_play()
    about_game()
    gender = chose_gender()
    print(gender)
    player = create_character()
    print(player)
    print(player.description())
    print(f"I am class instance {player.name}")
    print(player.about)
    print(player.secret)
