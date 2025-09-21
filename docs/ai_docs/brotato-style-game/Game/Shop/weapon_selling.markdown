# Documentation for src/brotato-style-game/Game/Shop/weapon_selling.gd

# AI Summary
This file defines a weapon display in a game. It handles the display of weapon information, selling weapons, and merging weapons. The code is well-structured and easy to understand, with clear function names and comments.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and follows conventions, with clear function names and comments. The functionality is clear and concise, with each function having a specific purpose.
# Functions

## _ready
### Explanation
This function is called when the node enters the scene tree for the first time. It sets up the initial state of the weapon display, including the image, title, and stats. It also disables the merge button if merging is not possible.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	stats.text = "Damage: {0}\n".format([data.damage])
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
This function is called when the sell button is pressed. It removes the weapon from the player's inventory and adds the refund value to the player's coins. It then refreshes the shop display.
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
This function is called every frame. It checks if merging is possible and updates the merge button's disabled state accordingly.
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
This function is called when the merge button is pressed. It finds another weapon with the same name and merge factor, removes it from the player's inventory, and increases the merge factor of the current weapon. It then refreshes the shop display.
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
This function checks if merging is possible by counting the number of weapons with the same name and merge factor. If there are at least two such weapons, it returns true.
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
	
	stats.text = "Damage: {0}\n".format([data.damage])
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
