# Documentation for src/brotato-style-game/Game/UpgradeSystem/upgrade_class.gd

# AI Summary
This GDScript file defines an `upgrade` resource class, which is used to represent various upgrades in a game. It includes properties for the upgrade's name, description, rarity, visual icon, and a list of stat changes it applies. The rarity setter automatically calculates a `weight` and `rarity_text` based on predefined constants. The `apply` function, the core logic, modifies player statistics (accessed via a global `Stats` object) by either adding or multiplying values based on the upgrade's `to_change` array. While the class effectively encapsulates upgrade data and logic, there is a minor misspelling (`desription`) and a discrepancy between a comment and actual variable name (`change_value` vs `change_by`). The `stat_changes` type and `Stats` global are assumed to be defined elsewhere.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, using an `extends Resource` pattern for data. The use of a setter for `rarity` is a good practice for maintaining data consistency. However, there's a typo in a variable name (`desription`), a mismatch between a comment and variable name (`change_value` vs `change_by`), and the reliance on an undefined `stat_changes` type and a global `Stats` object within this file. The class name `upgrade` is lowercase, which is less conventional for class names in GDScript (usually PascalCase).
# Functions

## apply
### Explanation
This function iterates through the `to_change` array, which specifies statistical modifications. For each stat change, it checks the `type` property. If `type` is "+", it adds the `change_by` value to the current stat value. If `type` is "*", it multiplies the current stat value by `change_by`. It uses a global `Stats` object to get and set player statistics.
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
		weight = rarity_to_weight[rarity]
		rarity_text = rarity_to_text[rarity]

var weight: int
var rarity_text: String

@export var has_icon: bool
@export var icon: Texture2D

# to_change: In format of:
# {"stat": String, "change_value": int, "type": String}
# type = "*" or "+"

@export var to_change: Array[stat_changes]

const rarity_to_weight = {1: 20}
const rarity_to_text = {1: "Common"}

func apply():
	for stat in to_change:
		if stat['type'] == "+":
			Stats.set(stat['stat'], Stats.get(stat['stat']) + stat['change_by'])
		elif stat['type'] == "*":
			Stats.set(stat['stat'], Stats.get(stat['stat']) * stat['change_by'])

```
