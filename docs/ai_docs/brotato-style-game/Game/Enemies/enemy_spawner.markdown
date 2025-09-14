# Documentation for src/brotato-style-game/Game/Enemies/enemy_spawner.gd

# AI Summary
This GDScript file defines an enemy spawner for a 2D game. It extends Node2D and uses exported variables for maximum spawn coordinates. It manages enemy spawning based on a time interval and a maximum enemy limit. It includes functions to spawn a random enemy type at a random position, count existing enemies, and a process function to handle the spawning logic over time.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. Variable names are clear, and the logic for spawning and counting enemies is concise. The use of `@export` for configurable variables is good practice. The `_ready` function is empty but that's a common pattern in Godot when it's not needed. Adherence to GDScript conventions is good, with clear function signatures and snake_case for variables and functions.
# Functions

## _ready
### Explanation
This is an overridden Godot Engine function that is called when the node enters the scene tree. In this implementation, it does nothing.
### Code
```gdscript
func _ready() -> void:
	pass
```

## spawn_enemy
### Explanation
This function creates a new enemy instance at a random position within the defined max_x and max_y boundaries. It also assigns a random enemy type ("Archer", "Swordsman", or "Orc") and adds the new enemy as a child of the current node's parent.
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
This function iterates through all children of the parent node and counts how many of them are in the "enemy" group, returning the total count.
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
This is an overridden Godot Engine function called every frame. It manages the enemy spawning interval. If the current interval exceeds the defined "interval", it resets the counter and, if the number of enemies is below "max_enemies", it calls the `spawn_enemy` function.
### Code
```gdscript
func _process(delta: float) -> void:
	current_interval += delta
	if current_interval >= interval:
		current_interval = 0.0
		if count_enemies() < max_enemies:
			spawn_enemy()
```
# Overall File Contents
```gdscript
extends Node2D

@export var max_x: int
@export var max_y: int
var interval = 1
var max_enemies = 10

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
	if current_interval >= interval:
		current_interval = 0.0
		if count_enemies() < max_enemies:
			spawn_enemy()

```
