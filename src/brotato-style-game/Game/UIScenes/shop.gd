extends Control

@export var weapons: Array[weapon]
var weapons_with_weights: Array[weapon]

func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)

func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]

func _process(delta: float) -> void:
	pass
