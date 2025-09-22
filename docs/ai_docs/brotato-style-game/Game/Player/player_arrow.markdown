# Documentation for src/brotato-style-game/Game/Player/player_arrow.gd

# AI Summary
This file defines the behavior of a player arrow in a game. The arrow is initialized with a target and damage value, and its direction and velocity are set towards the target. The arrow can bounce off walls and other objects, and its direction and velocity can be updated if it is tracing the target. The arrow is removed when it exits the screen or when it has hit the target enough times.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand, but there are some areas where the naming conventions could be improved. The code is also well-commented, which makes it easier to understand.
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
Sets the initial rotation and direction of the player arrow towards the target.
### Code
```gdscript
func _ready():
	rotation = global_position.angle_to_point(target.global_position)
	direction = global_position.direction_to(target.global_position)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer
```

## _physics_process
### Explanation
Handles the physics processing for the player arrow.
### Code
```gdscript
func _physics_process(_delta: float) -> void:
	move_and_slide()
```

## _process
### Explanation
Handles the processing for the player arrow, including checking if the arrow has hit the target enough times to be removed and updating the direction and velocity of the arrow if it is tracing the target.
### Code
```gdscript
func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
	
	if Stats.arrow_tracing > 0 and target != null:
		rotation = global_position.angle_to_point(target.global_position)
		direction = global_position.direction_to(target.global_position)
		velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer
```

## _on_visible_on_screen_notifier_2d_screen_exited
### Explanation
Removes the player arrow when it exits the screen.
### Code
```gdscript
func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()
```

## _on_bounce_detecter_screen_exited
### Explanation
Handles the bouncing of the player arrow when it hits a wall or other object.
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

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
	
	if Stats.arrow_tracing > 0 and target != null:
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
