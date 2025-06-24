extends CharacterBody2D

var speed = 0
const max_speed = 300
const flags_required = 20
var direction = Vector2()
var flags = 0

@export var next_scene:PackedScene

func is_player():
	return true

func _physics_process(_delta: float) -> void:
	if ((Input.is_action_pressed('move_left') or Input.is_action_pressed('move_right'))
		or (Input.is_action_just_pressed("move_up") or Input.is_action_just_pressed("move_down"))):
		
		direction = Input.get_vector("move_left", "move_right", "move_up", "move_down").normalized()
	
	$FlagDisplay.set_text("{0}/{1} Flags".format([flags, flags_required]))
	
	if direction.y > 0:
		speed += direction.y
	else:
		speed += direction.y * 6
	speed = clamp(speed, 0, max_speed)
	
	velocity = direction * speed
	$Sprite.rotation = direction.angle()
	
	move_and_slide()

func _process(_delta: float) -> void:
	if Input.is_action_pressed("sprint"):
		$Sprite.speed_scale = 2
	else:
		$Sprite.speed_scale = 1
	
	if flags == flags_required:
		get_tree().change_scene_to_packed(next_scene)
		return

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Controller.new_scene = "res://scenes/places/montreal.tscn"
	get_tree().call_deferred("change_scene_to_file", "res://scenes/failure_screen.tscn")
