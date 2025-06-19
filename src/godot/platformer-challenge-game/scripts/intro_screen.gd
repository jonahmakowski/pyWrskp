extends Control

func _on_button_pressed() -> void:
	get_tree().change_scene_to_file("res://scenes/levels/level_1.tscn")

func _process(_delta: float):
	if Input.is_action_just_pressed("confirm"):
		get_tree().change_scene_to_file("res://scenes/levels/level_1.tscn")
