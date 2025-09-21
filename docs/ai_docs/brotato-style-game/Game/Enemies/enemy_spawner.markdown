# Documentation for src/brotato-style-game/Game/Enemies/enemy_spawner.gd

# AI Summary
This file is a script for a Node2D in a game. It handles the spawning of enemies at random positions and counts the number of enemies in the game. The script uses exported variables to set the maximum x and y positions for enemy spawning. It also uses a current interval variable to control the rate at which enemies are spawned.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, the variable names could be more descriptive, and the code could be more concise in some places.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It does nothing in this case.
### Code
```gdscript
func _ready() -> void:
	pass
```

## spawn_enemy
### Explanation
This function spawns an enemy at a random position within the specified range. The enemy type is randomly selected from a list of types.
### Code
```gdscript
func spawn_enemy() -> void:
	var x_pos = randf_range(max_x, -max_x)
	var y_pos = randf_range(max_y, -max_y)
	var pos = Vector2(x_pos, y_pos)
	var type = ["Archer", "Swordsman", "Orc"][randi_range(0, 2)]
	
	var instance = Scenes.enemy.instantiate()
	instance.init(type)
	instance.position = pos
	
	get_parent().add_child(instance)
```

## count_enemies
### Explanation
This function counts the number of enemies in the game. It does this by iterating over all children of the parent node and checking if they are in the "enemy" group.
### Code
```gdscript
func count_enemies():
	var enemies = 0
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			enemies += 1
	
	return enemies
```

## _process
### Explanation
This function is called every frame. It increments the current interval by the delta time and spawns an enemy if the current interval is greater than or equal to the enemy spawn rate.
### Code
```gdscript
func _process(delta: float) -> void:
	current_interval += delta
	if current_interval >= Stats.enemy_spawn_rate:
		current_interval = 0.0
		spawn_enemy()
```
# Overall File Contents
```gdscript
extends Node2D

@export var max_x: int
@export var max_y: int

var current_interval = 0.0

func _ready() -> void:
	pass

func spawn_enemy() -> void:
	var x_pos = randf_range(max_x, -max_x)
	var y_pos = randf_range(max_y, -max_y)
	var pos = Vector2(x_pos, y_pos)
	var type = ["Archer", "Swordsman", "Orc"][randi_range(0, 2)]
	
	var instance = Scenes.enemy.instantiate()
	instance.init(type)
	instance.position = pos
	
	get_parent().add_child(instance)

func count_enemies():
	var enemies = 0
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			enemies += 1
	
	return enemies

func _process(delta: float) -> void:
	current_interval += delta
	if current_interval >= Stats.enemy_spawn_rate:
		current_interval = 0.0
		spawn_enemy()

```
