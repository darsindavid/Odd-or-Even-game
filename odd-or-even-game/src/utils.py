def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_choice(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ["odd", "even"]:
            return choice
        else:
            print("Invalid choice. Please type 'odd' or 'even'.")