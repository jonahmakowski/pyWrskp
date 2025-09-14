extends Control

func _on_start_pressed() -> void:
	Stats.reset()
	get_tree().change_scene_to_packed(Scenes.level1)
