extends Control

@onready var next_scene: PackedScene = Globals.president_scene

@onready var scores = Globals.president_scores.duplicate(true)
@onready var num_of_players = Globals.num_of_players

@onready var grid: GridContainer = %Grid

@export var helper: PackedScene

const test_mode = false # Sets the score

func _ready():
	if test_mode:
		scores = [[3, 2], [2, 3], [1, 1]]
	
	for index in range(num_of_players):
		if len(scores[index]) == 0:
			Globals.president_scores[index].append(0)
			scores = Globals.president_scores.duplicate(true)
	
	var totals = []
	
	# Add up all the totals
	for score_set in scores:
		var to_add = 0
		for score in score_set:
			to_add += score
		totals.append(to_add)
	
	for index in range(num_of_players):
		scores[index].push_front("Player #{0}".format([index+1]))
		scores[index].append("Total: {0}".format([totals[index]]))
	
	for score_index in range(len(scores[0])):
		for player in range(num_of_players):
			var instance = helper.instantiate()
			instance.text = str(scores[player][score_index])
			grid.add_child(instance)
	
	print(scores)
	
	grid.columns = Globals.num_of_players

func _on_continue_pressed() -> void:
	Globals.rankings = []
	get_tree().change_scene_to_packed(next_scene)
