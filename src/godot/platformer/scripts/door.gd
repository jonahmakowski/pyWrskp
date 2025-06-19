extends Node2D
@export var destination = ""
@export var destinationpos = Vector2()
@export var requires_key = false
@export var key_uuid = ""
@export var requires_time = false
@export var time_required = []

var touchingPlayer
var player

func _ready() -> void:
	if requires_key and Controller.is_key_collected(key_uuid):
		$locked.visible = true
	elif requires_time and Clock.time in time_required:
		$locked.visible = true
	else:
		$locked.visible = false

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = true
		player = body
		if requires_key and !Controller.is_key_collected(key_uuid):
			$nokey.visible = true
		elif requires_time and !Clock.time in time_required:
			$badtime.visible = true
		else:
			$key.visible = true

func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.name == "Character":
		touchingPlayer = false
	$nokey.visible = false
	$key.visible = false
	$badtime.visible = false

func _process(delta: float) -> void:
	if touchingPlayer:
		if requires_key and !Controller.is_key_collected(key_uuid):
			$nokey.visible = true
		elif requires_time and !Clock.time in time_required:
			$badtime.visible = true
		elif Input.is_action_just_pressed('interact') and touchingPlayer:
			$"/root/Controller".change_scene(destinationpos, destination)
	if requires_key:
		$locked.visible = false if Controller.is_key_collected(key_uuid) else true
	if requires_time:
		$locked.visible = false if Clock.time in time_required else true
