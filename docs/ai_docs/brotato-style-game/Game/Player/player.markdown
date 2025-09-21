# Documentation for src/brotato-style-game/Game/Player/player.gd

# AI Summary
This file defines a player character in a game. It handles player movement, health management, weapon management, and interactions with enemies. The player can move around the game world, take damage from enemies, and use weapons to defeat them. The file also includes functions for sorting and retrieving enemies, updating the player's health, and managing the game's UI elements.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where the code could be more concise or efficient. The code also follows the conventions of the Godot game engine, but there are a few instances where the code could be more consistent with the engine's conventions.
# Functions

## _ready
### Explanation
This function is called when the node enters the scene tree for the first time. It initializes the player's sprite, clears any existing weapons, adds the current weapons to the weapon container, and sets the level label text.
### Code
```gdscript
func _ready() -> void:
	sprite.show()
	
	for child in weapon_container.get_children():
		child.queue_free()
	
	for w in Stats.current_weapons:
		var instance = Scenes.player_weapon.instantiate()
		instance.data = w
		weapon_container.add_child(instance)
	
	level_label.text = "Level: {0}".format([Stats.level])
```

## _physics_process
### Explanation
This function is called during the physics process. It handles player movement and updates the player's sprite animation based on the direction of movement.
### Code
```gdscript
func _physics_process(_delta: float) -> void:
	var direction = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	if direction:
		if sprite.animation != "Hurt": sprite.animation = "Walking"
		if direction.x < 0:
			sprite.flip_h = true
		elif direction.x > 0:
			sprite.flip_h = false
	else:
		if sprite.animation != "Hurt": sprite.animation = "Idle"
	velocity = direction * Stats.SPEED * Stats.speed_multiplyer
	move_and_slide()
```

## enemy_sort
### Explanation
This function is used to sort enemies by their distance from the player.
### Code
```gdscript
func enemy_sort(a, b): # by distance
	if a["distance"] < b["distance"]:
		return true
	return false
```

## get_enemies
### Explanation
This function retrieves a list of enemies in the game, filters out enemies that are already dead, and sorts them by distance from the player.
### Code
```gdscript
func get_enemies():
	var enemies = []
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			if child.sprite.animation == "Death":
				continue
			enemies.append({"enemy": child.enemy_type, "position": child.global_position, "distance": global_position.distance_to(child.global_position), "instance": child})
	
	enemies.sort_custom(enemy_sort)
	
	return enemies
```

## _process
### Explanation
This function is called every frame. It updates the list of enemies, manages the player's health, updates the health, killed, coin, and time remaining labels, and checks if the player has died.
### Code
```gdscript
func _process(delta: float) -> void:
	enemies_list = get_enemies()
	
	if Stats.current_health < Stats.max_health:
		Stats.current_health += Stats.health_regen * delta
	if Stats.current_health > Stats.max_health:
		Stats.current_health = Stats.max_health
	
	if Stats.current_health <= 0:
		get_tree().change_scene_to_packed(Scenes.death_screen)
	
	health_label.text = "Health: {0}/{1}".format([round(Stats.current_health*10)/10, round(Stats.max_health*10)/10])
	killed_label.text = "Killed {0} enemies this round".format([Stats.enemies_killed])
	coin_label.text = "Coins: {0}".format([Stats.coins])
	time_remaining_label.text = "{0}s".format([round(get_parent().find_child("LevelOverTimer").time_left * 10) / 10])
```

## take_damage
### Explanation
This function reduces the player's health by the specified damage amount and plays the 'Hurt' animation.
### Code
```gdscript
func take_damage(damage: float):
	Stats.current_health -= damage
	sprite.play("Hurt")
```

## _on_arrow_detector_body_entered
### Explanation
This function is called when an arrow enters the arrow detector area. It removes the arrow from the game and applies damage to the player based on the archer's damage and the enemy damage multiplier.
### Code
```gdscript
func _on_arrow_detector_body_entered(body: Node2D) -> void:
	body.queue_free()
	take_damage(Stats.ENEMY_DAMAGE["Archer"] * Stats.enemy_damage_multiplyer)
```

## _on_animation_finished
### Explanation
This function is called when an animation finishes playing. If the animation is 'Hurt', it plays the 'Idle' animation.
### Code
```gdscript
func _on_animation_finished() -> void:
	if sprite.animation == "Hurt":
		sprite.play("Idle")
```
# Overall File Contents
```gdscript
extends CharacterBody2D

const PLAYER = 1
@onready var sprite: AnimatedSprite2D = get_node("Sprites/" + str(PLAYER))
@onready var arrow_detector: Area2D = %ArrowDetector
@onready var health_label: Label = %"Health Label"
@onready var killed_label: Label = %"Killed Label"
@onready var coin_label: Label = %"Coin Label"
@onready var time_remaining_label: Label = %TimeRemainingLabel
@onready var weapon_container: Node2D = %WeaponContainer
@onready var level_label: Label = %LevelLabel

var enemies_list = []

func _ready() -> void:
	sprite.show()
	
	for child in weapon_container.get_children():
		child.queue_free()
	
	for w in Stats.current_weapons:
		var instance = Scenes.player_weapon.instantiate()
		instance.data = w
		weapon_container.add_child(instance)
	
	level_label.text = "Level: {0}".format([Stats.level])

func _physics_process(_delta: float) -> void:
	var direction = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	if direction:
		if sprite.animation != "Hurt": sprite.animation = "Walking"
		if direction.x < 0:
			sprite.flip_h = true
		elif direction.x > 0:
			sprite.flip_h = false
	else:
		if sprite.animation != "Hurt": sprite.animation = "Idle"
	velocity = direction * Stats.SPEED * Stats.speed_multiplyer
	move_and_slide()

func enemy_sort(a, b): # by distance
	if a["distance"] < b["distance"]:
		return true
	return false

func get_enemies():
	var enemies = []
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			if child.sprite.animation == "Death":
				continue
			enemies.append({"enemy": child.enemy_type, "position": child.global_position, "distance": global_position.distance_to(child.global_position), "instance": child})
	
	enemies.sort_custom(enemy_sort)
	
	return enemies

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	enemies_list = get_enemies()
	
	if Stats.current_health < Stats.max_health:
		Stats.current_health += Stats.health_regen * delta
	if Stats.current_health > Stats.max_health:
		Stats.current_health = Stats.max_health
	
	if Stats.current_health <= 0:
		get_tree().change_scene_to_packed(Scenes.death_screen)
	
	health_label.text = "Health: {0}/{1}".format([round(Stats.current_health*10)/10, round(Stats.max_health*10)/10])
	killed_label.text = "Killed {0} enemies this round".format([Stats.enemies_killed])
	coin_label.text = "Coins: {0}".format([Stats.coins])
	time_remaining_label.text = "{0}s".format([round(get_parent().find_child("LevelOverTimer").time_left * 10) / 10])

func take_damage(damage: float):
	Stats.current_health -= damage
	sprite.play("Hurt")

func _on_arrow_detector_body_entered(body: Node2D) -> void:
	body.queue_free()
	take_damage(Stats.ENEMY_DAMAGE["Archer"] * Stats.enemy_damage_multiplyer)

func _on_animation_finished() -> void:
	if sprite.animation == "Hurt":
		sprite.play("Idle")

```
