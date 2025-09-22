# Documentation for src/brotato-style-game/Game/Shop/shop.gd

# AI Summary
This file defines a shop system for a game. It manages the weapons available for purchase, updates the display of weapons for sale, and handles the logic for when a button is pressed, which affects enemy stats and advances the level.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more closely to conventions.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It initializes the weapons_with_weights array by appending each weapon according to its weight. It then calls redo_selling() to update the weapon selling display. Finally, it creates instances of shop_weapon_selection for each weapon in the shop and adds them to the weapon_selection container.
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
This function updates the weapon selling display. It first removes all children from the weapon_selling container. Then, for each weapon in Stats.current_weapons, it creates an instance of shop_weapon_selling, sets its data to the weapon, and adds it to the weapon_selling container.
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
This function is called when a button is pressed. It decreases the enemy spawn rate based on its current value. It then increases various enemy stats and increments the level. Finally, it changes the scene to level1.
### Code
```gdscript
func _on_button_pressed() -> void:
	if Stats.enemy_spawn_rate > 1:
		Stats.enemy_spawn_rate -= 0.25
	elif Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	elif Stats.enemy_spawn_rate > 0.005:
		Stats.enemy_spawn_rate -= 0.001
	
	Stats.enemy_health_multiplyer += 0.1
	Stats.enemy_damage_multiplyer += 0.1
	Stats.enemy_speed_multiplyer += 0.1
	Stats.enemy_projectile_speed_multiplyer += 0.05
	
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
		Stats.enemy_spawn_rate -= 0.25
	elif Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	elif Stats.enemy_spawn_rate > 0.005:
		Stats.enemy_spawn_rate -= 0.001
	
	Stats.enemy_health_multiplyer += 0.1
	Stats.enemy_damage_multiplyer += 0.1
	Stats.enemy_speed_multiplyer += 0.1
	Stats.enemy_projectile_speed_multiplyer += 0.05
	
	Stats.level += 1
	
	get_tree().change_scene_to_packed(Scenes.level1)

```
