extends Node2D

@export var to_scene = ""
@export var move = false
@export var location = Vector2()

var touching_player = false

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("interact") and touching_player:
		$Interact.visible = false
		$Wait.visible = true
		$Timer.start()
		$ColorIcon.visible = true

func _on_timer_timeout() -> void:
	if move:
		Controller.current_respawn = location
		Controller.send_to_respawn = true
	Controller.finish_level()
	get_tree().change_scene_to_file(to_scene)

func _on_area_2d_body_entered(body: Node2D) -> void:
	$Interact.visible = true
	touching_player = true

func _on_area_2d_body_exited(body: Node2D) -> void:
	touching_player = false
	$Wait.visible = false
	$Interact.visible = false
	$Timer.stop()
	$ColorIcon.visible = false
