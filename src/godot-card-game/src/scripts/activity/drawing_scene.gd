extends Control

@onready var location = get_viewport().get_mouse_position()

func _ready() -> void:
	pass

func _process(delta: float) -> void:
	if get_viewport_rect().has_point(get_viewport().get_mouse_position()):
		location = get_viewport().get_mouse_position()
		
		if Input.is_action_pressed("draw"):
			var instance = TextureRect.new()
			instance.texture = load("res://assets/activity/black_circle.svg")
			instance.pivot_offset = instance.size / 2
			instance.scale = Vector2(0.25, 0.25)
			add_child(instance)
			instance.position = location - ((instance.size/2) * instance.scale)
