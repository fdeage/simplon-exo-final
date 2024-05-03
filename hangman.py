import random

def choose_word():
    words = ["pendu", "code"]
    return random.choice(words)

def get_user_letter():
    return input("Entrez une lettre : ").lower()

def check_letter_in_word(letter, word):
    return letter in word

def update_completed_word(completed_word, letter, word):
    index = word.index(letter)
    return completed_word[:index] + letter + completed_word[index + 1:]

def game_over_fct(try_nb, completed_word, word):
    """Gère le nombre de tentatives et détermine si le jeu est terminé."""
    if try_nb == 8 or "_" not in completed_word:
        return True
    return False

def display_results(game_over, try_nb, word):
    """Affiche les résultats du jeu."""
    if game_over:
        if try_nb == 8:
            print("Vous avez épuisé toutes vos tentatives.")
        else:
            print("Vous avez deviné le mot : ", word)
    else:
        print("Le jeu continue...")

def hangman():
    word = choose_word()
    completed_word = "_" * len(word)
    try_nb = 0

    while try_nb < 8 and "_" in completed_word:
        print("Mot à deviner :", completed_word)
        letter = get_user_letter()

        if check_letter_in_word(letter, word):
            completed_word = update_completed_word(completed_word, letter, word)
            print("Lettre trouvée!")
        else:
            try_nb += 1
            print(f"Tentative {try_nb} échouée.")

        if game_over_fct(try_nb, completed_word, word):
            game_over = True
            break

    display_results(game_over, try_nb, word)

if __name__ == "__main__":
    hangman()
