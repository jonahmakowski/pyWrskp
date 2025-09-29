# Documentation for src/brotato-style-game/Game/Shop/shop.gd

# AI Summary
This file defines a shop in a game, where players can buy and sell weapons. It includes functions to initialize the shop, handle button presses, and manage the weapon selection and selling displays. The shop also includes a reroll feature that allows players to refresh the weapon selection for a cost.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where the code could be more concise or efficient. The adherence to conventions is good, but there are some areas where the code could be more consistent.
# Functions

## _ready
### Explanation
Initializes the shop by populating the weapons_with_weights array based on the weights of the weapons. It also connects various signals to their respective handlers and calls redo_selling and redo_selection functions. Finally, it connects the MONEY_CHANGE signal to the reroll_enabled function and calls reroll_enabled.
### Code
```gdscript
func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	Messanger.REDO_SELLING.connect(redo_selling)
	Messanger.WEAPON_CHANGE.connect(redo_selling)
	Messanger.REDO_SELECTION.connect(redo_selection)
	
	redo_selling()
	redo_selection()
	
	Messanger.MONEY_CHANGE.connect(reroll_enabled)
	reroll_enabled()
```

## redo_selection
### Explanation
Clears the current weapon selection and repopulates it with new random weapons. It does this by first freeing all existing children of the weapon_selection container, then instantiating new shop_weapon_selection scenes and setting their data to a randomly selected weapon.
### Code
```gdscript
func redo_selection():
	for child in weapon_selection.get_children():
		child.queue_free()
	
	for i in range(Stats.weapons_in_shop):
		var instance = Scenes.shop_weapon_selection.instantiate()
		instance.data = get_random_weapon()
		weapon_selection.add_child(instance)
```

## redo_selling
### Explanation
Clears the current weapon selling display and repopulates it with the weapons the player currently has. It does this by first freeing all existing children of the weapon_selling container, then instantiating new shop_weapon_selling scenes and setting their data to the weapons in Stats.current_weapons.
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
Returns a random weapon from the weapons_with_weights array. It does this by generating a random index within the bounds of the array and returning the weapon at that index.
### Code
```gdscript
func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]
```

## _on_button_pressed
### Explanation
Handles the button press event. It advances the game to the next level and changes the scene to the level1 scene.
### Code
```gdscript
func _on_button_pressed() -> void:
	Stats.next_level()
	
	get_tree().change_scene_to_packed(Scenes.level1)
```

## _on_reroll_button_pressed
### Explanation
Handles the reroll button press event. It checks if the player has enough coins to reroll, deducts the reroll cost from the player's coins, doubles the reroll cost, updates the reroll button's text to reflect the new cost, and calls redo_selection to refresh the weapon selection.
### Code
```gdscript
func _on_reroll_button_pressed() -> void:
	if Stats.coins < reroll_cost:
		return
	
	Stats.coins -= reroll_cost
	reroll_cost *= 2
	reroll_button.text = "Reroll\n(Cost: {0})".format([reroll_cost])
	
	redo_selection()
```

## reroll_enabled
### Explanation
Enables or disables the reroll button based on whether the player has enough coins to reroll. It does this by checking if the player's coins are less than the reroll cost and setting the disabled property of the reroll button accordingly.
### Code
```gdscript
func reroll_enabled() -> void:
	if Stats.coins < reroll_cost:
		reroll_button.disabled = true
	else:
		reroll_button.disabled = false
```
# Overall File Contents
```gdscript
extends Control

@export var weapons: Array[weapon]
var weapons_with_weights: Array[weapon]
@onready var weapon_selling: HBoxContainer = %WeaponSelling
@onready var weapon_selection: HBoxContainer = %WeaponSelection
@onready var reroll_button: Button = %RerollButton

var reroll_cost = 1

func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	Messanger.REDO_SELLING.connect(redo_selling)
	Messanger.WEAPON_CHANGE.connect(redo_selling)
	Messanger.REDO_SELECTION.connect(redo_selection)
	
	redo_selling()
	redo_selection()
	
	Messanger.MONEY_CHANGE.connect(reroll_enabled)
	reroll_enabled()

func redo_selection():
	for child in weapon_selection.get_children():
		child.queue_free()
	
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
	Stats.next_level()
	
	get_tree().change_scene_to_packed(Scenes.level1)

func _on_reroll_button_pressed() -> void:
	if Stats.coins < reroll_cost:
		return
	
	Stats.coins -= reroll_cost
	reroll_cost *= 2
	reroll_button.text = "Reroll\n(Cost: {0})".format([reroll_cost])
	
	redo_selection()

func reroll_enabled() -> void:
	if Stats.coins < reroll_cost:
		reroll_button.disabled = true
	else:
		reroll_button.disabled = false

```
