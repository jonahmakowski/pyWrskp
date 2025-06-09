extends Node

var base_health = 20
var player_health = base_health
var current_respawn = Vector2()
var player

var passed_levels = []

var hearts = []
var hearts_collected = []

var enemies_defeated = []

func generate_uuid(node: Node2D):
	return '{0}|{1}'.format([str(node.name), str(node.get_owner())])

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	if len(get_tree().get_nodes_in_group("player")) != 0:
		player = get_tree().get_nodes_in_group("player")[0]

func reset_level(levels, lis):
	for item in lis:
		for level in levels:
			if str(level) in item:
				lis.remove_at(lis.get(item))
				break
	return lis

func kill_player():
	player.position = current_respawn
	player_health = base_health
	hearts_collected = reset_level(passed_levels, hearts_collected)
	enemies_defeated = reset_level(passed_levels, enemies_defeated)
	get_tree().reload_current_scene()

func finish_level():
	passed_levels.append(get_tree().current_scene)
