extends Control

func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("pause"):
		if get_tree().paused == false:
			get_tree().paused = true
			show()
		else:
			get_tree().paused = false
			hide()

func _on_restart_button_pressed() -> void:
	get_tree().paused = false
	Controller.kill_player()

func _on_resume_button_pressed() -> void:
	get_tree().paused = false
	hide()
