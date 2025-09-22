# Documentation for src/brotato-style-game/Game/Shop/weapon_selection.gd

# AI Summary
This file is a script for a weapon selection UI in a game. It sets up the UI, checks if the player can afford and add weapons, and handles the merging of weapons.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise. The code follows the conventions of the Godot game engine, but there are some areas where the code could be more consistent.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets up the initial state of the weapon selection UI, including the image, title, and stats of the weapon. It also checks if the player can afford the weapon and if there is space to add it to the player's current weapons.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
```

## _process
### Explanation
This function is called every frame. It checks if the player can afford the weapon and if there is space to add it to the player's current weapons. If not, it disables the buy button.
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
This function is called when the buy button is pressed. It checks if the player can afford the weapon. If the player has space in their current weapons, it adds the weapon to the player's current weapons. If the player's current weapons are full, it checks if there is a weapon with the same name and merge factor. If so, it increases the merge factor of that weapon.
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
This function checks if there is a weapon in the player's current weapons with the same name and merge factor as the current weapon. If so, it returns true, indicating that the weapon can be merged.
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
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
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
