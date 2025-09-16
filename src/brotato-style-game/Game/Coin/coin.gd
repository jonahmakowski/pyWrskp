extends Node2D

var value = 1

func init(v):
	value = v

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Stats.coins += value
	queue_free()
