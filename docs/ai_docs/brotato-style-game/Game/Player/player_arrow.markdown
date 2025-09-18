# Documentation for src/brotato-style-game/Game/Player/player_arrow.gd

# AI Summary
This file defines a player arrow in a game. The player arrow is a CharacterBody2D that moves towards a target and deals damage. The player arrow can pierce through enemies and is destroyed when it exits the screen or when it has pierced through too many enemies.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, the variable names could be more descriptive, and there could be more comments to explain the code.
# Functions

## init
### Explanation
This function initializes the target and damage variables.
### Code
```gdscript
func init(t, d):
	target = t
	damage = d
```

## _ready
### Explanation
This function sets the rotation and direction of the player arrow based on the target, and sets the velocity of the arrow.
### Code
```gdscript
func _ready():
	rotation = global_position.angle_to_point(target)
	direction = global_position.direction_to(target)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer
```

## _physics_process
### Explanation
This function moves the player arrow using the move_and_slide function.
### Code
```gdscript
func _physics_process(_delta: float) -> void:
	move_and_slide()
```

## _process
### Explanation
This function checks if the number of hits is greater than the piercing stat, and if so, frees the player arrow.
### Code
```gdscript
func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
```

## _on_visible_on_screen_notifier_2d_screen_exited
### Explanation
This function frees the player arrow when it exits the screen.
### Code
```gdscript
func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()
```
# Overall File Contents
```gdscript
extends CharacterBody2D

var direction: Vector2
var target: Vector2
var damage: float
var hits = 0

func init(t, d):
	target = t
	damage = d

func _ready():
	rotation = global_position.angle_to_point(target)
	direction = global_position.direction_to(target)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _physics_process(_delta: float) -> void:
	move_and_slide()

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()

```
