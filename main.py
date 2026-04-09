from games import guessing_game, hangman, rock_paper_scissors
from storage import load_players, save_players
from player import Player


def get_player(players, username):
    if username not in players:
        players[username] = Player(username)
        print("New player created!")
    return players[username]


def main():
    players = load_players()

    username = input("Enter username: ").strip()
    player = get_player(players, username)

    while True:
        print("\n=== MINI ARCADE ===")
        print("1. Guessing Game")
        print("2. Hangman")
        print("3. Rock Paper Scissors")  # NEW
        print("4. View Stats")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            guessing_game(player)
        elif choice == "2":
            hangman(player)
        elif choice == "3":
            rock_paper_scissors(player)  # NEW
        elif choice == "4":
            print(player.get_stats())
        elif choice == "5":
            save_players(players)
            print("Data saved successfully!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
