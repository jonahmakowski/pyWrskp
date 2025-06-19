extends Node

var base_health = 20
var player_health = base_health
var current_respawn = Vector2()
var send_to_respawn = false
var player
var pause_visible = false

var passed_levels = []

var hearts = []
var hearts_collected = []

var coins = []
var coins_collected = []

var enemies_defeated = []

func generate_uuid(node: Node2D):
	return '{0}|{1}|{2}|{3}'.format([str(node.position.x), str(node.position.y), str(node.get_owner().name), node.name])

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	if len(get_tree().get_nodes_in_group("player")) != 0:
		player = get_tree().get_nodes_in_group("player")[0]

func reset_level(levels, lis):
	var index = 0
	for item in lis:
		var stay = false
		for level in levels:
			if str(level) in item:
				stay = true
				break
		if not stay:
			lis.remove_at(index)
		index += 1
	return lis

func kill_player():
	player.position = current_respawn
	player_health = base_health
	hearts_collected = reset_level(passed_levels, hearts_collected)
	enemies_defeated = reset_level(passed_levels, enemies_defeated)
	coins_collected = reset_level(passed_levels, coins_collected)
	get_tree().reload_current_scene()

func finish_level():
	passed_levels.append(get_tree().current_scene.name)

func play_audio(node: AudioStreamPlayer2D, audio_file, volume=0):
	node.stream = load(audio_file)
	node.volume_db = volume
	node.play()
