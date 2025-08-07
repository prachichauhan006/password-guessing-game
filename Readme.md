# Password Guessing Game

Welcome to the **Password Guessing Game**, a fun and interactive terminal-based Python project designed to test your guessing skills!  
This game randomly generates a secret password based on your chosen difficulty level. Your task is to guess the password with the help of hints.

---

## Features

- Choose from **Easy**, **Medium**, or **Hard** difficulty
- Get hints after every incorrect guess
- Timer to track how long you take
- Leaderboard to store top scores
- Clean and modular Python code

---

##  Project Structure

password_guessing_game/
│
├── game.py # Main file to run the game
├── data/
│ └── words.py # Word lists for all difficulty levels
├── core/
│ ├── engine.py # Game logic
│ ├── hint.py # Hint generator
│ └── leaderboard.py # Score storage and display
├── utils/
│ └── timer.py # Timer utility
└── scores.txt # Leaderboard data file


---

##  How to Run

Make sure you have Python installed 

Step 1: Clone the repository
```bash
git clone https://github.com/prachichauhan006/password-guessing-game.git
cd password-guessing-game

Step 2: Install dependencies
pip install colorama

Step 3: Run the game



