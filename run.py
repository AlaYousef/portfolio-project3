import time
import random
import textwrap
import sys
import os

# questions list of dectionaries (question,answers,correct_answer)
questions = [
    {
        "question":"1. Which element got its name from the water it makes when burned?",
        "answers":
        ["1.iodine", "2.hydrogen", "3.tungsten","4.sodium"],
        "correct_answer": "2.hydrogen",
        "details": ("Hydrogen was first called “inflammable air” "
        " before chemist Antoine Lavoisier renamed it “water-former” (hydro + gen).")
    },
    {
        "question": "2. Uranium was named after which of the following?",
        "answers":
        ["1.a dog", "2.a planet", "3.a scientist", "4.a country"],
        "correct_answer": "2.a planet",
        "details": ("Uranium was discovered in 1789, shortly after the planet Uranus was discovered." 
        " Neptunium and plutonium are also named for celestial bodies in our solar system.")

    },
    {
        "question": "3. Which of these metals is liquid at room temperature?",
        "answers":
        ["1.mercury", "2.nickel", "3.titanium", "4.zinc"],
        "correct_answer": "1.mercury",
        "details": ("Mercury, often called “quicksilver,” remains a liquid until cooled to about −40 °F."
        " Bromine is the only other element that is liquid at room temperature.")
    },
    {
        "question":
        ("4. Which element is most abundant in both Earth’s crust and the human body?"
         " into energy?"),
        "answers":
        ["1.iron", "2.hydrogen", "3.silicon", "4.oxygen"],
        "correct_answer": "4.oxygen",
        "details": "Oxygen constitutes nearly half of Earth’s crust and two-thirds of a human body’s mass."

    },
    {
        "question": "5. Diamonds are made of which element?",
        "answers":
        ["1.sulfur", "2.nitrogen", "3.lithium","4.carbon"],
        "correct_answer": "4.carbon",
        "details": ("Contrary to popular belief, diamonds are not made from coal, although both contain carbon.")

    },
    {
        "question": "6. What is the most common element found in all living organisms?",
        "answers":
        ["1.Oxygen", "2.Carbon", "3.Nitrogen", "4.Hydrogen"],
        "correct_answer": "2.Carbon",
        "details": "Contrary to popular belief, diamonds are not made from coal, although both contain carbon."

    },
    {
        "question":"7. Which element found in red blood cells helps carry oxygen?",
        "answers":
        ["1.iron", "2.boron", "3.calcium","4.lead"],
        "correct_answer": "1.iron",
        "details": ("The iron in hemoglobin forms a reversible bond with oxygen;"
        " they latch together in the lungs and then split at the oxygen’s destination.")

    },
    {
        "question": "8. Which of these famous poisons appears in the periodic table?",
        "answers":
        ["1.cyanide", "2.strychnine", "3.ricin", "4.arsenic"],
        "correct_answer": "4.arsenic",
        "details": "Arsenic has been dubbed the “king of poisons” thanks to its odorless and tasteless qualities."

    },
    {
        "question":"9. Elements, such as helium and neon, that tend to not undergo chemical reactions are called what?",
        "answers":
        ["1.conservative gases", "2.lazy gases", "3.content gases", "4.noble gases"],
        "correct_answer": "4.noble gases",
        "details": ("Just as a nobleman might avoid commoners,"
        " so too do noble gases resist interacting with other elements.")

    },
    {
        "question": "10. Which element’s name and symbol (Cu) comes from the Latin name for Cyprus, where ancient Romans mined it?",
        "answers":
        ["1.copper", "2.chromium", "3.calcium", "4.carbon"],
        "correct_answer": "4.copper",
        "details": ("The Romans called the element aes Cyprium (“metal of Cyprus”),"
        " which was shortened to cyprium and then corrupted to cuprum, eventually becoming copper.")

    },
    {
        "question": "11. Which element was discovered on the Sun before it was found on Earth?",
        "answers":
        ["1.helium", "2.potassium", "3.neon", "4.iodine"],
        "correct_answer": "1.helium",
        "details": ("Using a spectroscope in 1868, scientists first detected helium on the Sun (from helios, the Greek word for “sun”) during an eclipse."
        " Fourteen years later, helium was found on Earth.")

    },
    {
        "question": "12. Ancient Romans used which element to make plumbing?",
        "answers":
        ["1.gold", "2.titanium", "3.lead", "4.aluminum"],
        "correct_answer": "3.lead",
        "details": ("Because it is highly durable and resistant to corrosion, lead (chemical symbol Pb from the Latin plumbum) "
        "was used by the Romans to make water pipes as well as coins and cooking utensils."
        " By the time of Augustus Caesar, lead poisoning had become an issue in Rome.")

    },
    {
        "question": "13. Which of these letters does not appear in the periodic table, either as a symbol or in an element name?",
        "answers":
        ["1. k", "2. x", "3. z", "4. j"],
        "correct_answer": "4. j",
        "details": ("The letter x can be found in xenon, z in zinc, and k in krypton (among other places)."
        " The letter q appears only in the extended periodic table in the name unbiquadium, "
        "a placeholder term for the as yet undiscovered element that will have the atomic number 124.")

    },
    {
        "question":
        ("14. Frequently used in flares, which element burns so intensely that it can "
        "cause temporary blindness and cannot be extinguished with water?"),
        "answers":
        ["1.magnesium", "2.neon", "3.iodine", "4.silicon"],
        "correct_answer": "1.magnesium",
        "details": ("Magnesium has been used in flash photography, pyrotechnics, and incendiary bombs."
        "When introduced to a magnesium fire, water is converted to a hydrogen gas, further fueling the flame.")

    },
     {
        "question":
        ("15. Used by the Indigenous people of South America for metalcraft,"
        " which element comes from the Spanish word for “silver”?"),
        "answers":
        ["1.tin", "2.cobalt", "3.nickel", "4.platinum"],
        "correct_answer": "4.platinum",
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

def check_answer_input(*answers_list):
    print(answers_list)
   
    while True:
        try:
            answer_input  = input("Enter answer number:  ")
            answer_number = int(answer_input)
            if answer_number < 1 or answer_number > 4:
                raise ValueError(
                    f"answer option should be from 1 to 4"
                )
            else:
                return str(answer_number)
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            
        


def run_quiz():
    score = 0
    answer_list = []
    for index in (questions):
        print(index['question'])
        for answers in index['answers']:
            print(answers)
            
        answer = check_answer_input()
        
        print(index['correct_answer'])
        
        for value in index['answers']:
            print(index['correct_answer'])
            print(value.__contains__(index['correct_answer']))
            
            if answer == index['correct_answer'][:1]:
                print(f"Good! Your answer is correct :) ...\n {index['details']}")
                score += 1
                break
            else:
                print("Your answer is incorrect :( ")
                break

        
                
            
        
            
       



def main():
    #quiz_introduction()
    run_quiz()
    
  
main()