extends Node2D

func _ready():
	TotalTimer.timer_on = false

func _on_button_pressed() -> void:
	TotalTimer.timer_on = true
	get_tree().change_scene_to_file(Controller.new_scene)

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("next_dialog"):
		TotalTimer.timer_on = true
		get_tree().change_scene_to_file(Controller.new_scene)
