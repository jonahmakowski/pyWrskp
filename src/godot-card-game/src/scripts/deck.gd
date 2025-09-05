class_name Deck

var deck: Array
var style: int

func fill_card_deck(min_rank=2, max_rank=13, jokers=true):
	deck = []
	var suits = ['clubs', 'diamonds', 'hearts', 'spades']
	
	for suit in suits:
		for rank in range(1, max_rank+1):
			if rank >= min_rank:
				deck.append(Card.new(rank, suit, style))
	
	if jokers:
		deck.append(Card.new(0, 'joker', 0))
		deck.append(Card.new(0, 'joker', 0))

func get_random_card():
	return randi_range(0, len(deck)-1)

func give_hands(players: int):
	var hands = []
	for player in range(players):
		hands.append([])
	
	while len(deck) != 0:
		for player in range(players):
			if len(deck) == 0:
				break
			
			var card_index = get_random_card()
			hands[player].append(deck[card_index])
			deck.remove_at(card_index)
	
	return hands

func _init(s: int, min_rank=2, max_rank=13, jokers=true):
	style = s
	fill_card_deck(min_rank, max_rank, jokers)
