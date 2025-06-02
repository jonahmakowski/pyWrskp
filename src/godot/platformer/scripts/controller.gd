extends Node2D

var move_player = false;
var move_player_to = Vector2();
var coins = 0;
var collected_coins = []
var collected_keys = []
var died = false;

func change_scene(player_pos: Vector2, scene: String) -> void:
	move_player = true;
	move_player_to = player_pos;
	get_tree().change_scene_to_file(scene)

func die():
	if get_tree().current_scene.scene_file_path != 'res://scenes/main.tscn':
		change_scene(Vector2.ZERO, 'res://scenes/main.tscn')
		died = true
	else:
		get_tree().get_nodes_in_group("player")[0].position = Vector2.ZERO
		get_tree().get_nodes_in_group("player")[0].get_node("deathMessage").visible = true
		get_tree().get_nodes_in_group("player")[0].get_node("AnimatedSprite2D").play('idle')
		get_tree().get_nodes_in_group("player")[0].velocity = Vector2.ZERO

func is_coin_collected(uuid: String) -> bool:
	return uuid in collected_coins

func mark_coin_collected(uuid: String) -> void:
	if uuid not in collected_coins:
		collected_coins.append(uuid)

func is_key_collected(uuid: String) -> bool:
	return uuid in collected_keys

func mark_key_collected(uuid: String) -> void:
	if uuid not in collected_keys:
		collected_keys.append(uuid)
