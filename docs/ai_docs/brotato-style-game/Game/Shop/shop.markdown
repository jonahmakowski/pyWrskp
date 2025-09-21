# Documentation for src/brotato-style-game/Game/Shop/shop.gd

# AI Summary
This code is a part of a game's shop system. It manages the weapons in the shop, including their weights and the current weapons being sold. It also handles the button press event, which affects the enemy stats and changes the scene to the next level.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise, such as the nested loops in the _ready function. The code also adheres to the conventions of the Godot game engine, but there are some areas where the code could be more consistent, such as the naming of variables and functions.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It initializes the weapons_with_weights array by appending each weapon according to its weight. It then calls redo_selling() to update the selling weapons. Finally, it creates instances of shop_weapon_selection for each weapon in the shop and adds them to the weapon_selection container.
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
This function updates the selling weapons. It first removes all children from the weapon_selling container. Then, it creates instances of shop_weapon_selling for each weapon in the current_weapons array and adds them to the weapon_selling container.
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
This function returns a random weapon from the weapons_with_weights array.
### Code
```gdscript
func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]
```

## _on_button_pressed
### Explanation
This function is called when a button is pressed. It decreases the enemy_spawn_rate by 0.1 if it is greater than 1, or by 0.05 if it is greater than 0.05. It then increases various enemy stats by 0.05 or 0.02. Finally, it increases the level and changes the scene to level1.
### Code
```gdscript
func _on_button_pressed() -> void:
	if Stats.enemy_spawn_rate > 1:
		Stats.enemy_spawn_rate -= 0.1
	elif Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	
	Stats.enemy_health_multiplyer += 0.05
	Stats.enemy_damage_multiplyer += 0.05
	Stats.enemy_speed_multiplyer += 0.05
	Stats.enemy_projectile_speed_multiplyer += 0.02
	
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
	if Stats.enemy_spawn_rate > 1:
		Stats.enemy_spawn_rate -= 0.1
	elif Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	
	Stats.enemy_health_multiplyer += 0.05
	Stats.enemy_damage_multiplyer += 0.05
	Stats.enemy_speed_multiplyer += 0.05
	Stats.enemy_projectile_speed_multiplyer += 0.02
	
	Stats.level += 1
	
	get_tree().change_scene_to_packed(Scenes.level1)

```
