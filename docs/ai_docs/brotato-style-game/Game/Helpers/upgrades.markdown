# Documentation for src/brotato-style-game/Game/Helpers/upgrades.gd

# AI Summary
This file defines a Node class that manages a list of upgrades. The _ready function initializes the upgrades_with_weights array, and the get_random_upgrade function returns a random upgrade from this array.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, the variable names could be more descriptive, and there is no error handling in the get_random_upgrade function.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It initializes the upgrades_with_weights array by iterating over all_upgrades and adding each upgrade to the array according to its weight.
### Code
```gdscript
func _ready():
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
			upgrades_with_weights.append(u)
```

## get_random_upgrade
### Explanation
This function returns a random upgrade from the upgrades_with_weights array. It uses the randi_range function to generate a random index within the bounds of the array.
### Code
```gdscript
func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]
```
# Overall File Contents
```gdscript
extends Node

@export var slightly_faster_spin: upgrade
@onready var all_upgrades = [slightly_faster_spin]
var upgrades_with_weights = []

func _ready():
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
			upgrades_with_weights.append(u)

func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]

```
