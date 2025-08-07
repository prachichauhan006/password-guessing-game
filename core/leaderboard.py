def save_score(name, level, attempts, time_taken):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{level},{attempts},{time_taken:.2f}\n")


def display_leaderboard():
    print("\n--- Leaderboard ---")
    try:
        with open("leaderboard.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("No scores yet.")
                return

            # Sort by time taken (4th value in each line)
            sorted_entries = sorted(entries, key=lambda x: float(x.strip().split(",")[3]))

            # Show top 5
            for entry in sorted_entries[:5]:
                name, level, attempts, time_taken = entry.strip().split(",")
                print(f"{name} ({level}) - Attempts: {attempts}, Time: {time_taken}s")

    except FileNotFoundError:
        print("No leaderboard data found.")
