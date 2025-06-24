extends Node

@export var pipe:PackedScene

func _ready() -> void:
	$Area2D.position.x = (get_window().size.x / 2) * 1.1
	make_new_pipe((get_window().size.x / 2) * 1.5)

func make_new_pipe(x_pos):
	var instance = pipe.instantiate()
	instance.init(x_pos)
	%Pipes.add_child(instance)

func _on_area_2d_area_exited(_area: Area2D) -> void:
	print_debug("New Pipe Summoned")
	make_new_pipe((get_window().size.x / 2) * 1.5)
