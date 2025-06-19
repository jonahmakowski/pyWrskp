extends Node2D

const delta_per_char = 0.075
@export var next_scene:PackedScene
@export var num_of_text = 7
var current_delta_count = 0
var current_text_box = 1

func _ready():
	TotalTimer.timer_on = false

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if current_text_box == num_of_text + 1:
		get_tree().change_scene_to_packed(next_scene)
		return
	
	var text_box = get_node('Text/Text' + str(current_text_box))
	text_box.visible = true
	current_delta_count += delta
	
	if text_box.get_total_character_count() <= text_box.visible_characters:
		if Input.is_action_just_pressed("next_dialog"):
			text_box.visible = false
			current_text_box += 1
		return
	
	if current_delta_count >= delta_per_char:
		text_box.visible_characters += 1
		current_delta_count = 0
	if Input.is_action_just_pressed("next_dialog"):
		text_box.visible_characters = text_box.get_total_character_count()
