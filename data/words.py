# data/words.py

easy_words = ["money","train","apply","mouse","god"]
medium_words = ["python", "planet", "coffee", "jungle", "bottle"]
hard_words = ["microsoft", "deloitte", "accenture", "mahindra", "elephant"]

def get_words_by_level(level):
    if level == "easy":
        return easy_words
    elif level == "medium":
        return medium_words
    elif level == "hard":
        return hard_words
    else:
        return easy_words  # fallback
 