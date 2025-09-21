# Documentation for src/brotato-style-game/Game/Helpers/upgrades.gd

# AI Summary
This GDScript file defines a Godot Node (`upgrades.gd`) designed to manage a collection of game upgrades. It allows developers to define upgrades with custom weights and rarities. The script provides functionality to sort these upgrades based on rarity and name, and to generate a weighted list for random selection. This is a common pattern for implementing loot tables or upgrade systems in games.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is clear, functional, and uses type hints. The custom setter for `all_upgrades` ensures the list is always sorted, which is good practice. However, the `sort_by_rarity` function could be slightly more concise, especially in its alphabetical sorting logic, and the explicit `null` checks might be redundant if the array is guaranteed to contain valid objects. The `upgrades_with_weights` array is rebuilt in `_ready()` and also implicitly when `all_upgrades` is set; consolidating this logic into a dedicated private function could improve maintainability.
# Functions

## _ready
### Explanation
This function initializes the `upgrades_with_weights` array by iterating through `all_upgrades` and adding each upgrade `u.weight` times. This creates a list where upgrades appear proportionally to their weight, facilitating weighted random selection.
### Code
```gdscript
func _ready():
	upgrades_with_weights = []
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
			upgrades_with_weights.append(u)
```

## get_random_upgrade
### Explanation
This function returns a randomly selected upgrade from the `upgrades_with_weights` array. The selection is weighted because `upgrades_with_weights` contains duplicates based on each upgrade's weight.
### Code
```gdscript
func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]
```

## sort_by_rarity
### Explanation
This custom sort function is used to sort `upgrade` objects. It primarily sorts by `rarity` in descending order (higher rarity first). If rarities are equal, it then sorts alphabetically by `name` in ascending order.
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
		notify_property_list_changed()

var upgrades_with_weights = []

func _ready():
	upgrades_with_weights = []
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
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
