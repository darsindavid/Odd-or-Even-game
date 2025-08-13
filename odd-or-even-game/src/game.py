import random
from utils import validate_input

def main():
    print("Welcome to the Odd or Even Game!")
    toss_choice = toss_phase()
    batting_phase(toss_choice)

def toss_phase():
    while True:
        print("Choose Odd or Even:")
        toss_choice = input().lower()
        if toss_choice in ["odd", "even"]:
            print(f"You have chosen {toss_choice.capitalize()}. Get ready for the toss!")
            player_num = validate_input("Enter your number (0-6): ")
            bot_num = random.randint(0, 6)
            print(f"Bot chose: {bot_num}")
            total = player_num + bot_num
            print(f"Total is: {total}")
            result = "even" if total % 2 == 0 else "odd"
            print(f"The result is {result.capitalize()}.")
            if toss_choice == result:
                print("You have won the toss! Choose to bat or bowl.")
                return input("Bat or Bowl? ").lower()
            else:
                print("You have lost the toss.")
                return "bowl" if toss_choice == "odd" else "bat"

def batting_phase(toss_choice):
    if toss_choice == "bat":
        print("You chose to bat!")
        # Implement batting logic here
    else:
        print("You chose to bowl!")
        # Implement bowling logic here

if __name__ == "__main__":
    main()