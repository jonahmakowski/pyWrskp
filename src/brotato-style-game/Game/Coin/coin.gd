extends CharacterBody2D

var value = 1
var to_player: bool

func init(v):
	value = v
	
	if randf() < float(Stats.coin_retrieval_percentage) / 100 and Stats.coin_retrieval_percentage != 0:
		to_player = true

func find_player() -> CharacterBody2D:
	var player = null
	for child in get_parent().get_children():
		if child.is_in_group("player"):
			player = child
	
	return player

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Stats.coins += value
	queue_free()

func _physics_process(_delta: float) -> void:
	if to_player:
		var player = find_player()
		var direction = global_position.direction_to(player.global_position)
		velocity = direction * Stats.COIN_MOVEMENT_SPEED
		move_and_slide()
