extends Node2D

const rocks = 4
@onready var time_label: Label = %"Time Label"
@onready var total_time: Label = %TotalTime
@export var rock_scene:PackedScene
@export var next_level:PackedScene
var active_rocks = 0

func _ready():
	TotalTimer.timer_on = true


func _process(_delta: float) -> void:
	var seconds = str(int(int($Timer.time_left) % 60)) if int(int($Timer.time_left) % 60) >= 10 else "0" + str(int(int($Timer.time_left) % 60))
	time_label.text = "Time Left: {0}:{1}".format([int($Timer.time_left / 60), seconds])
	active_rocks = len($Area2D.get_overlapping_bodies())
	total_time.text = TotalTimer.formated_version()

func new_rock():
	if active_rocks < rocks:
		var rock := rock_scene.instantiate()
		active_rocks += 1
		if active_rocks < rocks:
			new_rock()
		$Rocks.call_deferred("add_child", rock)

func _on_area_2d_body_exited(_body: Node2D) -> void:
	active_rocks -= 1

func _on_timer_timeout() -> void:
	get_tree().change_scene_to_packed(next_level)

func _on_new_rocks_timeout() -> void:
	new_rock()
