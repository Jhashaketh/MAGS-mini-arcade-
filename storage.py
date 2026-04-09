import json
import os
from player import Player

FILE = "players.json"


def load_players():
    players = {}

    if not os.path.exists(FILE):
        return players

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

            for username, pdata in data.items():
                players[username] = Player.from_dict(username, pdata)

    except Exception:
        print("Error loading file!")

    return players


def save_players(players):
    data = {name: p.to_dict() for name, p in players.items()}

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)