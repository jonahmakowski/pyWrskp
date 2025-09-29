# Documentation for src/brotato-style-game/Game/Shop/weapon_selling.gd

# AI Summary
This file is a Godot script that extends the Control node. It is responsible for displaying and managing a weapon in a shop. The script sets up the weapon's image, title, and stats, and provides functionality for selling and merging weapons.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-written and follows the Godot scripting conventions. However, there are a few areas where the code could be improved, such as the use of hard-coded values and the lack of comments.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets up the weapon's image, title, and stats, and connects the check_merge function to the WEAPON_CHANGE signal.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	if Stats.damage_multiplyer != 1:
		stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	else:
		stats.text = "Damage: {0}\n".format([data.damage])
	
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])
	
	check_merge()
	Messanger.WEAPON_CHANGE.connect(check_merge)
```

## _on_sell_pressed
### Explanation
This function is called when the sell button is pressed. It removes the weapon from the current weapons list, adds the refund value to the coins, and calls the redo_selling function.
### Code
```gdscript
func _on_sell_pressed() -> void:
	var index = 0
	for w in Stats.current_weapons:
		if w.name == data.name and data.cost == w.cost:
			Stats.current_weapons.remove_at(index)
			break
		index += 1
	
	Stats.coins += int(data.cost * (Stats.refund_rate / 100.0))
	get_parent().get_parent().get_parent().redo_selling()
```

## check_merge
### Explanation
This function checks if the weapon can be merged and sets the merge button's disabled property accordingly.
### Code
```gdscript
func check_merge() -> void:
	if not can_merge():
		merge.disabled = true
	else:
		merge.disabled = false
```

## _on_merge_pressed
### Explanation
This function is called when the merge button is pressed. It checks if the weapon can be merged, finds the other weapon to merge with, removes the other weapon from the current weapons list, increases the merge factor of the current weapon, and emits the REDO_SELLING signal.
### Code
```gdscript
func _on_merge_pressed() -> void:
	if can_merge():
		var merger: weapon
		var index = 0
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				@warning_ignore("unassigned_variable")
				if merger == null:
					merger = w
				else:
					break
			index += 1
		
		Stats.current_weapons.remove_at(index)
		merger.merge_factor += 1
		Messanger.REDO_SELLING.emit()
```

## can_merge
### Explanation
This function checks if there are two weapons with the same name and merge factor in the current weapons list.
### Code
```gdscript
func can_merge():
	var existing = 0
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			existing += 1
			
			if existing == 2:
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
@onready var merge: Button = %Merge


func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	if Stats.damage_multiplyer != 1:
		stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	else:
		stats.text = "Damage: {0}\n".format([data.damage])
	
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])
	
	check_merge()
	Messanger.WEAPON_CHANGE.connect(check_merge)

func _on_sell_pressed() -> void:
	var index = 0
	for w in Stats.current_weapons:
		if w.name == data.name and data.cost == w.cost:
			Stats.current_weapons.remove_at(index)
			break
		index += 1
	
	Stats.coins += int(data.cost * (Stats.refund_rate / 100.0))
	get_parent().get_parent().get_parent().redo_selling()

func check_merge() -> void:
	if not can_merge():
		merge.disabled = true
	else:
		merge.disabled = false

func _on_merge_pressed() -> void:
	if can_merge():
		var merger: weapon
		var index = 0
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				@warning_ignore("unassigned_variable")
				if merger == null:
					merger = w
				else:
					break
			index += 1
		
		Stats.current_weapons.remove_at(index)
		merger.merge_factor += 1
		Messanger.REDO_SELLING.emit()

func can_merge():
	var existing = 0
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			existing += 1
			
			if existing == 2:
				return true
	return false

```
