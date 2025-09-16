# Documentation for src/brotato-style-game/Game/UIScenes/upgrade_selection_helper.gd

# AI Summary
This file is a helper for the upgrade selection in the game. It extends VBoxContainer and has functions to set the title, image, and description of the upgrade, and to handle the button press event.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there is a typo in the description variable name (desription instead of description). The code could be more concise by combining some of the operations.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets the title of the upgrade, shows the image if the upgrade has an icon, and sets the description of the upgrade.
### Code
```gdscript
func _ready() -> void:
	title.text = rendered_upgrade.name + " ({0})".format([rendered_upgrade.rarity_text])
	
	if rendered_upgrade.has_icon:
		image.show()
		image.texture = rendered_upgrade.icon
	
	description.text = rendered_upgrade.desription
```

## _on_button_pressed
### Explanation
This function is called when the button is pressed. It applies the upgrade and calls the selected_upgrade function of the parent node.
### Code
```gdscript
func _on_button_pressed() -> void:
	rendered_upgrade.apply()
	get_parent().selected_upgrade()
```
# Overall File Contents
```gdscript
extends VBoxContainer

var rendered_upgrade: upgrade

@onready var title: Label = %Title
@onready var image: TextureRect = %Image
@onready var description: Label = %Description

func _ready() -> void:
	title.text = rendered_upgrade.name + " ({0})".format([rendered_upgrade.rarity_text])
	
	if rendered_upgrade.has_icon:
		image.show()
		image.texture = rendered_upgrade.icon
	
	description.text = rendered_upgrade.desription

func _on_button_pressed() -> void:
	rendered_upgrade.apply()
	get_parent().selected_upgrade()

```
