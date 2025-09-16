extends Node

@export var slightly_faster_spin: upgrade
@onready var all_upgrades = [slightly_faster_spin]
var upgrades_with_weights = []

func _ready():
	for u in all_upgrades:
		var weight = u.weight
		for i in range(weight):
			upgrades_with_weights.append(u)

func get_random_upgrade() -> upgrade:
	var index = randi_range(0, len(upgrades_with_weights)-1)
	return upgrades_with_weights[index]
