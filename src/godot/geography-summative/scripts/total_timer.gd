extends Node

var total_time = 0
var timer_on = false

func _process(delta: float) -> void:
	if timer_on:
		total_time += delta

func formated_version():
	var minutes = int(total_time / 60)
	var seconds = int(total_time) % 60
	if len(str(seconds)) == 2: return "Time: {0}:{1}".format([minutes, seconds])
	else: return "Time: {0}:0{1}".format([minutes, seconds])
