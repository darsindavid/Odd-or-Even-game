import random

def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid input. Please choose from {', '.join(choices)}.")

def get_valid_number(prompt):
    while True:
        num = input(prompt).strip()
        if num.isdigit() and 1 <= int(num) <= 6:
            return int(num)
        print("Invalid input. Please enter a number between 1 and 6.")

def toss_phase():
    print("\n--- Toss Phase ---")
    user_choice = get_valid_choice("Choose 'odd' or 'even': ", ['odd', 'even'])
    user_num = get_valid_number("Pick a number between 1 and 6 for the toss: ")
    comp_num = random.randint(1, 6)
    print(f"Computer picked: {comp_num}")
    total = user_num + comp_num
    print(f"Sum is {total} ({'odd' if total % 2 else 'even'})")
    if (total % 2 == 0 and user_choice == 'even') or (total % 2 == 1 and user_choice == 'odd'):
        print("You win the toss!")
        toss_winner = "user"
    else:
        print("Computer wins the toss!")
        toss_winner = "computer"
    return toss_winner

def batting_phase(batter, target=None):
    print(f"\n--- {batter.capitalize()} Batting ---")
    score = 0
    while True:
        if batter == "user":
            bat = get_valid_number("Your shot (1-6): ")
            bowl = random.randint(1, 6)
            print(f"Computer bowls: {bowl}")
        else:
            bat = random.randint(1, 6)
            print(f"Computer bats: {bat}")
            bowl = get_valid_number("Your bowl (1-6): ")
        if bat == bowl:
            print("OUT!")
            break
        else:
            score += bat
            print(f"Runs scored: {bat} | Total: {score}")
            if target is not None and score > target:
                print(f"{batter.capitalize()} has surpassed the target!")
                break
    return score

def main():
    print("Welcome to Odd or Even - Hand Cricket Game!\n")
    while True:
        toss_winner = toss_phase()
        if toss_winner == "user":
            action = get_valid_choice("Do you want to bat or bowl first? ", ['bat', 'bowl'])
        else:
            action = random.choice(['bat', 'bowl'])
            print(f"Computer chooses to {action} first.")

        if (toss_winner == "user" and action == "bat") or (toss_winner == "computer" and action == "bowl"):
            user_score = batting_phase("user")
            print(f"\nYour innings ends with {user_score} runs.")
            comp_score = batting_phase("computer", target=user_score)
            print(f"\nComputer's innings ends with {comp_score} runs.")
        else:
            comp_score = batting_phase("computer")
            print(f"\nComputer's innings ends with {comp_score} runs.")
            user_score = batting_phase("user", target=comp_score)
            print(f"\nYour innings ends with {user_score} runs.")

        print("\n--- Match Result ---")
        print(f"Your score: {user_score}")
        print(f"Computer score: {comp_score}")
        if user_score > comp_score:
            print("You win!")
        elif comp_score > user_score:
            print("Computer wins!")
        else:
            print("It's a tie!")

        play_again = get_valid_choice("\nPlay again? (yes/no): ", ['yes', 'no'])
        if play_again == 'no':
            print("Thanks for playing Odd or Even!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()