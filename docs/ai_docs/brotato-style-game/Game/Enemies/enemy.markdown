# Documentation for src/brotato-style-game/Game/Enemies/enemy.gd

# AI Summary
This code defines an enemy in a game, handling various aspects such as initialization, movement, attacking, taking damage, and handling animations. The enemy can be of different types, including an archer who can fire arrows.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more strictly to conventions.
# Functions

## init
### Explanation
Initializes the enemy with a specific type.
### Code
```gdscript
func init(type):
	enemy_type = type
```

## _ready
### Explanation
Sets up the enemy's initial state, including showing the sprite, setting health, and configuring the timer.
### Code
```gdscript
func _ready() -> void:
	sprite.show()
	health = Stats.ENEMY_HEALTHS[enemy_type] * Stats.enemy_health_multiplyer
	timer.wait_time = Stats.ENEMY_COOLDOWN[enemy_type]
```

## find_player
### Explanation
Finds the player in the game world.
### Code
```gdscript
func find_player():
	var player = null
	for child in get_parent().get_children():
		if child.is_in_group("player"):
			player = child
	
	return player
```

## _physics_process
### Explanation
Handles the physics processing for the enemy, including movement and attacking.
### Code
```gdscript
func _physics_process(delta: float) -> void:
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
```

## fire_arrow
### Explanation
Fires an arrow from the enemy.
### Code
```gdscript
func fire_arrow():
	var instance = Scenes.enemy_arrow.instantiate()
	instance.global_position = global_position
	get_parent().add_child(instance)
```

## attack
### Explanation
Handles the enemy's attack, including setting the attack animation and dealing damage to the player.
### Code
```gdscript
func attack():
	attacking = true
	sprite.animation = "Attack"
	sprite.frame = 0
	if enemy_type != "Archer":
		var player = find_player()
		player.take_damage(Stats.ENEMY_DAMAGE[enemy_type] * Stats.enemy_damage_multiplyer)
	timer.start()
```

## _process
### Explanation
Handles the main process loop for the enemy, including updating the health label and checking for attacks.
### Code
```gdscript
func _process(delta: float) -> void:
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
```

## _on_animation_finished
### Explanation
Handles what happens when an animation finishes, including removing the enemy if it's dead and firing an arrow if it's an archer.
### Code
```gdscript
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
```

## _on_timer_timeout
### Explanation
Handles the timer timeout event, setting the attacking flag to false.
### Code
```gdscript
func _on_timer_timeout() -> void:
	attacking = false
```

## _on_navigation_agent_2d_velocity_computed
### Explanation
Handles the velocity computation for the navigation agent, setting the velocity based on whether the enemy is attacking or not.
### Code
```gdscript
func _on_navigation_agent_2d_velocity_computed(safe_velocity: Vector2) -> void:
	if not attacking: velocity = safe_velocity
	else: velocity = Vector2()
	move_and_slide()
```

## take_damage
### Explanation
Handles the enemy taking damage, updating the health and setting the appropriate animation.
### Code
```gdscript
func take_damage(amount):
	health -= amount
	if health <= 0:
		sprite.animation = "Death"
	else:
		sprite.animation = "Hurt"
```

## _on_area_2d_body_entered
### Explanation
Handles when a body enters the enemy's area, taking damage and incrementing the hits count.
### Code
```gdscript
func _on_area_2d_body_entered(body: Node2D) -> void:
	take_damage(body.damage)
	body.hits += 1
```
# Overall File Contents
```gdscript
extends CharacterBody2D

@export var enemy_type = "Archer"

var health
var attacking = false

@onready var sprite: AnimatedSprite2D = get_node("Sprites/" + str(enemy_type))
@onready var timer: Timer = $Timer
@onready var navigation_agent_2d: NavigationAgent2D = %NavigationAgent2D
@onready var health_label: Label = $HealthLabel

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

func _physics_process(delta: float) -> void:
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

func _process(delta: float) -> void:
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

```
