import random  # Import the random module to generate a random number


def number_guessing_game():
    while True:
        print("\nWelcome to the Number Guessing Game!")

        # Let the user set their own range
        while True:
            try:
                lower_bound = int(input("Enter the lower bound: "))
                upper_bound = int(input("Enter the upper bound: "))
                if lower_bound < upper_bound:
                    break
                else:
                    print("Invalid range! Lower bound must be less than upper bound.")
            except ValueError:
                print("Please enter valid numbers.")

        # Generate a random number within the chosen range
        secret_number = random.randint(lower_bound, upper_bound)

        # Set a limited number of attempts
        max_attempts = int((upper_bound - lower_bound) * 0.2)  # 20% of range size
        attempts = 0
        previous_difference = None

        print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
        print(f"You have {max_attempts} attempts to guess correctly.")

        while attempts < max_attempts:
            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            attempts += 1
            remaining_attempts = max_attempts - attempts
            difference = abs(secret_number - guess)

            if guess < secret_number:
                hint = "Too low!"
            elif guess > secret_number:
                hint = "Too high!"
            else:
                print(f"🎉 Congratulations! You've guessed the number in {attempts} attempts!")
                break  # Exit the loop when guessed correctly

            # Provide more detailed hints
            if previous_difference is not None:
                if difference < previous_difference:
                    hint += " You're getting closer!"
                elif difference > previous_difference:
                    hint += " You're moving farther away."

            previous_difference = difference  # Update previous difference
            print(hint)

            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left.")
            else:
                print(f"Game Over! The correct number was {secret_number}.")
                break

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye. 👋")
            break


# Start the game
number_guessing_game()
