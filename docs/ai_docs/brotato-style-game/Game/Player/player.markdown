# Documentation for src/brotato-style-game/Game/Player/player.gd

# AI Summary
This file defines a player character in a 2D game, handling movement, health management, weapon management, and interaction with enemies. It includes functions for initialization, physics processing, enemy management, and UI updates.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more strictly to conventions.
# Functions

## _ready
### Explanation
Initializes the player's health, shows the sprite, clears existing weapons, adds current weapons to the weapon container, and sets the level label.
### Code
```gdscript
func _ready() -> void:
	Stats.current_health = Stats.max_health
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
Handles player movement and animation based on input direction.
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
Sorts enemies by distance.
### Code
```gdscript
func enemy_sort(a, b): # by distance
	if a["distance"] < b["distance"]:
		return true
	return false
```

## get_enemies
### Explanation
Retrieves a list of enemies, excluding those that are dead.
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
Updates the list of enemies, manages health regeneration, checks for player death, and updates various UI labels.
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
Reduces the player's health by the specified damage amount and plays the hurt animation.
### Code
```gdscript
func take_damage(damage: float):
	Stats.current_health -= damage
	sprite.play("Hurt")
```

## _on_arrow_detector_body_entered
### Explanation
Handles the event when an arrow enters the player's detection area, removing the arrow and applying damage.
### Code
```gdscript
func _on_arrow_detector_body_entered(body: Node2D) -> void:
	body.queue_free()
	take_damage(Stats.ENEMY_DAMAGE["Archer"] * Stats.enemy_damage_multiplyer)
```

## _on_animation_finished
### Explanation
Handles the event when an animation finishes, specifically resetting the sprite to the idle animation if it was hurt.
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
	Stats.current_health = Stats.max_health
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
