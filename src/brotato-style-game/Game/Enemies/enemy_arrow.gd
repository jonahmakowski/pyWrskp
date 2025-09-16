extends CharacterBody2D

var direction: Vector2

func find_player():
	var player = null
	for child in get_parent().get_children():
		if child.is_in_group("player"):
			player = child
	
	return player

func _ready():
	var player = find_player()
	
	if player == null:
		queue_free()
		return
	
	rotation = global_position.angle_to_point(player.global_position)
	direction = global_position.direction_to(player.global_position)
	velocity = (direction * Stats.ENEMY_PROJECTILE_SPEED) * Stats.enemy_projectile_speed_multiplyer

func _physics_process(_delta: float) -> void:
	move_and_slide()

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()
