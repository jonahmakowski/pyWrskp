extends Control

var num_ranks
var goods = []
var bads = []
var current_player = 0
var current_good_num = 0
var hands = []
var selected_cards = []

@onready var rankings = Globals.rankings.duplicate(true)
@onready var round_over: PanelContainer = %RoundOver
@onready var card_hbox: HBoxContainer = %"Card Hbox"
@onready var card_area: Node = %"Card Area"
@onready var information_display: Label = %"Information Display"
@onready var give_button: Button = %"Give Button"
@onready var round_over_label: Label = %"Round Over Label"
@onready var player_turn_label_on_round_change: Label = %"Player Turn Label on Round Change"

@onready var score_scene: PackedScene = Globals.president_score_scene
@onready var card_scene: PackedScene = Globals.president_card_scene

func show_hand(hand: Array):
	for h in hands:
		h.sort_custom(Controller.president_sort_hand)
	
	var children = card_hbox.get_children()
	for child in children:
		if child.is_in_group("card"):
			child.queue_free()
	
	for card in hand:
		var instance = card_scene.instantiate()
		instance.setup(card)
		card_area.add_sibling(instance)

func find_highest_cards(hand, amount):
	var returns = [] # List to return at the end
	
	for unimportant in range(amount): returns.append(0) # Fill it with empty cards
	
	for card in hand: # Check if the card is the biggest in order
		var index = 0
		for c in returns: # For each card already in the returns
			if c is int or c.president_rank < card.president_rank: 
				# If it's zero (so unset), or the rank in the returns is lower
				returns[index] = card # Set that to the current card from the hand
				break # Break out of the loop
			index += 1
	
	return returns

func _ready() -> void:
	hands = Deck.new(Globals.style).give_hands(Globals.num_of_players)
	
	for hand in hands:
		hand.sort_custom(Controller.president_sort_hand)
	
	# Add New Scores
	if Globals.president_scores == []: # If it's the first round
		for unimportant in range(Globals.num_of_players): Globals.president_scores.append([]) # Fill it with empty lists
	
	# Set the current score to give to the number of players
	var score_to_give = Globals.num_of_players - 1
	
	for player in Globals.rankings: # For each player in the rankings
		Globals.president_scores[player].append(score_to_give) # Give them their score
		score_to_give -= 1 # Decrease the score by one for the next player
		print('Added a {0} to player {1} rankings'.format([score_to_give+1, player]))
	
	if Globals.num_of_players == 3:
		num_ranks = 1
	elif Globals.num_of_players == 4 or Globals.num_of_players == 5:
		num_ranks = 2
	else:
		num_ranks = 3
	
	for index in range(num_ranks):
		goods.append(rankings[index])
	
	for index in range(num_ranks):
		bads.append(rankings[-index-1])
	
	var index = 0
	for bad in bads:
		var best_cards = find_highest_cards(hands[bad], num_ranks-index) # Find the best cards from their hand
		proccess_give(best_cards, goods[index], bad)
		index += 1
		
	current_player = goods[0]
	
	show_hand(hands[current_player])
	
	player_turn_label_on_round_change.text = "Player {0}".format([current_player+1])
	information_display.text = "Player #{0} Select {1} Cards to give away.".format([current_player+1, num_ranks])
	
	Globals.president_bum = bads[0]

func proccess_give(to_give, player_to_give_to, player_to_take_away_from):
	hands[player_to_give_to].append_array(to_give) # Give the cards to the equal good
	
	var hand_index = 0
	for card in hands[player_to_take_away_from]: # For every hand in the player's hand
		for c in to_give:
			if c.rank == card.rank and c.suit == card.suit: # If they're on of the ones given away
				hands[player_to_take_away_from].remove_at(hand_index) # remove them from their hand
		hand_index += 1

func full_process():
	# If their trying to give away too much or too little
	var have_to_give = num_ranks - current_good_num
	
	if len(selected_cards) != have_to_give:
		return # Don't let them give it away
	
	proccess_give(selected_cards, bads[current_good_num], current_player)
	
	current_good_num += 1
	if current_good_num >= num_ranks:
		Globals.president_hands = hands
		get_tree().change_scene_to_packed(score_scene)
	else:
		current_player = goods[current_good_num]
		information_display.text = "Player #{0} Select {1} Cards to give away.".format([current_player+1, num_ranks-current_good_num])
		player_turn_label_on_round_change.text = "Player #{0}".format([current_player+1])
		round_over_label.text = "Next Player!"
		round_over.active = true
		round_over.visible = true
		show_hand(hands[current_player])
		selected_cards = []

func _process(_delta: float) -> void:
	for child in card_hbox.get_children():
		if child.is_in_group("card"):
			if child.selected == false and child.card in selected_cards:
				selected_cards.remove_at(Controller.get_index_of_card(child.card, selected_cards))
			elif child.selected == true and child.card not in selected_cards:
				selected_cards.append(child.card)
	
	if Input.is_action_just_pressed("play_cards"):
		full_process()

func _on_give_button_pressed() -> void:
	full_process()
