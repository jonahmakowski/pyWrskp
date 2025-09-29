# Documentation for src/brotato-style-game/Game/Helpers/upgrades.gd

# AI Summary
This Godot Node script, `upgrades.gd`, is designed to manage and provide a weighted random selection of game upgrades. It automatically sorts a list of `upgrade` objects by rarity and then by name. Based on each upgrade's `weight` property, it creates an internal list from which a random upgrade can be efficiently retrieved. This setup is particularly useful for game systems requiring weighted probabilities for item drops or selection.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally clear, functional, and addresses a common game development need for weighted random selection. The structure is logical, and the use of a dedicated setter for sorting and weight calculation is a good practice. However, the custom sorting function could be slightly more concise in its logic, especially in the secondary alphabetical sort. Also, while `upgrade` is a custom type, it's used with a lowercase hint, which is typically reserved for built-in types; custom types usually follow PascalCase.
# Functions

## all_upgrades setter
### Explanation
This is a setter for the `all_upgrades` array. When `all_upgrades` is assigned a value, it sorts the array using the `sort_by_rarity` custom function. If the engine is not in editor hint mode (i.e., running the game), it calls `set_weights()` to update the weighted list of upgrades. Otherwise, it notifies the editor that the property list has changed.
### Code
```gdscript
set(value):
	all_upgrades = value
	all_upgrades.sort_custom(sort_by_rarity)
	if not Engine.is_editor_hint(): set_weights()
	else: notify_property_list_changed()
```

## _ready
### Explanation
This is a built-in Godot engine callback function that is automatically called when the node enters the scene tree for the first time. It checks if the engine is running in an editor hint mode. If not, it calls `set_weights()` to initialize the weighted list of upgrades.
### Code
```gdscript
func _ready():
	if not Engine.is_editor_hint():
		set_weights()
```

## set_weights
### Explanation
This function populates the `upgrades_with_weights` array. It iterates through each `upgrade` in the `all_upgrades` array. For each upgrade, it adds the upgrade to `upgrades_with_weights` a number of times equivalent to its `weight` property. This creates a list where upgrades with higher weights appear more frequently, facilitating weighted random selection.
### Code
```gdscript
func set_weights():
	upgrades_with_weights = []
	for u in all_upgrades:
		for i in range(u.weight):
			upgrades_with_weights.append(u)
```

## get_random_upgrade
### Explanation
This function returns a single random upgrade from the `upgrades_with_weights` array. It calculates a random index within the bounds of this array using `randi_range` and then retrieves the upgrade at that specific index. Due to the way `upgrades_with_weights` is populated, this effectively provides a randomly weighted upgrade.
### Code
```gdscript
func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]
```

## sort_by_rarity
### Explanation
This is a custom comparison function used to sort `upgrade` objects. It first compares two upgrades based on their `rarity` property; an upgrade with a higher rarity is considered "greater". If the rarities are equal, it then compares their `name` properties alphabetically to ensure a consistent secondary sorting order.
### Code
```gdscript
func sort_by_rarity(a: upgrade, b: upgrade):
	if a != null and a.rarity > b.rarity:
		return true
	elif a != null and a.rarity == b.rarity:
		var abc_sort = [a.name, b.name]
		abc_sort.sort()
		if abc_sort[0] == a.name:
			return true
	return false
```
# Overall File Contents
```gdscript
@tool
extends Node

@export var all_upgrades: Array[upgrade]:
	set(value):
		all_upgrades = value
		all_upgrades.sort_custom(sort_by_rarity)
		if not Engine.is_editor_hint(): set_weights()
		else: notify_property_list_changed()

var upgrades_with_weights = []

func _ready():
	if not Engine.is_editor_hint():
		set_weights()

func set_weights():
	upgrades_with_weights = []
	for u in all_upgrades:
		for i in range(u.weight):
			upgrades_with_weights.append(u)

func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]

func sort_by_rarity(a: upgrade, b: upgrade):
	if a != null and a.rarity > b.rarity:
		return true
	elif a != null and a.rarity == b.rarity:
		var abc_sort = [a.name, b.name]
		abc_sort.sort()
		if abc_sort[0] == a.name:
			return true
	return false

```
