extends Control

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("pause"):
		if get_tree().paused == false:
			TotalTimer.timer_on = false
			get_tree().paused = true
			show()
		else:
			TotalTimer.timer_on = true
			get_tree().paused = false
			hide()

func _on_resume_button_pressed() -> void:
	TotalTimer.timer_on = true
	get_tree().paused = false
	hide()

func _on_restart_button_pressed() -> void:
	TotalTimer.timer_on = true
	get_tree().paused = false
	get_tree().change_scene_to_file(get_tree().current_scene.scene_file_path)
