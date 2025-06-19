extends CharacterBody2D

@export var health_base = 10
@export var gives_coin = false
var health = 0
const SPEED = 100
var player_direction = 0
@onready var player = get_tree().get_nodes_in_group("player")[0]
@onready var respawn = position
@onready var uuid = Controller.generate_uuid($".")

func _ready():
	health = health_base
	if gives_coin and uuid not in Controller.coins: Controller.coins.append(uuid)
	if gives_coin: $Coin.visible = true
	if uuid in Controller.enemies_defeated:
		queue_free()

func reset():
	position = respawn
	health = health_base
	velocity = Vector2()
	$Sprite.animation = "idle"

func _process(_delta: float) -> void:
	player = get_tree().get_nodes_in_group("player")[0]
	
	if $ShapeCastLeft.is_colliding():
		player_direction = -1
	elif $ShapeCastRight.is_colliding():
		player_direction = 1
	
	$Sprite.flip_h = true if player_direction == -1 else false
	$Label.text = str(health)

func found_player():
	return $ShapeCastLeft.is_colliding() or $ShapeCastRight.is_colliding()

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity += get_gravity() * delta
	
	if health > 0:
		if not taking_action() and ($RayCastLeft.is_colliding() or $RayCastRight.is_colliding()):
			player.attacked()
			$Sprite.animation = "attack"
			$EnemyAudio.stream = load("res://assets/audio/sword-swing.mp3")
			$EnemyAudio.play()
		
		if (!($RayCastLeft.is_colliding() or $RayCastRight.is_colliding()) and found_player()) and not taking_action():
			if ((not (($RayCastLeftTerrain.is_colliding() and player_direction == -1)
				or $RayCastRightTerrain.is_colliding() and player_direction == 1)) 
				and ((($RayCastDownLeft.is_colliding() and player_direction == -1)
				or $RayCastDownRight.is_colliding() and player_direction == 1))):
				
				velocity.x = SPEED * player_direction
				$Sprite.animation = "run"
			else:
				velocity.x = 0
				$Sprite.animation = "idle"
		else:
			if not taking_action(): $Sprite.animation = "idle"
			velocity.x = 0
	
	move_and_slide()

func attacked():
	if health <= 0:
		return
	health -= 1
	$Sprite.animation = "hurt"
	$EnemyAudio.stream = load("res://assets/audio/hurt.mp3") if health != 0 else load("res://assets/audio/death.mp3")
	$EnemyAudio.play()
	if health == 0:
		velocity = Vector2()
		Controller.enemies_defeated.append(uuid)

func taking_action():
	return $Sprite.animation == "hurt" or $Sprite.animation == "attack"

func _on_sprite_animation_looped() -> void:
	if taking_action():
		$Sprite.animation = "idle"

func _on_enemy_audio_finished() -> void:
	if health <= 0:
		if gives_coin: Controller.coins_collected.append(uuid)
		queue_free()
