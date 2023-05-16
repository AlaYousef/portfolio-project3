import time

def quiz_introduction():
    print("=========================================")
    print("|                                       |")
    print("|     Welcome to Periodic Table Quiz    |")
    print("|                                       |")
    print("=========================================")
    time.sleep(1)
    print("\n*********** Quiz Instructions ***********")
    print("The quiz consists of 15 questions, with four answer options.") 
    print("You should choose one of answer options from (1 to 4). After complete the 15 questions you will get your score")
    time.sleep(4)
    print("\nThe program will randomly find a value on the selected dice and calculate the score. If the sum after rolling all dices is 12 you win the game, If the sum is more than 12 so you loss the game ")
    time.sleep(2)
    print("\nPreparing quiz questions...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

def input_value():
    user_input  = input("Please, Enter your name:  ")
    return user_input

def main():
    quiz_introduction()
    v = input_value()
    print(v)

main()