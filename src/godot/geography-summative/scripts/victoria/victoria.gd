extends Node2D

@export var arrow_scene: PackedScene
@export var next_scene: PackedScene
@export var lives_max = 0

@onready var lives = lives_max

const chart_path = "res://scripts/victoria/victoria_data.json"
var x_options = {"up": 274.5, "down": 109.5, "left": 12.5, "right": 370.5}
var chart_data
var total_expected_arrows = 0

func load_chart(path: String) -> Array:
	var file := FileAccess.open(path, FileAccess.READ)
	if file:
		var json_text := file.get_as_text()
		var json_result = JSON.parse_string(json_text)
		if typeof(json_result) == TYPE_ARRAY:
			return json_result
		else:
			push_error("Failed to parse JSON: Not an array")
	else:
		push_error("Failed to open file: %s" % path)
	return []

func _ready():
	TotalTimer.timer_on = true
	chart_data = load_chart(chart_path)
	var current_y = -30
	for item in chart_data:
		if item['up']:
			spawn_arrow('up', current_y)
		if item['down']:
			spawn_arrow('down', current_y)
		if item['left']:
			spawn_arrow('left', current_y)
		if item['right']:
			spawn_arrow('right', current_y)
		current_y -= 50

func spawn_arrow(direction: String, y: float):
	var instance = arrow_scene.instantiate()
	instance.init(Vector2(x_options[direction], y), direction)
	$Arrows.add_child(instance)
	total_expected_arrows += 1

func _process(_delta: float) -> void:
	var cleared_arrows = total_expected_arrows - $Arrows.get_child_count()
	var percentage = float((float(cleared_arrows) / total_expected_arrows) * 100)
	$UI.set_progress("Progress: " + str(int(percentage)) + "%")
	
	if $Arrows.get_child_count() == 0:
		get_tree().change_scene_to_packed(next_scene)
		return
	
	for arrow in $ButtonPressArea.get_overlapping_bodies():
		if Input.is_action_just_pressed("rhythm_down") and arrow.type == 'down':
			arrow.queue_free()
		if Input.is_action_just_pressed("rhythm_up") and arrow.type == 'up':
			arrow.queue_free()
		if Input.is_action_just_pressed("rhythm_right") and arrow.type == 'right':
			arrow.queue_free()
		if Input.is_action_just_pressed("rhythm_left") and arrow.type == 'left':
			arrow.queue_free()
	
	$UI.set_lives("Lives: {0}/{1}".format([lives, lives_max]))
	
	if lives <= 0:
		get_tree().reload_current_scene()

func _on_area_2d_body_entered(body: Node2D) -> void:
	$AnimatedSprite2D.animation = "hurt"
	lives -= 1
	body.queue_free()

func _on_animated_sprite_2d_animation_looped() -> void:
	$AnimatedSprite2D.animation = "default"
