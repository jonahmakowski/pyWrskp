extends StaticBody2D

var in_bottom = false
var in_top = false
var top_body
var bottom_body

const move_distance = 100

func _on_bottom_area_2d_body_entered(body: Node2D) -> void:
	bottom_body = body
	in_bottom = true

func _on_bottom_area_2d_body_exited(body: Node2D) -> void:
	in_bottom = false

func _on_top_area_2d_body_entered(body: Node2D) -> void:
	top_body = body
	in_top = true

func _on_top_area_2d_body_exited(body: Node2D) -> void:
	in_top = false

func _process(_delta: float) -> void:
	if in_top and Input.is_action_just_pressed("interact"):
		top_body.position.y += move_distance
	if in_bottom and Input.is_action_just_pressed("interact"):
		bottom_body.position.y -= move_distance
