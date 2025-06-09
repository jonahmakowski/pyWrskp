extends CharacterBody2D

const SPEED = 200.0
const JUMP_VELOCITY = -400.0
const RUN_MULT = 2

var blocking = false

func _ready() -> void:
	Controller.current_respawn = position

func get_enemies():
	var objects_collide = []
	while $EnemyRayCast.is_colliding():
		var obj = $EnemyRayCast.get_collider(0)
		objects_collide.append(obj)
		$EnemyRayCast.add_exception(obj)
		$EnemyRayCast.force_shapecast_update()

	for obj in objects_collide:
		$EnemyRayCast.remove_exception(obj)
	return objects_collide

func _process(_delta: float) -> void:
	if (Input.is_action_just_pressed("attack1") or 
		Input.is_action_just_pressed("attack2") or 
		Input.is_action_just_pressed("attack3")):
		
		$PlayerAudio.stream = load("res://assets/audio/sword-swing.mp3")
		$PlayerAudio.play()
		
		if $EnemyRayCast.is_colliding():
			var collidors = get_enemies()
			for collider in collidors:
				collider.attacked()
	if Input.is_action_just_pressed('block'): 
		blocking = true
	$Health.text = "Health: " + str(Controller.player_health)

func is_attacking():
	return "attack" in $Sprite.animation or $Sprite.animation == 'defend'

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity += get_gravity() * delta

	if Input.is_action_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	var direction := Input.get_axis("move_left", "move_right")
	if direction:
		velocity.x = direction * SPEED if not Input.is_action_pressed('run') else direction * SPEED * RUN_MULT
		if not is_attacking(): $Sprite.animation = "walk" if not Input.is_action_pressed('run') else "run"
		$Sprite.flip_h = true if direction == -1 else false
		$EnemyRayCast.target_position.x = 30 * direction
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		if not is_attacking(): $Sprite.animation = "idle"
	
	if not (is_on_floor() or is_attacking()): $Sprite.animation = "jump"
	if not is_attacking():
		if Input.is_action_just_pressed("attack1"): $Sprite.animation = "attack1"
		elif Input.is_action_just_pressed("attack2"): $Sprite.animation = "attack2"
		elif Input.is_action_just_pressed("attack3"): $Sprite.animation = "attack3"
	
	if not is_attacking() and Input.is_action_just_pressed("block"): $Sprite.animation = 'defend'
	
	move_and_slide()

func _on_sprite_animation_looped() -> void:
	if "attack" in $Sprite.animation:
		$Sprite.animation = "idle"
	if $Sprite.animation == "defend":
		blocking = false
		$Sprite.animation = "idle"

func attacked():
	if not blocking:
		$PlayerAudio.stream = load("res://assets/audio/hurt.mp3")
		$PlayerAudio.play()
		Controller.player_health -= 1
		if Controller.player_health == 0:
			Controller.kill_player()
