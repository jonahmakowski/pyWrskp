extends Control

@onready var score_display: Label = %"Score Display"

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	score_display.text = "Score: " + str(Controller.score)
