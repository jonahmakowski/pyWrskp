# Documentation for src/brotato-style-game/Game/Helpers/upgrades.gd

# AI Summary
This file defines a Node class that manages a list of upgrades. It includes functionality to set the weights of the upgrades, get a random upgrade, and sort the upgrades by rarity. The upgrades are stored in an array, and each upgrade has a weight and rarity. The weights are used to determine the probability of an upgrade being selected, and the rarity is used to sort the upgrades.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where the code could be more concise or follow conventions more closely. For example, the `sort_by_rarity` function could be simplified, and the `get_random_upgrade` function could be made more efficient by avoiding the repeated generation of random indices.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It sets the weights of the upgrades if the engine is not in editor hint mode.
### Code
```gdscript
func _ready():
	if not Engine.is_editor_hint():
		set_weights()
```

## set_weights
### Explanation
This function sets the weights of the upgrades. It creates a new array of upgrades where each upgrade is repeated according to its weight.
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
This function returns a random upgrade from the array of upgrades with weights. It continues to generate a random index until it finds one where the upgrade's conditions are met.
### Code
```gdscript
func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	
	while not upgrades_with_weights[index].check_conditions():
		index = randi_range(0, len(upgrades_with_weights)-1)
	
	return upgrades_with_weights[index]
```

## sort_by_rarity
### Explanation
This function is used to sort the upgrades by rarity. If two upgrades have the same rarity, they are sorted alphabetically by name.
### Code
```gdscript
func sort_by_rarity(a: upgrade, b: upgrade):
	if a == null:
		return false
	elif b == null:
		return true
	
	if a.rarity > b.rarity:
		return true
	elif a.rarity == b.rarity:
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
		notify_property_list_changed()

var upgrades_with_weights: Array[upgrade] = []

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
	
	while not upgrades_with_weights[index].check_conditions():
		index = randi_range(0, len(upgrades_with_weights)-1)
	
	return upgrades_with_weights[index]

func sort_by_rarity(a: upgrade, b: upgrade):
	if a == null:
		return false
	elif b == null:
		return true
	
	if a.rarity > b.rarity:
		return true
	elif a.rarity == b.rarity:
		var abc_sort = [a.name, b.name]
		abc_sort.sort()
		if abc_sort[0] == a.name:
			return true
	
	return false

```
