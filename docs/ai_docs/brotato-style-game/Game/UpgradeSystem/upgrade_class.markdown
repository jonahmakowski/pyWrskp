# Documentation for src/brotato-style-game/Game/UpgradeSystem/upgrade_class.gd

# AI Summary
This file defines an upgrade class in Godot. It includes properties for the upgrade's name, description, rarity, icon, and the changes to be made to stats. It also includes functions to check conditions and apply the upgrade.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some inconsistencies in naming conventions and some potential improvements in code organization.
# Functions

## check_conditions
### Explanation
This function checks if all conditions for an upgrade are met. It iterates through the conditions array and returns false if any condition is not met. Otherwise, it returns true.
### Code
```gdscript
func check_conditions():
	var result = true
	
	for condition in conditions:
		if not condition.check_condition():
			result = false
			break
	
	return result
```

## apply
### Explanation
This function applies the upgrade if all conditions are met. If any condition is not met, it issues a warning. It then iterates through the to_change array and applies the changes to the stats based on the type of change (either addition or multiplication).
### Code
```gdscript
func apply():
	if not check_conditions():
		push_warning("Applying upgrade even though one or more conditions are invalid")
	
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
@export var conditions: Array[upgrade_conditions]

func check_conditions():
	var result = true
	
	for condition in conditions:
		if not condition.check_condition():
			result = false
			break
	
	return result

func apply():
	if not check_conditions():
		push_warning("Applying upgrade even though one or more conditions are invalid")
	
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_by'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_by'])

```
