import random


def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def play_game(max_range, best_score):
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    if best_score is None or attempts < best_score:
        print("🏆 New best score!")
        return attempts
    else:
        return best_score


def main():
    best_attempts = None

    while True:
        max_range = choose_difficulty()
        best_attempts = play_game(max_range, best_attempts)

        if best_attempts:
            print(f"Best Score so far: {best_attempts} attempts")

        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    main()
