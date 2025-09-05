extends Node

const OPTIONS_FILE_PATH = "user://options.json"

func _ready() -> void:
	var options = load_options()
	Globals.current_options = options
	Globals.style = options['style']

func load_options() -> Dictionary:
	var options = {}

	if FileAccess.file_exists(OPTIONS_FILE_PATH):
		var file_access = FileAccess.open(OPTIONS_FILE_PATH, FileAccess.READ)

		var content = file_access.get_as_text()
		file_access.close()

		var parse_result = JSON.parse_string(content)
		if parse_result is Dictionary:
			options = parse_result
		else:
			push_error("Loaded options file content is not a dictionary. Using default options.")
			options = Globals.default_options
	else:
		options = Globals.default_options
		save_options(Globals.default_options) 
	for key in Globals.default_options:
		if not options.has(key):
			options[key] = Globals.default_options[key]
			
	return options

func save_options(options_to_save: Dictionary) -> void:
	var file_access = FileAccess.open(OPTIONS_FILE_PATH, FileAccess.WRITE)

	var json_string = JSON.stringify(options_to_save, "\t") # "\t" for tabs, 4 for 4 spaces

	file_access.store_string(json_string)
	file_access.close()

func president_mode():
	var deck = Deck.new(0)
	var hands = deck.give_hands(Globals.num_of_players)

func president_sort_hand(a, b):
	var rank_a = a.president_rank
	var rank_b = b.president_rank
	
	if rank_a < rank_b:
		return true
	else:
		return false

func get_index_of_card(item, list):
	var index = 0
	for object in list:
		if object.rank == item.rank and object.suit == item.suit:
			return index
		index += 1
	return -1

func get_index_of_generic(item, list):
	var index = 0
	for object in list:
		if object == item:
			return index
		index += 1
	return -1
