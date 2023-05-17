import time
import random
import textwrap
import sys
import os

# questions list of dectionaries (question,answers,correct_answer)
questions = [
    {
        "question":"Which element got its name from the water it makes when burned?",
        "answers":
        ["iodine", "hydrogen", "tungsten","sodium"],
        "correct_answer": "hydrogen",
        "details": ("Hydrogen was first called “inflammable air” "
        " before chemist Antoine Lavoisier renamed it “water-former” (hydro + gen).")
    },
    {
        "question": "Uranium was named after which of the following?",
        "answers":
        ["a dog", "a planet", "a scientist", "a country"],
        "correct_answer": "a planet",
        "details": ("Uranium was discovered in 1789, shortly after the planet Uranus was discovered." 
        " Neptunium and plutonium are also named for celestial bodies in our solar system.")

    },
    {
        "question": "Which of these metals is liquid at room temperature?",
        "answers":
        ["mercury", "nickel", "titanium", "zinc"],
        "correct_answer": "mercury",
        "details": ("Mercury, often called “quicksilver,” remains a liquid until cooled to about −40 °F."
        " Bromine is the only other element that is liquid at room temperature.")
    },
    {
        "question":
        ("Which element is most abundant in both Earth’s crust and the human body?"
         " into energy?"),
        "answers":
        ["iron", "hydrogen", "silicon", "oxygen"],
        "correct_answer": "oxygen",
        "details": "Oxygen constitutes nearly half of Earth’s crust and two-thirds of a human body’s mass."

    },
    {
        "question": "Diamonds are made of which element?",
        "answers":
        ["sulfur", "nitrogen", "lithium","carbon"],
        "correct_answer": "carbon",
        "details": ("Contrary to popular belief, diamonds are not made from coal, although both contain carbon.")

    },
    {
        "question": "What is the most common element found in all living organisms?",
        "answers":
        ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon",
        "details": "Contrary to popular belief, diamonds are not made from coal, although both contain carbon."

    },
    {
        "question":"Which element found in red blood cells helps carry oxygen?",
        "answers":
        ["iron", "boron", "calcium","lead"],
        "correct_answer": "iron",
        "details": ("The iron in hemoglobin forms a reversible bond with oxygen;"
        " they latch together in the lungs and then split at the oxygen’s destination.")

    },
    {
        "question": "Which of these famous poisons appears in the periodic table?",
        "answers":
        ["cyanide", "strychnine", "ricin", "arsenic"],
        "correct_answer": "arsenic",
        "details": "Arsenic has been dubbed the “king of poisons” thanks to its odorless and tasteless qualities."

    },
    {
        "question":"Elements, such as helium and neon, that tend to not undergo chemical reactions are called what?",
        "answers":
        ["conservative gases", "lazy gases", "content gases", "noble gases"],
        "correct_answer": "noble gases",
        "details": ("Just as a nobleman might avoid commoners,"
        " so too do noble gases resist interacting with other elements.")

    },
    {
        "question": "Which element’s name and symbol (Cu) comes from the Latin name for Cyprus, where ancient Romans mined it?",
        "answers":
        ["copper", "chromium", "calcium", "carbon"],
        "correct_answer": "copper",
        "details": ("The Romans called the element aes Cyprium (“metal of Cyprus”),"
        " which was shortened to cyprium and then corrupted to cuprum, eventually becoming copper.")

    },
    {
        "question": "Which element was discovered on the Sun before it was found on Earth?",
        "answers":
        ["helium", "potassium", "neon", "iodine"],
        "correct_answer": "helium",
        "details": ("Using a spectroscope in 1868, scientists first detected helium on the Sun (from helios, the Greek word for “sun”) during an eclipse."
        " Fourteen years later, helium was found on Earth.")

    },
    {
        "question": "Ancient Romans used which element to make plumbing?",
        "answers":
        ["gold", "titanium", "lead", "aluminum"],
        "correct_answer": "lead",
        "details": ("Because it is highly durable and resistant to corrosion, lead (chemical symbol Pb from the Latin plumbum) "
        "was used by the Romans to make water pipes as well as coins and cooking utensils."
        " By the time of Augustus Caesar, lead poisoning had become an issue in Rome.")

    },
    {
        "question": "Which of these letters does not appear in the periodic table, either as a symbol or in an element name?",
        "answers":
        ["k", "x", "z", "j"],
        "correct_answer": "j",
        "details": ("The letter x can be found in xenon, z in zinc, and k in krypton (among other places)."
        " The letter q appears only in the extended periodic table in the name unbiquadium, "
        "a placeholder term for the as yet undiscovered element that will have the atomic number 124.")

    },
    {
        "question":
        ("Frequently used in flares, which element burns so intensely that it can "
        "cause temporary blindness and cannot be extinguished with water?"),
        "answers":
        ["magnesium", "neon", "iodine", "silicon"],
        "correct_answer": "magnesium",
        "details": ("Magnesium has been used in flash photography, pyrotechnics, and incendiary bombs."
        "When introduced to a magnesium fire, water is converted to a hydrogen gas, further fueling the flame.")

    },
     {
        "question":
        ("Used by the Indigenous people of South America for metalcraft,"
        " which element comes from the Spanish word for “silver”?"),
        "answers":
        ["tin", "cobalt", "nickel", "platinum"],
        "correct_answer": "platinum",
        "details": ("Spaniards who arrived in South America found deposits of the metal in Colombia’s "
        "Río Pinto and called it platina del Pinto (“silver of the Pinto”).")

    }
]


def quiz_introduction():
    """
    Function show quiz information and  instuctions
    """
    print("============================================================")
    print("|                                                          |")
    print("|             Welcome to Periodic Table Quiz               |")
    print("|                                                          |")
    print("============================================================")
    time.sleep(1)
    print("\n******************* Quiz Instructions ********************")
    print("The quiz consists of 15 questions, with four answer options.") 
    print("You should choose one of answer options from (1 to 4)."
    " After complete the 15 questions you will get your score")
    time.sleep(6)
    clear_screen()

    name = input_value()
    
    print("\nHello, {name}! Welcome to Periodic Table Quiz")
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
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def input_value():
    """
    function that take name from user and return it
    """
    user_input  = input("First, please enter your name:  ")
    return user_input

def run_quiz():
    print(questions)


def main():
    quiz_introduction()
    
  
main()