extends CharacterBody2D

const SPEED = 125.0
const JUMP_VELOCITY = -300.0
const SPRINT_SPEED = 200

func _ready() -> void:
	if Controller.move_player:
		position = Controller.move_player_to
		Controller.move_player = false
	if Controller.died:
		$deathMessage.visible = true
		$AnimatedSprite2D.play('idle')
		velocity = Vector2.ZERO
		Controller.died = false

func _process(delta: float) -> void:
	if $PlatformRayCast.is_colliding() and Input.is_action_just_pressed("move_down"):
		position.y += 3
	if Input.is_action_pressed('interact'):
		$deathMessage.visible = false

func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	if not $deathMessage.visible:
		# Handle jump.
		if Input.is_action_just_pressed("jump") and is_on_floor(): velocity.y = JUMP_VELOCITY
		if not is_on_floor(): 
			if velocity.y < 0: $AnimatedSprite2D.play('jump')
			else: $AnimatedSprite2D.play('fall')
		
		# Get the input direction and handle the movement/deceleration.
		# As good practice, you should replace UI actions with custom gameplay actions.
		var direction := Input.get_axis("move_left", "move_right")
		if direction:
			velocity.x = direction * SPRINT_SPEED if Input.is_action_pressed("sprint") else direction * SPEED
			$AnimatedSprite2D.set_flip_h(true if direction == -1 else false)
			if is_on_floor(): $AnimatedSprite2D.play('run')
		else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
			if is_on_floor(): $AnimatedSprite2D.play('idle')

	move_and_slide()

func _on_spike_collider_entered(body: Node2D) -> void:
	Controller.die()
