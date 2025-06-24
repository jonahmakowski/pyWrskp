extends Label

func _ready():
	TotalTimer.timer_on = true

func _process(_delta: float):
	text = TotalTimer.formated_version()
