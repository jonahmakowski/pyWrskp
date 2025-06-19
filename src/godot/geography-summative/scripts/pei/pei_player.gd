extends CharacterBody2D

@export var max_of_white:int
@export var yellow_required:int
@export var death_screen:PackedScene
@export var next_scene:PackedScene

const speed = 100

var score_of_yellow = 0
var score_of_white = 0

func _physics_process(delta: float) -> void:
	var direction = Input.get_vector("move_left", "move_right", "move_up", "move_down").normalized()
	velocity = direction * speed
	
	if direction.y == 0 and direction.x == 0:
		$AnimatedSprite2D.animation = "idle"
	elif abs(direction.x) > abs(direction.y):
		$AnimatedSprite2D.animation = "walking_sideways"
		$AnimatedSprite2D.flip_h = true if direction.x > 0 else false
	elif direction.y > 0:
		$AnimatedSprite2D.animation = "walking_down"
	else:
		$AnimatedSprite2D.animation = "walking_up"
	
	if max_of_white <= score_of_white:
		Controller.new_scene = str(get_tree().current_scene.scene_file_path)
		get_tree().change_scene_to_packed(death_screen)
	
	move_and_slide()
