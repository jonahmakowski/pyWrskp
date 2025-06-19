extends Node2D

@export var button_color_id = ""

func _ready() -> void:
	$AnimatedSprite2D.animation = "unpressed_" + button_color_id.to_lower()
	if len($Area2D.get_overlapping_bodies()) > 0:
		$AnimatedSprite2D.animation = "pressed_" + button_color_id.to_lower()
		Controller.buttons_pressed[button_color_id.to_lower()] = true

func _process(delta: float) -> void:
	if len($Area2D.get_overlapping_bodies()) > 0:
		$AnimatedSprite2D.animation = "pressed_" + button_color_id.to_lower()
		Controller.buttons_pressed[button_color_id.to_lower()] = true

func _on_area_2d_body_exited(body: Node2D) -> void:
	if len($Area2D.get_overlapping_bodies()) == 0:
		$AnimatedSprite2D.animation = "unpressed_" + button_color_id.to_lower()
		Controller.buttons_pressed[button_color_id.to_lower()] = false
