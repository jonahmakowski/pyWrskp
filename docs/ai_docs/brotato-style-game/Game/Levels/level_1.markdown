# Documentation for src/brotato-style-game/Game/Levels/level_1.gd

# AI Summary
This file is a level script for a game. It extends Node2D and includes a navigation region, an enemy spawner, and a timer for the level. The _ready function sets up the navigation region and starts the timer. The _on_level_over_timer_timeout function handles what happens when the level timer runs out.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where it could be improved, such as adding comments to explain the purpose of the variables and functions, and using more descriptive variable names.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It bakes the navigation polygon for the nav_region, sets the wait time for the level_over_timer to Stats.level_time, and starts the timer.
### Code
```gdscript
func _ready() -> void:
	nav_region.bake_navigation_polygon(true)
	level_over_timer.wait_time = Stats.level_time
	level_over_timer.start()
```

## _on_level_over_timer_timeout
### Explanation
This function is called when the level_over_timer times out. It sets the current health of the player to the maximum health, and changes the scene to the upgrade selection scene.
### Code
```gdscript
func _on_level_over_timer_timeout() -> void:
	Stats.current_health = Stats.max_health
	get_tree().change_scene_to_packed(Scenes.upgrade_selection)
```
# Overall File Contents
```gdscript
extends Node2D

@onready var nav_region: NavigationRegion2D = %NavigationRegion2D
@onready var enemy_spawner: Node2D = %EnemySpawner
@onready var level_over_timer: Timer = $LevelOverTimer


func _ready() -> void:
	nav_region.bake_navigation_polygon(true)
	level_over_timer.wait_time = Stats.level_time
	level_over_timer.start()


func _on_level_over_timer_timeout() -> void:
	Stats.current_health = Stats.max_health
	get_tree().change_scene_to_packed(Scenes.upgrade_selection)

```
