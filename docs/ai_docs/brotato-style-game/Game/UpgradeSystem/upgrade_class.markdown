# Documentation for src/brotato-style-game/Game/UpgradeSystem/upgrade_class.gd

# AI Summary
This file defines a class named `upgrade` that extends the `Resource` class. It includes properties for the upgrade's name, description, rarity, icon, and a list of stats to change. The `apply` function modifies the stats based on the upgrades specified.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some inconsistencies in naming conventions and comments.
# Functions

## apply
### Explanation
This function applies the upgrades specified in the `to_change` array. It iterates over each upgrade and modifies the corresponding stat in the `Stats` object based on the upgrade type (addition or multiplication).
### Code
```gdscript
func apply():
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_value'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_value'])
```
# Overall File Contents
```gdscript
class_name upgrade
extends Resource

@export var name: String
@export var desription: String
@export var rarity: int:
	set(value):
		rarity = value
		weight = rarity_to_weight[rarity]
		rarity_text = rarity_to_text[rarity]

var weight: int
var rarity_text: String

@export var has_icon: bool
@export var icon: Texture2D

# to_change: In format of:
# {"stat": String, "change_value": int, "type": String}
# type = "*" or "+"

@export var to_change: Array[Dictionary]

const rarity_to_weight = {1: 20}
const rarity_to_text = {1: "Common"}

func apply():
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_value'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_value'])

```
