extends CharacterBody2D

const SPEED = 125
const MAX_DISTANCE = 90

func is_player():
	return true

func _physics_process(_delta: float) -> void:
	var vertical_input := Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
	velocity.y = vertical_input * SPEED
	move_and_slide()
	
	position.y = clamp(position.y, -MAX_DISTANCE, MAX_DISTANCE)

func _process(_delta: float) -> void:
	if Input.is_action_pressed("sprint"):
		$AnimatedSprite2D.speed_scale = 2
	else:
		$AnimatedSprite2D.speed_scale = 1

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Controller.new_scene = "res://scenes/places/montreal.tscn"
	get_tree().call_deferred("change_scene_to_file", "res://scenes/failure_screen.tscn")
