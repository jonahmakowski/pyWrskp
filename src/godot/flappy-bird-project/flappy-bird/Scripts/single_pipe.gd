extends Node2D

@export var master:Node

func _on_area_2d_body_entered(_body: Node2D) -> void:
	master.hit_pipe()
