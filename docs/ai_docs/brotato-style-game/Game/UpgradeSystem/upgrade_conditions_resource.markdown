# Documentation for src/brotato-style-game/Game/UpgradeSystem/upgrade_conditions_resource.gd

# AI Summary
This file defines a resource class `upgrade_conditions` that extends the `Resource` class. It includes variables for a stat, a type of condition, an opposite flag, and a value. The main function `check_condition` checks if a condition is met based on the current value of the stat and the specified type and value.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there is a small issue with the condition type string "Greater Tian or Equal To" which should be "Greater Than or Equal To". The code follows most conventions well, but the small error slightly reduces the rating.
# Functions

## check_condition
### Explanation
This function checks if a condition is met based on the current value of a stat. It uses the `Stats.get` method to retrieve the current value of the stat. If the stat does not exist, it pushes an error message and returns false. Depending on the `type` and `opposite` variables, it checks if the current value meets the condition (greater than, less than, equal to, etc.) and returns true if the condition is met, otherwise it returns false.
### Code
```gdscript
func check_condition():
	var current_value = Stats.get(stat)
	
	if current_value == null:
		push_error("Stat '{0}' does not exist.".format([stat]))
		return false
	
	if not opposite:
		if type == "Greater Than" and value > current_value:
			return true
		elif type == "Less Than" and value < current_value:
			return true
		elif type == "Equal To" and value == current_value:
			return true
		elif type == "Greater Than or Equal To" and value >= current_value:
			return true
		elif type == "Less Than or Equal To" and value <= current_value:
			return true
	else:
		if type == "Greater Than" and not value > current_value:
			return true
		elif type == "Less Than" and not value < current_value:
			return true
		elif type == "Equal To" and not value == current_value:
			return true
		elif type == "Greater Than or Equal To" and not value >= current_value:
			return true
		elif type == "Less Than or Equal To" and not value <= current_value:
			return true
	
	return false
```
# Overall File Contents
```gdscript
extends Resource
class_name upgrade_conditions

@export var stat: String
@export_enum("Greater Than", "Less Than", "Equal To", "Greater Than or Equal To", "Less Than or Equal To") var type: String
@export var opposite: bool
@export var value: float

func check_condition():
	var current_value = Stats.get(stat)
	
	if current_value == null:
		push_error("Stat '{0}' does not exist.".format([stat]))
		return false
	
	if not opposite:
		if type == "Greater Than" and value > current_value:
			return true
		elif type == "Less Than" and value < current_value:
			return true
		elif type == "Equal To" and value == current_value:
			return true
		elif type == "Greater Than or Equal To" and value >= current_value:
			return true
		elif type == "Less Than or Equal To" and value <= current_value:
			return true
	else:
		if type == "Greater Than" and not value > current_value:
			return true
		elif type == "Less Than" and not value < current_value:
			return true
		elif type == "Equal To" and not value == current_value:
			return true
		elif type == "Greater Than or Equal To" and not value >= current_value:
			return true
		elif type == "Less Than or Equal To" and not value <= current_value:
			return true
	
	return false

```
