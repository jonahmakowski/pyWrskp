extends Node2D
@export var destination = ""
@export var destinationpos = Vector2()
@export var requires_key = false
@export var key_uuid = ""

var touchingPlayer
var player

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = true
		player = body
		if Controller.is_key_collected(key_uuid) or not requires_key:
			$key.visible = true

func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = false
	$nokey.visible = false
	$key.visible = false

func _process(delta: float) -> void:
	if touchingPlayer:
		if not (!requires_key or Controller.is_key_collected(key_uuid)):
			$nokey.visible = true
		elif Input.is_action_just_pressed('interact') and touchingPlayer:
			$"/root/Controller".change_scene(destinationpos, destination)
	if requires_key:
		if Controller.is_key_collected(key_uuid):
			$unlocked.visible = true
			$locked.visible = false
		else:
			$unlocked.visible = false
			$locked.visible = true
