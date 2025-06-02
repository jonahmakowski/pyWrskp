extends Node2D

@export var uuid: String = ""

func _ready():
	if Controller.is_key_collected(uuid):
		queue_free()  # Already collected

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group('player'):
		Controller.mark_key_collected(uuid)
		queue_free()
