from core.engine import start_game
from core.leaderboard import display_leaderboard
from colorama import Fore, Style


def main():
    print(Fore.CYAN + "\nWELCOME TO THE PASSWORD GUESSING GAME" + Style.RESET_ALL)
    print("Choose a difficulty level: easy, medium, or hard")

    level = input("Enter difficulty: ").lower()

    if level not in ["easy", "medium", "hard"]:
        print(Fore.YELLOW + "Invalid choice. Defaulting to easy level." + Style.RESET_ALL)
        level = "easy"

    start_game(level)

    while True:
        show = input("\nDo you want to see the leaderboard? (y/n): ").lower()
        if show == "y":
            display_leaderboard()
            break
        elif show == "n":
            break
        else:
            print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()


