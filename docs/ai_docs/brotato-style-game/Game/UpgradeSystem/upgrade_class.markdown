# Documentation for src/brotato-style-game/Game/UpgradeSystem/upgrade_class.gd

# AI Summary
This file defines a class called 'upgrade' that extends the 'Resource' class. It includes properties for the upgrade's name, description, rarity, icon, and an array of stat changes. The 'apply' function applies these stat changes to the player's stats. The rarity property is set using a setter method that also updates the weight and rarity text based on predefined mappings in the Stats object.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, with clear variable names and a logical flow. However, there is a typo in the 'desription' variable name, and the 'change_value' key in the 'to_change' array format comment should be 'change_by' to match the actual code.
# Functions

## apply
### Explanation
This function applies the changes specified in the 'to_change' array to the player's stats. It iterates over each stat change in the array and updates the corresponding stat in the Stats object. If the change type is '+', it adds the change value to the current stat value. If the change type is '*', it multiplies the current stat value by the change value.
### Code
```gdscript
func apply():
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_by'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_by'])
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
		weight = Stats.RARITY_TO_WEIGHT[rarity]
		rarity_text = Stats.RARITY_TO_TEXT[rarity]

var weight: int
var rarity_text: String

@export var has_icon: bool
@export var icon: Texture2D

# to_change: In format of:
# {"stat": String, "change_value": int, "type": String}
# type = "*" or "+"

@export var to_change: Array[stat_changes]

func apply():
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_by'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_by'])

```
