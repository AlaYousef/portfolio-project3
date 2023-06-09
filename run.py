import time
import random
import textwrap
import sys
import platform  
import os

# questions list of dectionaries (question,answers,correct_answer)
questions = [
    {
        "question": "Which element got its name from the water"
        " it makes when burned?",
        "answers": ["1.iodine", "2.hydrogen", "3.tungsten",
                    "4.sodium"],
        "correct_answer": "2.hydrogen",
        "details": ("Hydrogen was first called “inflammable air”"
                    " before chemist Antoine Lavoisier renamed it"
                    " “water-former” (hydro + gen).")
    },
    {
        "question": "Uranium was named after which of the following?",
        "answers": ["1.a dog", "2.a planet", "3.a scientist", "4.a country"],
        "correct_answer": "2.a planet",
        "details": ("Uranium was discovered in 1789, shortly after the planet "
                    "Uranus was discovered. Neptunium and plutonium are "
                    "also named for  celestial bodies in our solar system.")
    },
    {
        "question": "Which of these metals is liquid at room temperature?",
        "answers": ["1.mercury", "2.nickel", "3.titanium", "4.zinc"],
        "correct_answer": "1.mercury",
        "details": ("Mercury, often called “quicksilver,” remains a liquid"
                    " until cooled to about −40 °F. Bromine is the only other"
                    " element that is liquid at room temperature.")
    },
    {
        "question":
        ("Which element is most abundant in both Earth’s crust and the"
         " human body?"),
        "answers": ["1.iron", "2.hydrogen", "3.silicon", "4.oxygen"],
        "correct_answer": "4.oxygen",
        "details":  "Oxygen constitutes nearly half of Earth’s crust"
                    " and two-thirds of a human body’s mass."
    },
    {
        "question": "Diamonds are made of which element?",
        "answers":  ["1.sulfur", "2.nitrogen", "3.lithium", "4.carbon"],
        "correct_answer": "4.carbon",
        "details": ("Contrary to popular belief, diamonds are not made"
                    " from coal, although both contain carbon.")
    },
    {
        "question": "What is the most common element found in all living"
                    " organisms?",
        "answers":  ["1.Oxygen", "2.Carbon", "3.Nitrogen", "4.Hydrogen"],
        "correct_answer": "2.Carbon",
        "details":  "Contrary to popular belief, diamonds are not"
                    " made from coal, although both contain carbon."

    },
    {
        "question": "Which element found in red blood cells helps carry"
                    " oxygen?",
        "answers":  ["1.iron", "2.boron", "3.calcium", "4.lead"],
        "correct_answer": "1.iron",
        "details": ("The iron in hemoglobin forms a reversible bond with "
                    " oxygen;they latch together in the lungs and then"
                    " split at the oxygen’s destination.")

    },
    {
        "question": "Which of these famous poisons appears in the periodic"
                    " table?",
        "answers": ["1.cyanide", "2.strychnine", "3.ricin", "4.arsenic"],
        "correct_answer": "4.arsenic",
        "details":  "Arsenic has been dubbed the “king of poisons” thanks"
                    " to its odorless and tasteless qualities."

    },
    {
        "question": "Elements, such as helium and neon, that tend to not"
                    " undergo chemical reactions are called what?",
        "answers": ["1.conservative gases", "2.lazy gases", "3.content gases",
                    "4.noble gases"],
        "correct_answer": "4.noble gases",
        "details": ("Just as a nobleman might avoid commoners,"
                    " so too do noble gases resist interacting with"
                    " other elements.")

    },
    {
        "question": "Which element’s name and symbol (Cu) comes from the "
                    " Latin name for Cyprus, where ancient Romans mined it?",
        "answers":  ["1.copper", "2.chromium", "3.calcium", "4.carbon"],
        "correct_answer": "4.copper",
        "details": ("The Romans called the element aes Cyprium"
                    " (“metal of Cyprus”), which was shortened to cyprium and"
                    " then corrupted to cuprum, eventually becoming copper.")

    },
    {
        "question": "Which element was discovered on the Sun before"
        " it was found on Earth?",
        "answers": ["1.helium", "2.potassium", "3.neon", "4.iodine"],
        "correct_answer": "1.helium",
        "details": ("Using a spectroscope in 1868, scientists first"
                    " detected helium on the Sun (from helios, the Greek word"
                    "  for “sun”) during an eclipse."
                    " Fourteen years later, helium was found on Earth.")
    },
    {
        "question": "Ancient Romans used which element to make plumbing?",
        "answers": ["1.gold", "2.titanium", "3.lead", "4.aluminum"],
        "correct_answer": "3.lead",
        "details": ("Because it is highly durable and resistant to corrosion,"
                    " lead (chemical symbol Pb from the Latin plumbum) was "
                    "used by the Romans to make water pipes as well as coins"
                    " and cooking utensils.By the time of Augustus Caesar,"
                    " lead poisoning had become an issue in Rome.")
    },
    {
        "question": "Which of these letters does not appear in the"
                    " periodic table, either as a symbol or in an element"
                    " name?",
        "answers": ["1. k", "2. x", "3. z", "4. j"],
        "correct_answer": "4. j",
        "details": ("The letter x can be found in xenon, z in zinc,"
                    " and k in krypton (among other places). The letter q "
                    "appears only in the extended periodic table in the name, "
                    "unbiquadium a placeholder term for the as yet "
                    "undiscovered element that will have the atomic "
                    " number 124.")
    },
    {
        "question": "Frequently used in flares, which element burns so"
                    " intensely that it can cause temporary blindness and"
                    " cannot be extinguished with water?",
        "answers": ["1.magnesium", "2.neon", "3.iodine", "4.silicon"],
        "correct_answer": "1.magnesium",
        "details": ("Magnesium has been used in flash photography,"
                    " pyrotechnics and incendiary bombs. When introduced"
                    " to a magnesium fire, water, is converted to a hydrogen"
                    " gas further fueling the flame.")
    },
    {
        "question": "Used by the Indigenous people of South America for"
        " metalcraft, which element comes from the Spanish word for “silver”?",
        "answers":  ["1.tin", "2.cobalt", "3.nickel", "4.platinum"],
        "correct_answer": "4.platinum",
        "details": ("Spaniards who arrived in South America found deposits"
                    " of the metal in Colombia’s Río Pinto and called it"
                    " platina del Pinto (“silver of the Pinto”).")

    }
]


def quiz_introduction():
    """
    Function show quiz information and instuctions
    """
    print("============================================================")
    print("|                                                          |")
    print("|             Welcome to Periodic Table Quiz               |")
    print("|                                                          |")
    print("============================================================")
    print()
    print("\n******************* Quiz Instructions ********************")
    print("The quiz consists of 15 questions, with four answer options.")
    print("You should choose one of answer options from (1 to 4)."
          " After complete the 15 questions you will get your score")
    print("Press Enter to start..\n")
    input()
    clear_screen()

    name = username_input()
    print(f"\nHello, {name}! Welcome to Periodic Table Quiz")
    time.sleep(1)
    print("Press Enter if you are ready to start the quiz..\n")
    input()
    print("Preparing quiz questions...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...\n")
    time.sleep(2)

    clear_screen()


def clear_screen():
    """
    Clears the screen based on the user's operating system.
    """
    # Check if Operating System is Mac and Linux or Windows
    if(platform.system().lower()=="windows"):
        cmdtorun='cls'
    else:
        cmdtorun='clear'   
    
    os.system(cmdtorun)
 


def username_input():
    """
    function that take name from user and return it
    """
    while True:
        try:
            user_input = input("First, please enter your name:  ")
            if user_input.isalpha():
                return user_input
                break
            else:
                raise ValueError(
                    f"Name should be characters"
                )

        except:
             print("Pleasr enter a valid name..")



def check_answer_input():
    """
    function has a while loop to check validation for answer option
    entered by user that should be a number between 1 and 4. The loop will
    repeatedly request data, until it is valid.
    """
    while True:
        try:
            answer_input = input("Enter answer number from (1-4):  ")
            answer_number = int(answer_input)
            if answer_number >= 1 and answer_number <= 4:
                return str(answer_number)
                break
            else:
                raise ValueError(
                    f"Answer option should be from 1 to 4"
                )
        except ValueError:
            print(f"Invalid data: please try again.\n")


def run_quiz():
    """
    function that run the game,
    fetch questions from questions list by for loop with answers
    option (nested for loop), then check if the user choose the correct
    answer or not by compare the first char in the correct answer which is
    the answer number with the number that the user enter by calling
    check_answer_input(). Increase score variable by 1 if answer is correct
    """
    os.system('clear')

    score = 0
    for index in (questions):
        print()
        random.shuffle(questions)
        print(index['question'])
        for answers in index['answers']:
            print(f"  {answers}")
        print()
        answer = check_answer_input()
        for value in index['answers']:
            if answer == index['correct_answer'][:1]:
                print(f"Good! Your answer is correct ⭐")
                print(index['details'])
                print()
                score += 1
                break
            else:
                print("Your answer is incorrect :(")
                print(f"The correct answer is: ")
                print(index['correct_answer'])
                break
    get_result(score)


def get_result(result):
    """
    function takes the score from run_quiz and display it to user,
    ask the user to play again by enter 'y' for (yes) or 'n' for (no).
    Run a while loop to until enter a valid string from the user
    via the terminal, which must be y or n. The loop will
    repeatedly request data, until it is valid.
    """
    print()
    if result >= 13:
        print("⭐⭐ Congratulations! ⭐⭐")
    print(f"Game Over.. Your score is {result} / {len(questions)} . \n")

    while True:
        try:
            play_again_input = input("Play Again? (y/n): ")
            if play_again_input.lower() == "y":
                os.system('clear')
                print()
                run_quiz()
                break
            elif play_again_input.lower() == "n":
                print("Thanks for you time:)")
                sys.exit()
            else:
                raise ValueError("n or y are only expected")
        except ValueError as e:
            print(f"Invalid input: please enter 'y' or 'n' to  exit.\n")


def main():
    quiz_introduction()
    run_quiz()


main()
