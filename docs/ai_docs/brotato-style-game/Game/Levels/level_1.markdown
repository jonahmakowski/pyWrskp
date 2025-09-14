# Documentation for src/brotato-style-game/Game/Levels/level_1.gd

# AI Summary
This file extends Node2D and defines two functions: _ready and _process. The _ready function bakes the navigation polygon for a NavigationRegion2D node, and the _process function does nothing.

The AI gave it a general rating of 5/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional but lacks comments and follows basic conventions.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It bakes the navigation polygon for the nav_region.
### Code
```godot
func _ready() -> void:
	nav_region.bake_navigation_polygon(true)
```

## _process
### Explanation
This function is called every frame. It does nothing in this case.
### Code
```godot
func _process(delta: float) -> void:
	pass
```
# Overall File Contents
```godot
extends Node2D

@onready var nav_region: NavigationRegion2D = %NavigationRegion2D
@onready var enemy_spawner: Node2D = %EnemySpawner


func _ready() -> void:
	nav_region.bake_navigation_polygon(true)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

```
