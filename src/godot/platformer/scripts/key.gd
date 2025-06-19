extends Node2D

@export var uuid: String = ""
@export var key_color_id = ""

func _ready():
	if Controller.is_key_collected(uuid):
		queue_free()  # Already collected
	$AnimatedSprite2D.animation = "key_" + key_color_id.to_lower()
	

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group('player'):
		Controller.mark_key_collected(uuid)
		queue_free()
