# Documentation for src/brotato-style-game/Game/UIScenes/upgrade_selection.gd

# AI Summary
This script extends an HBoxContainer and is responsible for creating and managing upgrade selection instances. It initializes a set number of upgrade options when the node is ready and changes the scene to level1 when an upgrade is selected.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and follows Godot's conventions. The functionality is clear and concise, with appropriate use of classes and methods.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It creates a number of upgrade selection helper instances equal to the number of upgrades specified in the Stats class. Each instance is configured with a random upgrade and added to the scene.
### Code
```gdscript
func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		add_child(instance)
```

## selected_upgrade
### Explanation
This function changes the scene to the level1 scene when called. It is likely triggered by some user interaction, such as selecting an upgrade.
### Code
```gdscript
func selected_upgrade():
	get_tree().change_scene_to_packed(Scenes.level1)
```
# Overall File Contents
```gdscript
extends HBoxContainer

func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		add_child(instance)

func selected_upgrade():
	get_tree().change_scene_to_packed(Scenes.level1)

```
