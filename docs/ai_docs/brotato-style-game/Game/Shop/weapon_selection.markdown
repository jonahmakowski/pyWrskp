# Documentation for src/brotato-style-game/Game/Shop/weapon_selection.gd

# AI Summary
This file is a part of a larger game project. It is responsible for displaying and managing the selection of weapons in the game's shop. It uses the Godot game engine and is written in the GDScript language. The file extends the Control node and has several functions that are called at different times to set up the weapon's image, title, and stats, enable or disable the buy button, and handle the buying of weapons.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is generally well-written and follows the conventions of the GDScript language. However, there are a few areas where the code could be improved, such as the use of magic numbers and the lack of comments to explain the code's functionality.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets up the weapon's image, title, and stats. It also connects to the MONEY_CHANGE and WEAPON_CHANGE signals and calls reroll_enabled.
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
	
	Messanger.MONEY_CHANGE.connect(reroll_enabled)
	Messanger.WEAPON_CHANGE.connect(reroll_enabled)
	reroll_enabled()
```

## reroll_enabled
### Explanation
This function is called when the MONEY_CHANGE or WEAPON_CHANGE signal is emitted. It enables or disables the buy button based on the player's coins and the number of weapons they currently have.
### Code
```gdscript
func reroll_enabled() -> void:
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	else:
		buy.disabled = false
```

## _on_buy_pressed
### Explanation
This function is called when the buy button is pressed. It checks if the player has enough coins to buy the weapon. If they do, it subtracts the cost of the weapon from the player's coins and adds the weapon to the player's current weapons. If the player already has the maximum number of weapons, it checks if any of the weapons can be merged with the new weapon. If they can, it merges them.
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
This function checks if any of the player's current weapons can be merged with the new weapon. It returns true if they can, and false if they cannot.
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
	
	Messanger.MONEY_CHANGE.connect(reroll_enabled)
	Messanger.WEAPON_CHANGE.connect(reroll_enabled)
	reroll_enabled()

func reroll_enabled() -> void:
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
