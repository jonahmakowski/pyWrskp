extends CharacterBody2D

@export var enemy_type = "Archer"

var health
var attacking = false
var death_targeted = false

@onready var sprite: AnimatedSprite2D = get_node("Sprites/" + str(enemy_type))
@onready var timer: Timer = $Timer
@onready var navigation_agent_2d: NavigationAgent2D = %NavigationAgent2D
@onready var health_label: Label = $HealthLabel
@onready var death_targeted_timeout: Timer = %DeathTargetedTimeout

func init(type):
	enemy_type = type

func _ready() -> void:
	sprite.show()
	health = Stats.ENEMY_HEALTHS[enemy_type] * Stats.enemy_health_multiplyer
	timer.wait_time = Stats.ENEMY_COOLDOWN[enemy_type]

func find_player():
	var player = null
	for child in get_parent().get_children():
		if child.is_in_group("player"):
			player = child
	
	return player

func _physics_process(_delta: float) -> void:
	var player = find_player()
	
	if player == null:
		navigation_agent_2d.target_position = global_position
		return
	
	if (sprite.animation == "Death" or sprite.animation == "Attack") or sprite.animation == "Hurt":
		navigation_agent_2d.set_velocity(Vector2())
		return
	
	navigation_agent_2d.target_position = player.global_position
	
	if global_position.distance_to(player.global_position) <= (Stats.ENEMY_RANGE[enemy_type] * Stats.enemy_range_multiplyer):
		sprite.animation = "Idle"
		return
	
	var destination = navigation_agent_2d.get_next_path_position()
	var direction = global_position.direction_to(destination)
	
	if direction:
		if sprite.animation == "Idle":
			sprite.animation = "Walking"
		if direction.x < 0:
			sprite.flip_h = true
		elif direction.x > 0:
			sprite.flip_h = false
	
	var d_velocity = direction * Stats.ENEMY_SPEED * Stats.enemy_speed_multiplyer
	navigation_agent_2d.set_velocity(d_velocity)

func fire_arrow():
	var instance = Scenes.enemy_arrow.instantiate()
	instance.global_position = global_position
	get_parent().add_child(instance)

func attack():
	attacking = true
	sprite.animation = "Attack"
	sprite.frame = 0
	if enemy_type != "Archer":
		var player = find_player()
		player.take_damage(Stats.ENEMY_DAMAGE[enemy_type] * Stats.enemy_damage_multiplyer)
	timer.start()

func _process(_delta: float) -> void:
	health_label.text = "Health: {0}".format([health if health > 0 else 0])
	if Input.is_action_pressed("show_enemy_health"):
		health_label.show()
	else:
		health_label.hide()
	
	if sprite.animation == "Death":
		return
	
	var player = find_player()
	
	if player == null:
		return
	
	if global_position.distance_to(player.global_position) <= Stats.ENEMY_RANGE[enemy_type] and not attacking:
		attack()
	
	if death_targeted:
		death_targeted_timeout.start()


func _on_animation_finished() -> void:
	if sprite.animation == "Death":
		queue_free()
		Stats.enemies_killed += 1
		var coin = Scenes.coin.instantiate()
		coin.init(Stats.death_value)
		coin.global_position = global_position
		add_sibling(coin)
	elif sprite.animation == "Attack" and enemy_type == "Archer":
		fire_arrow()
	sprite.animation = "Idle"
	sprite.play()


func _on_timer_timeout() -> void:
	attacking = false

func _on_navigation_agent_2d_velocity_computed(safe_velocity: Vector2) -> void:
	if not attacking: velocity = safe_velocity
	else: velocity = Vector2()
	move_and_slide()

func take_damage(amount):
	health -= amount
	if health <= 0:
		sprite.animation = "Death"
	else:
		sprite.animation = "Hurt"

func _on_area_2d_body_entered(body: Node2D) -> void:
	take_damage(body.damage)
	body.hits += 1

func _on_death_targeted_timeout_timeout() -> void:
	death_targeted = false
