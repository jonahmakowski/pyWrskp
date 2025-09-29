@tool
extends Node

@export var all_upgrades: Array[upgrade]:
	set(value):
		all_upgrades = value
		all_upgrades.sort_custom(sort_by_rarity)
		if not Engine.is_editor_hint(): set_weights()
		notify_property_list_changed()

var upgrades_with_weights: Array[upgrade] = []

func _ready():
	if not Engine.is_editor_hint():
		set_weights()

func set_weights():
	upgrades_with_weights = []
	for u in all_upgrades:
		for i in range(u.weight):
			upgrades_with_weights.append(u)

func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	
	while not upgrades_with_weights[index].check_conditions():
		index = randi_range(0, len(upgrades_with_weights)-1)
	
	return upgrades_with_weights[index]

func sort_by_rarity(a: upgrade, b: upgrade):
	if a == null:
		return false
	elif b == null:
		return true
	
	if a.rarity > b.rarity:
		return true
	elif a.rarity == b.rarity:
		var abc_sort = [a.name, b.name]
		abc_sort.sort()
		if abc_sort[0] == a.name:
			return true
	
	return false
