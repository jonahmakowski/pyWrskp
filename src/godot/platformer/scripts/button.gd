extends Node2D

func _on_area_2d_body_entered(body: Node2D) -> void:
	$AnimatedSprite2D.animation = "pressed"

func _on_area_2d_body_exited(body: Node2D) -> void:
	$AnimatedSprite2D.animation = "unpressed"
