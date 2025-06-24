extends Node

var score = 0

@export var main_scene:PackedScene

func death():
	score = 0
	get_tree().change_scene_to_packed(main_scene)
