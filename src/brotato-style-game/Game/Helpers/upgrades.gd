@tool
extends Node

@export var all_upgrades: Array[upgrade]:
	set(value):
		all_upgrades = value
		all_upgrades.sort_custom(sort_by_rarity)
		notify_property_list_changed()

var upgrades_with_weights = []

func _ready():
	upgrades_with_weights = []
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
			upgrades_with_weights.append(u)

func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]

func sort_by_rarity(a: upgrade, b: upgrade):
	if a != null and a.rarity > b.rarity:
		return true
	elif a != null and a.rarity == b.rarity:
		var abc_sort = [a.name, b.name]
		abc_sort.sort()
		if abc_sort[0] == a.name:
			return true
	return false
