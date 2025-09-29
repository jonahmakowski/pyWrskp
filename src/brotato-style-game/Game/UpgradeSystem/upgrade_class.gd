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
