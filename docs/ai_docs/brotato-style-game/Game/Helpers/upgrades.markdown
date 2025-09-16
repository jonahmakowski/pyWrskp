# Documentation for src/brotato-style-game/Game/Helpers/upgrades.gd

# AI Summary
This file defines a Node class that manages upgrades. It initializes an array of upgrades and populates another array with weighted upgrades. It also provides a function to get a random upgrade from the weighted array.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and follows conventions, but there is room for improvement in terms of conciseness and functionality.
# Functions

## _ready
### Explanation
This function initializes the upgrades_with_weights array by iterating over all_upgrades and appending each upgrade according to its weight.
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
This function returns a random upgrade from the upgrades_with_weights array.
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
@export var deal_slightly_more_damage: upgrade

@onready var all_upgrades = [slightly_faster_spin, deal_slightly_more_damage]
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
