# Documentation for src/brotato-style-game/Game/Shop/weapon_selection.gd

# AI Summary
This file is a part of a game's shop system. It handles the selection and purchase of weapons. The file includes functions for setting up the weapon selection UI, checking if the player can afford and can carry the weapon, and handling the purchase of the weapon. It also includes a function for checking if the weapon can be merged with an existing weapon in the player's inventory.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where the code could be more concise. The naming of variables and functions is generally good, but there are a few instances where the names could be more descriptive. The code follows the conventions of the Godot game engine, but there are a few areas where the code could be more consistent with these conventions.
# Functions

## _ready
### Explanation
This function is called when the node enters the scene tree for the first time. It sets up the initial state of the weapon selection UI, including the image, title, and stats of the weapon. It also checks if the player can afford the weapon and if they have space in their inventory.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
```

## _process
### Explanation
This function is called every frame. It checks if the player can afford the weapon and if they have space in their inventory. If not, it disables the buy button. If they can, it enables the buy button.
### Code
```gdscript
func _process(_delta: float) -> void:
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	else:
		buy.disabled = false
```

## _on_buy_pressed
### Explanation
This function is called when the buy button is pressed. It checks if the player can afford the weapon. If they can, it subtracts the cost of the weapon from the player's coins and adds the weapon to the player's inventory. If the player's inventory is full, it checks if the weapon can be merged with an existing weapon in the inventory. If it can, it merges the weapons.
### Code
```gdscript
func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		get_parent().get_parent().call_deferred("redo_selling")
		
		queue_free()
	elif len(Stats.current_weapons) == Stats.max_weapons:
		Stats.coins -= data.cost
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				w.merge_factor += 1
				get_parent().get_parent().call_deferred("redo_selling")
				queue_free()
				break
```

## can_merge
### Explanation
This function checks if the weapon can be merged with an existing weapon in the player's inventory. It does this by checking if there is a weapon in the inventory with the same name and merge factor as the current weapon.
### Code
```gdscript
func can_merge():
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			return true
	return false
```
# Overall File Contents
```gdscript
extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats
@onready var buy: Button = %Buy

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true

func _process(_delta: float) -> void:
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	else:
		buy.disabled = false

func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		get_parent().get_parent().call_deferred("redo_selling")
		
		queue_free()
	elif len(Stats.current_weapons) == Stats.max_weapons:
		Stats.coins -= data.cost
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				w.merge_factor += 1
				get_parent().get_parent().call_deferred("redo_selling")
				queue_free()
				break

func can_merge():
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			return true
	return false

```
