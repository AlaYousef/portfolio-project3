import time

def game_introduction():
    print("=========================================")
    print("|                                       |")
    print("|      Welcome to the Dice Game 12      |")
    print("|                                       |")
    print("=========================================")
    time.sleep(1)
    print("\n*********** Game Instructions ***********")
    print("The game consists of three dices. Each dice can only be rolled once per round.")
    print("In each round, you should be able to choose between:")
    print("# 1 to roll the dice 1")
    print("# 2 to roll the dice 2")
    print("# 3 to roll the dice 3")
    print("# q to exit the game")
    time.sleep(4)
    print("\nThe program will randomly find a value on the selected dice and calculate the score. If the sum after rolling all dices is 12 you win the game, If the sum is more than 12 so you loss the game ")
    time.sleep(2)
    print("\nPreparing the program...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

def input_value():
    print("\n Welcom to the Dice Game 12. You should roll 1-3 dice and try to get the sum 12...")
    user_input  = input(" Enter which dice you want to roll [1,2,3] Or exit with [q]: ")
    return user_input

def main():
    game_introduction()
    v = input_value()
    print(v)

main()