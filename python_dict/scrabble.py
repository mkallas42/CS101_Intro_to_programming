"""
Scrabble.

In this project, you will process some data from a group of friends playing scrabble.

You will use dictionaries to organize players, words, and points.
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# ----------------------------------------------------------
# Build your Point Dictionary

letter_to_points = {key: value for key, value in zip(letters, points)}

letter_to_points[" "] = 0


# -------------------------------------------------------------
# Score a Word

def score_word(word):
    point_total = 0

    for letter in word:
        if letter in letter_to_points:
            point_total += letter_to_points[letter]
        point_total += 0
    return point_total


brownie_points = score_word("BROWNIE")

# --------------------------------------------------------------
# Score a Game

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points


# print(player_to_points)

# ---------------------------------------------------------------
# Ideas for Further Practice!

def play_word(player, word):
    player_to_words[player].append(word)


play_word("wordNerd", "FOMO")
print(player_to_words)

player_to_points = {}


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


update_point_totals()
print(player_to_points)

letters += [letter.lower() for letter in letters]