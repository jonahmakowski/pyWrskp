extends Timer
var time = 0
var time_type = 0
var times = {0: 120, 1: 30, 2: 120, 3: 30, 4: 120, 5: 120, 6: 30, 7: 120, 8: 30, 9: 120, 10: 180, 11: 180, 12: 120, 13: 180, 14: 180, 15: 120}


func _on_timeout() -> void:
	print(":3")
	time += 1
	if time == 16:
		time = 0
	
	wait_time = times[time]
		
	start()
