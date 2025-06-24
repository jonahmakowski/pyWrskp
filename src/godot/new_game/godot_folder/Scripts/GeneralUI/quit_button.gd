extends Button

@onready var button_click: AudioStreamPlayer = %ButtonClick

func _on_pressed() -> void:
	button_click.play()
	await get_tree().process_frame
	while button_click.playing:
		await get_tree().process_frame
		get_tree().quit()
