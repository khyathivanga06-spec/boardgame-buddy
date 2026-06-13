
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
