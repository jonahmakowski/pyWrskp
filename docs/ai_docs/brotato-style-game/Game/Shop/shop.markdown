# Documentation for src/brotato-style-game/Game/Shop/shop.gd

# AI Summary
This GDScript file (`shop.gd`) is a core component of the game's shop and level progression system. It extends `Control` and manages the display and selection of weapons available to the player. It initializes a weighted list of weapons for random selection and dynamically populates UI elements for buying and selling weapons. Additionally, it contains logic for advancing to the next game level, which involves adjusting global enemy statistics like spawn rate, health, damage, and speed, as well as updating the level time and loading the next scene.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is generally well-structured and follows GDScript conventions, including the use of `@export` for editable properties, `@onready` for node references, and type hints for functions. The logic for weighted weapon selection and shop UI updates is clear. The `_on_button_pressed` function, while functional, could be slightly refactored to reduce repetition in the `enemy_spawn_rate` conditional logic, perhaps using a data-driven approach for spawn rate adjustments based on thresholds. Overall, it's clean and readable, but minor improvements could enhance its conciseness and maintainability.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It initializes the weapons_with_weights array by appending each weapon according to its weight, effectively creating a weighted random selection. It then calls `redo_selling()` to set up the selling section of the shop. Finally, it populates the `weapon_selection` HBoxContainer with instances of `Scenes.shop_weapon_selection`, assigning a randomly selected weapon to each instance.
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
This function updates the display of weapons currently being sold. It first clears any existing weapon display elements from the `weapon_selling` HBoxContainer. Then, for each weapon in `Stats.current_weapons`, it instantiates a `Scenes.shop_weapon_selling` scene, assigns the weapon data to it, and adds it to the `weapon_selling` container.
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
This function selects and returns a random weapon from the `weapons_with_weights` array. The `weapons_with_weights` array is pre-populated in `_ready()` to include multiple entries for weapons with higher "weight" values, ensuring a weighted random distribution.
### Code
```gdscript
func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]
```

## _on_button_pressed
### Explanation
This function is triggered when a button is pressed, likely signaling the progression to a new level or wave. It adjusts the `Stats.enemy_spawn_rate` based on a tiered reduction system. It then globally increases several enemy-related statistics such as health, damage, speed, and projectile speed. The `Stats.level_time` is also extended, and the `Stats.level` is incremented. Finally, it transitions the game scene to `Scenes.level1`.
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
	Stats.level_time += 2
	
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
	Stats.level_time += 2
	
	Stats.level += 1
	
	get_tree().change_scene_to_packed(Scenes.level1)

```
