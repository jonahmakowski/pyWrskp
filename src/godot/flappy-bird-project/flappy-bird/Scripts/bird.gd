extends CharacterBody2D

const JUMP_VELOCITY = -200.0


func _physics_process(delta: float) -> void:
	velocity += get_gravity() * delta / 2
	
	if Input.is_action_just_pressed("jump"):
		velocity.y = JUMP_VELOCITY
	
	velocity.x = 0
	
	move_and_slide()
	
	position.y = clamp(position.y, -(get_window().size.y / 2) / 3, (get_window().size.y / 2) / 3)

func _process(_delta: float) -> void:
	pass
