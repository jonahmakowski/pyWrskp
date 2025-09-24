# Documentation for src/brotato-style-game/Game/Player/player_arrow.gd

# AI Summary
This file defines a player arrow in a game. It handles the initialization, movement, and interactions of the arrow, including targeting enemies, bouncing off surfaces, and being freed when it exits the screen or hits a certain number of times.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some areas where it could be more concise and adhere more closely to conventions.
# Functions

## init
### Explanation
Initializes the player arrow with a target and damage value.
### Code
```gdscript
func init(t, d):
	target = t
	damage = d
```

## _ready
### Explanation
Sets the initial rotation and direction of the arrow towards the target.
### Code
```gdscript
func _ready():
	rotation = global_position.angle_to_point(target.global_position)
	direction = global_position.direction_to(target.global_position)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer
```

## _physics_process
### Explanation
Handles the physics processing for the arrow.
### Code
```gdscript
func _physics_process(_delta: float) -> void:
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
Gets a list of enemies and sorts them by distance.
### Code
```gdscript
func get_enemies() -> Array:
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
Handles the main processing for the arrow, including checking if the arrow should be freed, updating the target if necessary, and updating the rotation and direction towards the target.
### Code
```gdscript
func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
		return
	
	if target == null and Stats.arrow_tracing > 0:
		target = get_enemies()[0]['instance']
	
	if Stats.arrow_tracing > 0:
		rotation = global_position.angle_to_point(target.global_position)
		direction = global_position.direction_to(target.global_position)
		velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer
```

## _on_visible_on_screen_notifier_2d_screen_exited
### Explanation
Handles the event when the arrow exits the screen.
### Code
```gdscript
func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()
```

## _on_bounce_detecter_screen_exited
### Explanation
Handles the event when the arrow bounces off a surface.
### Code
```gdscript
func _on_bounce_detecter_screen_exited() -> void:
	if bounces >= Stats.projectile_bounces:
		return
	
	velocity *= -1
	rotation_degrees += 180
	bounces += 1
```
# Overall File Contents
```gdscript
extends CharacterBody2D

var direction: Vector2
var target: CharacterBody2D
var damage: float
var hits = 0
var bounces = 0

func init(t, d):
	target = t
	damage = d

func _ready():
	rotation = global_position.angle_to_point(target.global_position)
	direction = global_position.direction_to(target.global_position)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _physics_process(_delta: float) -> void:
	move_and_slide()

func enemy_sort(a, b): # by distance
	if a["distance"] < b["distance"]:
		return true
	return false

func get_enemies() -> Array:
	var enemies = []
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			if child.sprite.animation == "Death":
				continue
			enemies.append({"enemy": child.enemy_type, "position": child.global_position, "distance": global_position.distance_to(child.global_position), "instance": child})
	
	enemies.sort_custom(enemy_sort)
	
	return enemies

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
		return
	
	if target == null and Stats.arrow_tracing > 0:
		target = get_enemies()[0]['instance']
	
	if Stats.arrow_tracing > 0:
		rotation = global_position.angle_to_point(target.global_position)
		direction = global_position.direction_to(target.global_position)
		velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()

func _on_bounce_detecter_screen_exited() -> void:
	if bounces >= Stats.projectile_bounces:
		return
	
	velocity *= -1
	rotation_degrees += 180
	bounces += 1

```
