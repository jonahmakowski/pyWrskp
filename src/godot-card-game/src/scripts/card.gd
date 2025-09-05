class_name Card

var sprite
var rank
var suit
var type
var president_rank

func set_president_rank():
	president_rank = rank
	# Aces
	if rank == 1:
		president_rank = 14
	
	# Twos
	if rank == 2:
		president_rank = 15
	
	# Jokers
	if rank == 0:
		president_rank = 16

func _init(r: int, s: String, t: int):
	rank = r
	suit = s
	type = t
	sprite = load("res://assets/cards/{0}/{1}_{2}.png".format([type, suit, rank]))
	set_president_rank()
