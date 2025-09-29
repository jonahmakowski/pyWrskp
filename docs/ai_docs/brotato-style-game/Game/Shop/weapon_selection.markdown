# Documentation for src/brotato-style-game/Game/Shop/weapon_selection.gd

# AI Summary
This file is a weapon selection script for a game. It handles the display of weapon information, the buying of weapons, and the merging of weapons. It uses the Stats and Messanger singletons to manage the player's coins, weapons, and other game state.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise or efficient. The code also follows the Godot engine's conventions for the most part, but there are some areas where the code could be more consistent.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets the image texture, updates the stats text based on the damage multiplier, and connects to the MONEY_CHANGE and WEAPON_CHANGE signals. It also calls the can_buy function.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	if Stats.damage_multiplyer != 1:
		stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	else:
		stats.text = "Damage: {0}\n".format([data.damage])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	
	Messanger.MONEY_CHANGE.connect(can_buy)
	Messanger.WEAPON_CHANGE.connect(can_buy)
	can_buy()
```

## can_buy
### Explanation
This function checks if the player can buy the weapon. It disables the buy button if the player doesn't have enough coins or if the player has reached the maximum number of weapons and cannot merge the weapon.
### Code
```gdscript
func can_buy() -> void:
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	else:
		buy.disabled = false
```

## _on_buy_pressed
### Explanation
This function is called when the buy button is pressed. It checks if the player can buy the weapon, subtracts the cost from the player's coins, and adds the weapon to the player's current weapons. If the player has reached the maximum number of weapons, it merges the weapon with an existing one.
### Code
```gdscript
func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		Messanger.REDO_SELLING.emit()
		
		queue_free()
	elif len(Stats.current_weapons) == Stats.max_weapons:
		Stats.coins -= data.cost
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				w.merge_factor += 1
				Messanger.REDO_SELLING.emit()
				queue_free()
				break
```

## can_merge
### Explanation
This function checks if the weapon can be merged with an existing one. It returns true if there is a weapon with the same name and merge factor.
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
	
	if Stats.damage_multiplyer != 1:
		stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	else:
		stats.text = "Damage: {0}\n".format([data.damage])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	
	Messanger.MONEY_CHANGE.connect(can_buy)
	Messanger.WEAPON_CHANGE.connect(can_buy)
	can_buy()

func can_buy() -> void:
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
		
		Messanger.REDO_SELLING.emit()
		
		queue_free()
	elif len(Stats.current_weapons) == Stats.max_weapons:
		Stats.coins -= data.cost
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				w.merge_factor += 1
				Messanger.REDO_SELLING.emit()
				queue_free()
				break

func can_merge():
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			return true
	return false

```
