extends StaticBody2D

@onready var skiier: CharacterBody2D = $"../../Skiier"

func _on_area_2d_body_entered(_body: Node2D) -> void:
	skiier.flags += 1
	queue_free()

func init(p_location, p_type="Random", clipping=false):
	position = p_location
