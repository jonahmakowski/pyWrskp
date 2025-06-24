extends Button

@onready var button_click: AudioStreamPlayer = %ButtonClick

func _on_pressed() -> void:
	button_click.play()
	print('Open Settings')
