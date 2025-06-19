extends Node2D

const delta_per_char = 0.075
var current_delta_count = 0
var current_text_box = 1
var status = "Normal"

func _ready():
	TotalTimer.timer_on = false
	var data = load_data()
	
	if TotalTimer.total_time <= data['best']:
		status = "Winner"
		save(TotalTimer.total_time, 0)
	elif TotalTimer.total_time >= data['worst']:
		status = "Loser"
		save(0, TotalTimer.total_time)
	else:
		status = "Normal"

func _process(delta: float) -> void:
	if current_text_box == get_node('Text/' + status).get_child_count() + 1:
		return
	
	var text_box = get_node('Text/' + status + '/Text' + str(current_text_box))
	text_box.visible = true
	current_delta_count += delta
	
	if text_box.get_total_character_count() <= text_box.visible_characters:
		if Input.is_action_just_pressed("next_dialog"):
			if not (current_text_box == get_node('Text/' + status).get_child_count()): text_box.visible = false
			current_text_box += 1
		return
	
	if current_delta_count >= delta_per_char:
		text_box.visible_characters += 1
		current_delta_count = 0
	if Input.is_action_just_pressed("next_dialog"):
		text_box.visible_characters = text_box.get_total_character_count()

func save(best=0, worst=0):
	var data = load_data()
	
	if best == 0:
		best = data['best']
	if worst == 0:
		worst = data['worst']
	
	var save_file = FileAccess.open("user://savegame.save", FileAccess.WRITE)
	var save_data = {"best": best, "worst": worst}
	var json_string = JSON.stringify(save_data)
	save_file.store_line(json_string)

func load_data():
	if not FileAccess.file_exists("user://savegame.save"):
		return {"best": 999*999, "worst": 0}
	
	var save_file = FileAccess.open("user://savegame.save", FileAccess.READ)
	
	var string_as_file = save_file.get_as_text()
	
	return JSON.parse_string(string_as_file)
