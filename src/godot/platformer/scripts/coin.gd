extends Node2D

@export var uuid: String = ""

func _ready():
	if Controller.is_coin_collected(uuid):
		queue_free()

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group('player'):
		Controller.coins += 1
		Controller.mark_coin_collected(uuid)
		queue_free()
