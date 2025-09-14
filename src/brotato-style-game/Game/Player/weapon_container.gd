@tool
extends Node2D

@export var animate_in_editor: bool = false:
	set(value):
		current_angle = 0
		arrange_children_in_circle(current_angle)
		animate_in_editor = value

@export var rotation_speed: float = 2.0

@export var radius: float = 50.0:
	set(value):
		radius = value
		var angle_to_use = current_angle if current_angle != null else 0.0
		if is_inside_tree():
			arrange_children_in_circle(angle_to_use)

var current_angle: float

func _ready() -> void:
	current_angle = 0.0
	arrange_children_in_circle(current_angle)

func _process(delta: float) -> void:
	if not Engine.is_editor_hint() or animate_in_editor:
		if current_angle == null:
			current_angle = 0.0
		current_angle += rotation_speed * delta
		current_angle = fmod(current_angle, TAU)
		arrange_children_in_circle(current_angle)

func arrange_children_in_circle(base_angle: float) -> void:
	if not is_inside_tree():
		return
	var children = get_children().filter(func(c): return c is Node2D)
	if children.is_empty():
		return
	var angle_step = TAU / children.size()
	for i in range(children.size()):
		var angle = base_angle + (i * angle_step)
		var x = radius * cos(angle)
		var y = radius * sin(angle)
		children[i].position = Vector2(x, y)
