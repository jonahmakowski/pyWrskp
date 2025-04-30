extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -400.0


func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump.
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY
	
	if not is_on_floor():
		$AnimatedSprite2D.play('jump')

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("move_left", "move_right")
	if direction:
		velocity.x = direction * SPEED
		$AnimatedSprite2D.set_flip_h(true if direction == -1 else false)
		if is_on_floor(): $AnimatedSprite2D.play('run')
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		if is_on_floor(): 
			$AnimatedSprite2D.play('idle')

	move_and_slide()
