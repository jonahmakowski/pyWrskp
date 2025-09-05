extends Control

@onready var card_area: Node = %"Card Area"
@onready var card_hbox: HBoxContainer = %"Card Hbox"
@onready var next_player_menu: PanelContainer = %"Next Player Menu"
@onready var card_played_area: HBoxContainer = %"Card Played Area"
@onready var timer: Timer = %NextPlayerTimer
@onready var card_count_area: HBoxContainer = %"Card Count Area"
@onready var hand_display: Label = %"Hand Display"

@export var card_scene: PackedScene
@export var inbetween_scene: PackedScene
@export var card_amount_display: PackedScene

var current_hand = 0
var hands = []
var selected_cards = []
var currently_played = []
var played = false
var hand_played_by = -1
var num_of_passes = 0
var winners = []
var burn = false

func next_player(change_by=1):
	current_hand += change_by
	if current_hand >= Globals.num_of_players:
		current_hand = 0
	
	update_winners()
	
	if current_hand in winners:
		while current_hand in winners:
			current_hand += 1
			if current_hand >= Globals.num_of_players:
				current_hand = 0

func show_hand(hand: Array):
	var children = card_hbox.get_children()
	for child in children:
		if child.is_in_group("card"):
			child.queue_free()
	
	for card in hand:
		var instance = card_scene.instantiate()
		instance.setup(card)
		card_area.add_sibling(instance)

func _ready() -> void:
	if Globals.president_hands == []:
		hands = Deck.new(Globals.style).give_hands(Globals.num_of_players)
	else:
		hands = Globals.president_hands
	
	for hand in hands:
		hand.sort_custom(Controller.president_sort_hand)
	
	Globals.president_hands = hands
	
	show_hand(hands[0])
	
	for player in range(Globals.num_of_players):
		var instance = card_amount_display.instantiate()
		instance.setup(player)
		card_count_area.add_child(instance)

func valid_hand():
	# Rules
	# Number of cards must match - Except for 2 and Jokers
	# Rank must be higher
	
	# If there are no cards, return false
	if len(selected_cards) == 0:
		print('Not allowed because zero cards selected')
		return false
	# If there are more than one card selected, and nothing is currently on the pile, allow it
	elif len(currently_played) == 0:
		print('Automatically allowed because nothing is on the pile')
		return true
	
	var ranks = []
	for card in selected_cards:
		ranks.append(card.president_rank)
	
	# If it's a joker, and there's more than one return false
	if 16 in ranks and len(ranks) > 1:
		print('Not allowed because more than one joker')
		return false
	# 2 rules
	if 15 in ranks:
		var num_of_selected_cards = len(selected_cards)
		var num_of_played_cards = len(currently_played)
		
		if num_of_played_cards == 1 and num_of_selected_cards != 1:
			return false
		elif num_of_played_cards == 2 and num_of_selected_cards != 1:
			return false
		elif num_of_played_cards == 3 and num_of_selected_cards != 2:
			return false
		elif num_of_played_cards == 4 and num_of_selected_cards != 2:
			return false 
	# If the amount of cards isn't equal, return false
	elif len(currently_played) != len(selected_cards):
		if not (selected_cards[0].rank == 2 and len(selected_cards) == len(currently_played)-1):
			if selected_cards[0].rank != 0:
				print('Not allowed because different number of cards')
				return false
	# If it's a lower rank than the previous cards, return false
	elif ranks[0] <= currently_played[0].card.president_rank:
		# Exception for the bum
		if current_hand != Globals.president_bum or ranks[0] < currently_played[0].card.president_rank:
			print('Not allowed because lower rank')
			return false
		else:
			burn = true
			print('This is a bum burn')
	
	# If it's made of different ranks
	for rank in ranks:
		if rank != ranks[0]:
			print('Not allowed because must all be same ranks')
			return false
	
	return true

func run_hand():
	burn = false
	if valid_hand():
		num_of_passes = 0
		
		hand_played_by = current_hand
		
		# Clear the viewing area from previous cards
		for child in card_played_area.get_children():
			child.queue_free()
		
		# Put card(s) in the viewing area and remove them from your hand
		for card in selected_cards:
			if selected_cards[0].rank != 0 and not burn:
				var card_instance = card_scene.instantiate()
				card_instance.setup(card, false)
				card_played_area.add_child(card_instance)
			
			var index = Controller.get_index_of_card(card, hands[current_hand])
			if card in hands[current_hand]:
				hands[current_hand].remove_at(index)
				show_hand(hands[current_hand])
		
		# If you played a joker or burned, and you aren't out of cards, make it the next player's turn
		if (selected_cards[0].rank != 0 and not burn) or len(hands[current_hand]) == 0:
			timer.start()
			next_player()
		
		selected_cards = []

func _process(_delta: float) -> void:
	Globals.president_hands = hands
	Globals.rankings = winners
	
	if Input.is_action_just_pressed("reset"):
		selected_cards = []
	
	if not played:
		for child in card_hbox.get_children():
			if child.is_in_group("card"):
				if child.selected == false and child.card in selected_cards:
					selected_cards.remove_at(Controller.get_index_of_card(child.card, selected_cards))
				elif child.selected == true and child.card not in selected_cards:
					selected_cards.append(child.card)
		
		if Input.is_action_just_pressed("play_cards"):
			run_hand()
		
		if Input.is_action_just_pressed("pass"):
			pass_hand()
		
		currently_played = card_played_area.get_children()

func change_hands():
	next_player(0)
	show_hand(hands[current_hand])
	next_player_menu.next_turn()
	selected_cards = []

func pass_hand():
	if card_played_area.get_child_count() == 0:
		return
	
	num_of_passes += 1
	var new_set = false
	if num_of_passes == Globals.num_of_players-len(winners)-1:
		current_hand = hand_played_by
		
		next_player(0)
		
		print('Had enough passes ({0}) in a row, changed to {1} was going to be {2}'.format([num_of_passes, current_hand, hand_played_by]))
		
		new_set = true
		for child in card_played_area.get_children():
			if child.is_in_group("card"):
				child.queue_free()
		num_of_passes = 0
	else:
		next_player()
	
	if card_played_area.get_child_count() != 0 or new_set:
		change_hands()
	
	hand_display.update()

func end_round():
	var player = 0
	
	for hand in hands:
		if len(hand) == 0 and player not in winners:
			winners.append(player)
			print('Player {0} is the loser'.format([player]))
		player += 1
	
	Globals.rankings = winners
	get_tree().change_scene_to_packed(inbetween_scene)

func update_winners():
	for player in range(Globals.num_of_players):
		if len(hands[player]) == 0 and player not in winners:
			winners.append(player)

func _on_timer_timeout() -> void:
	update_winners()
	if len(winners) >= Globals.num_of_players - 1:
		end_round()
	else:
		change_hands()
