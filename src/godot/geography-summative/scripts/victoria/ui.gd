extends Control

@onready var progress_display: Label = %ProgressDisplay
@onready var lives_display: Label = %LivesDisplay
@onready var time_left_display: Label = %TimeLeftDisplay

func _process(_delta: float) -> void:
	time_left_display.text = TotalTimer.formated_version()

func set_progress(precentage: String):
	progress_display.text = precentage

func set_lives(lives: String):
	lives_display.text = lives
