extends Node2D

@onready var uuid = Controller.generate_uuid($".")

func _ready() -> void:
	if uuid not in Controller.coins:
		Controller.coins.append(uuid)
	if uuid in Controller.coins_collected:
		queue_free()

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Controller.coins_collected.append(uuid)
	queue_free()
