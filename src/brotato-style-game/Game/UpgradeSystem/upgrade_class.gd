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
