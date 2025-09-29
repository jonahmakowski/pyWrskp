# Documentation for src/brotato-style-game/Game/UIScenes/upgrade_selection.gd

# AI Summary
This file extends a Control node and sets up an upgrade box. The _ready function creates and adds upgrade selection instances to the upgrade box.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is generally well-structured and follows conventions. The naming is clear, and the functionality is concise.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It creates and adds upgrade selection instances to the upgrade box.
### Code
```gdscript
func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		upgrade_box.add_child(instance)
```
# Overall File Contents
```gdscript
extends Control

@onready var upgrade_box: HBoxContainer = %UpgradeBox

func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		upgrade_box.add_child(instance)

```
