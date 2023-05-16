import time
import random
import textwrap
import sys
import os

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
    "After complete the 15 questions you will get your score")
    time.sleep(6)

    print("Press Enter to start the quiz..\n")
    input()

    
    print("\nPreparing quiz questions...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...\n")
    time.sleep(2)

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
    clear_screen()
    user_input  = input("First, please enter your name:  ")
    return user_input

def main():
    quiz_introduction()
    v = input_value()
    print(v)

main()