extends Node2D


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Clock.time > 11:
		return
	$AnimatedSprite2D.frame = Clock.time
