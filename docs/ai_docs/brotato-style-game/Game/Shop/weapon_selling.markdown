# Documentation for src/brotato-style-game/Game/Shop/weapon_selling.gd

# AI Summary
This file is a part of a game's shop system. It handles the display and functionality of weapons in the shop. The weapons can be sold or merged, and the player's coins are updated accordingly. The code is well-structured and easy to understand, but there are some areas where it could be improved for better performance and readability.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-written and follows the conventions of the GDScript language. However, there are some areas where it could be improved for better performance and readability.
# Functions

## _ready
### Explanation
This function initializes the weapon's image, title, and stats. It also checks if the weapon can be merged and disables the merge button if it cannot.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])
	
	if not can_merge():
		merge.disabled = true
```

## _on_sell_pressed
### Explanation
This function handles the event when the sell button is pressed. It removes the weapon from the player's inventory and adds the refund value to the player's coins.
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

## _process
### Explanation
This function is called every frame. It checks if the weapon can be merged and updates the merge button's disabled state accordingly.
### Code
```gdscript
func _process(_delta: float) -> void:
	if not can_merge():
		merge.disabled = true
	else:
		merge.disabled = false
```

## _on_merge_pressed
### Explanation
This function handles the event when the merge button is pressed. It finds another weapon with the same name and merge factor, removes it from the player's inventory, and increases the merge factor of the current weapon.
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
		get_parent().get_parent().get_parent().call_deferred("redo_selling")
```

## can_merge
### Explanation
This function checks if the weapon can be merged. It does this by counting the number of weapons with the same name and merge factor in the player's inventory. If there are at least two such weapons, it returns true.
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
@onready var merge: Button = $VBoxContainer/Merge

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])
	
	if not can_merge():
		merge.disabled = true

func _on_sell_pressed() -> void:
	var index = 0
	for w in Stats.current_weapons:
		if w.name == data.name and data.cost == w.cost:
			Stats.current_weapons.remove_at(index)
			break
		index += 1
	
	Stats.coins += int(data.cost * (Stats.refund_rate / 100.0))
	get_parent().get_parent().get_parent().redo_selling()

func _process(_delta: float) -> void:
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
		get_parent().get_parent().get_parent().call_deferred("redo_selling")

func can_merge():
	var existing = 0
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			existing += 1
			
			if existing == 2:
				return true
	return false

```
