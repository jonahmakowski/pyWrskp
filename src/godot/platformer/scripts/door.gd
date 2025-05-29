extends Node2D
@export var destination = ""
@export var destinationpos = Vector2()
var touchingPlayer
var player

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = true
		player = body

func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = false

func _process(delta: float) -> void:
	if Input.is_action_just_pressed('interact') and touchingPlayer:
		get_tree().change_scene_to_file(destination)
		player.position = destination
		
