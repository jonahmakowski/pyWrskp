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
