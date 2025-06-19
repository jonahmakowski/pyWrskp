extends Control

@onready var label: Label = %Label
@onready var time_left: Label = %TimeLeft

func set_text(text):
	label.text = text

func _process(_delta: float) -> void:
	time_left.text = TotalTimer.formated_version()
