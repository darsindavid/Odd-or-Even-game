import random
def oddoreven():
    global toss_choice
    while True:
        print("Odd or Even?")
        toss_choice= input().lower() #convrts all answers to lowercase
        if toss_choice == "even":
            print("You have chosen Even. Get ready for the toss!")
            break #loop is closed if condition is valid (even)
        elif toss_choice == "odd":
            print("You have chosen Odd. Get ready for the toss!")
            break
        else:
            print("Type either odd or even only.")
oddoreven()

def toss():
    player_num= int(input("Enter your number (0-6): "))
    bot_num=random.randint(0,6)
    print(f"Bot chose: {bot_num}")
    total=player_num+bot_num
    print(f"Total is: {total} ")
    if total%2 == 0:
        result="even"
        print ("The result is even")
    else:
        result="odd"
        print("The result is odd")
    if toss_choice==result:
        print("You have won the toss! Choose to bat or bowl")
        batorbowl=input("Bat or Bowl?")
    else:
        print("You have lost the toss.")
toss()
player_choice = oddoreven()
toss(player_choice)