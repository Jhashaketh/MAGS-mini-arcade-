import random
from utils import get_int


def guessing_game(player):
    number = random.randint(1, 20)
    attempts = 3

    print("\nGuess the number (1–20)")

    while attempts > 0:
        guess = get_int("Enter guess: ")

        if guess == number:
            print(" Correct!")
            player.record_win()
            return
        elif guess < number:
            print("Too Low!")
        else:
            print("Too High!")

        attempts -= 1
        print("Attempts left:", attempts)

    print(" You lost! Number was", number)
    player.record_loss()


def hangman(player):
    words = ["python", "game", "arcade"]
    word = random.choice(words)

    display = ["_"] * len(word)
    attempts = 5

    print("\nHangman Game")

    while attempts > 0 and "_" in display:
        print("Word:", " ".join(display))
        guess = input("Enter letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    if "_" not in display:
        print(" You guessed:", word)
        player.record_win()
    else:
        print(" Game Over! Word was:", word)
        player.record_loss()