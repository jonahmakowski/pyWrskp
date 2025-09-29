# Documentation for src/brotato-style-game/Game/UIScenes/upgrade_selection_helper.gd

# AI Summary
This file is a script for a Godot game. It extends VBoxContainer and has three variables: rendered_upgrade, title, image, and description. The _ready function sets the text of the title and description labels and shows the image if the upgrade has an icon. The _on_button_pressed function applies the upgrade and changes the scene to the shop scene.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-written and follows the conventions of the Godot engine. However, there is a typo in the description variable name (desription instead of description).
# Functions

## _ready
### Explanation
This function is called when the node enters the scene tree for the first time. It sets the text of the title label to the name of the rendered upgrade and its rarity text. If the upgrade has an icon, it shows the image and sets its texture to the upgrade's icon. It also sets the text of the description label to the upgrade's description.
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
This function is called when the button is pressed. It applies the rendered upgrade and changes the scene to the shop scene.
### Code
```gdscript
func _on_button_pressed() -> void:
	rendered_upgrade.apply()
	get_tree().change_scene_to_packed(Scenes.shop)
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
	get_tree().change_scene_to_packed(Scenes.shop)

```
