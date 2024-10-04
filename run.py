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
                print(type(next_display))
                print(value_text)
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
            next_display = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            value_text = next_display
            if value_text not in options:
                print(type(value_text))
                print(value_text)
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
    disagree = "n"
    while disagree:
        chose_gender = check_errors_list_inputs(
            "Type Male or Female", male_female, "Did You type Male or Female?")
        chose_gender
        character_gender = chose_gender
        if character_gender == "male":
            male = character_gender
            print_colour(f"You chose {male}", colours[5])

        if character_gender == "female":
            female = character_gender
            print_colour(f"You chose {female}", colours[4])

        agree_disagree = check_errors_list_inputs(
            f"Is {character_gender} correct?\n"
            "Type Y for Yes or N for No:", yes_no, "Did you type Y or N")
        if agree_disagree == agree:
            print(character_gender)
            return character_gender

        break


def student_name(person, names):
    yes_no = ["y", "n"]
    agree = "y"
    disagree = "n"

    while disagree:
        print_colour(f"You can create a name for your {person}", colours[2])
        print_colour("Or select one from suggested names.", colours[2])
        name_character = check_errors_list_inputs("Would you like "
                                                  "to create a name?\n"
                                                  " Type Y for Yes"
                                                  " and N for No",
                                                  yes_no,
                                                  "Did you type Y or N")
        name_character

        if name_character == agree:
            create_name = name_character
            create_name = input("Type a first name only:")
            create_name
            print(create_name)

            return create_name
        else:
            if disagree:
                choose_name = check_errors_list_inputs(f"Choose from:{names}",
                                                       names,
                                                       "Did you type"
                                                       " the name correctly?")
                choose_name

                return choose_name

        break


def students_info(people):
    choice = ["a", "b", "c"]
    for student in data[people]:
        print(colored(f"Id: {student['id']}\n", "light_yellow",
                      attrs=["bold"]),
              colored(
                  f"Background:\n {student['background']}\n",
                  "light_cyan",
            attrs=['bold']),
            colored("Personality:\n"
                    f" {student['personality']}\n\n",
                    "light_grey",
                    attrs=['bold']))
    chosen_person = check_errors_list_inputs(
        "Would you like A, B or C ", choice, "Did you type A, B or C?")

    return chosen_person


def create_character():
    """
   The player can create their character.
   They can choose male or female and create a name.
They will have a choice of three background and personalities
for their character as well as a choice of secret talents.
    """
    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour("You can create your own character.\n"
                 "Let's start by choosing:", colours[5])
    print(colored("Male", "light_cyan", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Female", "light_magenta", attrs=["bold"]))

    player_gender = chose_gender()
    player_gender
    male_names = ["liam", "jordan", "ethan"]
    female_names = ["zoe", "maya", "sophie"]

    if player_gender == "male":
        male_character = player_gender
        male_student_name = student_name(
            colored(f"{male_character} student.",
                    "light_cyan", attrs=['bold']),
            male_names)
        male_student_name
        print_colour(f"You chose: {male_student_name}", colours[5])

    if player_gender == "female":
        female_character = player_gender
        female_student_name = student_name(
            colored(f"{female_character} student.",
                    "light_magenta", attrs=['bold']),
            female_names)
        female_student_name
        print_colour(f"You chose: {female_student_name}", colours[4])


if __name__ == "__main__":
    game_play()
    about_game()
    create_character()
