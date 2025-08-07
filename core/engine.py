import random
from colorama import Fore, Style
from data.words import get_words_by_level
from utils.timer import Timer, format_time
from core.hint import generate_hint
from core.leaderboard import save_score, display_leaderboard


def start_game(level):
    words = get_words_by_level(level)
    secret_word = random.choice(words)

    print(Fore.YELLOW + f"\nA {len(secret_word)}-letter password has been set." + Style.RESET_ALL)
    print("You need to guess it correctly.")

    timer = Timer()
    timer.start()

    attempts = 0

    while True:
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1

        if guess == secret_word:
            timer.stop()
            print(Fore.GREEN + "\nAccess Granted! You cracked the password." + Style.RESET_ALL)
            print(f"Time taken: {timer.elapsed_time():.2f} seconds")
            print(f"Total attempts: {attempts}")

            name = input("Enter your name for the leaderboard: ").strip()
            save_score(name, level, attempts, timer.elapsed_time())
            break
        else:
            print(Fore.RED + "Access Denied. Incorrect password." + Style.RESET_ALL)
            hint = generate_hint(secret_word, guess)
            print(f"Hint: {hint}")

    print("\nLeaderboard:")
    display_leaderboard()
