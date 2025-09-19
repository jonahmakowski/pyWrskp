# Documentation for src/brotato-style-game/Game/Shop/shop.gd

# AI Summary
This file defines a shop system in a game. It includes functions to initialize the shop, update the weapon selling display, get a random weapon, and handle button press events. The shop system allows players to buy and sell weapons, and it also manages the game's difficulty by increasing the maximum number of enemies and decreasing the enemy spawn rate as the player progresses through levels.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise or follow conventions more closely. For example, the _on_button_pressed function could be split into smaller functions to improve readability. Additionally, the code could benefit from more comments to explain the purpose of certain variables and functions.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It initializes the weapons_with_weights array by appending each weapon according to its weight. It then calls redo_selling() to update the weapon selling display. Finally, it creates instances of shop_weapon_selection for each weapon in the shop.
### Code
```gdscript
func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	redo_selling()
	
	for i in range(Stats.weapons_in_shop):
		var instance = Scenes.shop_weapon_selection.instantiate()
		instance.data = get_random_weapon()
		weapon_selection.add_child(instance)
```

## redo_selling
### Explanation
This function updates the weapon selling display. It first removes all existing children from the weapon_selling container. Then, it creates instances of shop_weapon_selling for each weapon in the current_weapons array and adds them to the weapon_selling container.
### Code
```gdscript
func redo_selling():
	for child in weapon_selling.get_children():
		child.queue_free()
	
	for w in Stats.current_weapons:
		var instance = Scenes.shop_weapon_selling.instantiate()
		instance.data = w
		weapon_selling.add_child(instance)
```

## get_random_weapon
### Explanation
This function returns a random weapon from the weapons_with_weights array. It generates a random index within the range of the array and returns the weapon at that index.
### Code
```gdscript
func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]
```

## _on_button_pressed
### Explanation
This function is called when the button is pressed. It increases the maximum number of enemies, decreases the enemy spawn rate if it is greater than 0.05, increases the level, and changes the scene to level1.
### Code
```gdscript
func _on_button_pressed() -> void:
	Stats.max_enemies += 1
	if Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	Stats.level += 1
	get_tree().change_scene_to_packed(Scenes.level1)
```
# Overall File Contents
```gdscript
extends Control

@export var weapons: Array[weapon]
var weapons_with_weights: Array[weapon]
@onready var weapon_selling: HBoxContainer = %WeaponSelling
@onready var weapon_selection: HBoxContainer = %WeaponSelection

func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	redo_selling()
	
	for i in range(Stats.weapons_in_shop):
		var instance = Scenes.shop_weapon_selection.instantiate()
		instance.data = get_random_weapon()
		weapon_selection.add_child(instance)

func redo_selling():
	for child in weapon_selling.get_children():
		child.queue_free()
	
	for w in Stats.current_weapons:
		var instance = Scenes.shop_weapon_selling.instantiate()
		instance.data = w
		weapon_selling.add_child(instance)

func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]

func _on_button_pressed() -> void:
	Stats.max_enemies += 1
	if Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	Stats.level += 1
	get_tree().change_scene_to_packed(Scenes.level1)

```
