
games = {
	"Chess": {
		"players": "2",
		"age": "6+",
		"time": "30-60 mins",
		"difficulty": 5,
		"video": "https://www.youtube.com/watch?v=OCSbzArwB10",
		"category": "Strategy Games",
		"setup": "Arrange all pieces on the board.",
		"play": "Take turns moving pieces.",
		"special": "Each piece moves differently.",
		"win": "Checkmate the opponent king."
	},

	"Uno": {
		"players": "2-10",
		"age": "7+",
		"time": "15-30 mins",
		"difficulty": 2,
		"video": "https://www.youtube.com/watch?v=OyD2mdd7iZ4",
		"category": "Card Games",
		"setup": "Deal 7 cards to each player.",
		"play": "Match color or number.",
		"special": "Use action cards.",
		"win": "Get rid of all cards."
	},

	"Monopoly": {
		"players": "2-6",
		"age": "8+",
		"time": "60-180 mins",
		"difficulty": 3,
		"video": "https://www.youtube.com/watch?v=GQ1KTa-EgHs",
		"category": "Family Games",
		"setup": "Place board and money.",
		"play": "Roll dice and buy property.",
		"special": "Collect rent.",
		"win": "Become richest player."
	}
}

def get_game(name):
	"""Return game data by name (case-insensitive) or None if not found."""
	return games.get(name) or games.get(name.title()) or games.get(name.capitalize())
games = {
    "Chess": {
        "players": "2",
        "age": "6+",
        "time": "30-60 mins",
        "difficulty": 5,
        "video": "https://www.youtube.com/watch?v=OCSbzArwB10",

        "setup": "Arrange all pieces in their starting positions.",

        "play": "Players take turns moving pieces. Each piece has its own movement rules.",

        "special": "The king is the most important piece. Protect it at all costs.",

        "win": "Checkmate your opponent's king."
    },

    "Uno": {
        "players": "2-10",
        "age": "7+",
        "time": "15-30 mins",
        "difficulty": 2,
        "video": "https://www.youtube.com/watch?v=OyD2mdd7iZ4",

        "setup": "Each player gets 7 cards.",

        "play": "Match cards by color or number.",

        "special": "Use action cards like Skip and Draw Two.",

        "win": "Be the first player to get rid of all cards."
    },

    "Monopoly": {
        "players": "2-6",
        "age": "8+",
        "time": "60-180 mins",
        "difficulty": 3,
        "video": "https://www.youtube.com/watch?v=GQ1KTa-EgHs",

        "setup": "Place the board and give money to each player.",

        "play": "Roll dice and move around the board buying properties.",

        "special": "Collect rent from other players.",

        "win": "Become the richest player and bankrupt everyone else."
    }
}