extends Node2D

@export var health = 1
@onready var uuid = Controller.generate_uuid($".")

func _ready() -> void:
	if uuid not in Controller.hearts:
		Controller.hearts.append(uuid)
	if uuid in Controller.hearts_collected:
		queue_free()

func _on_area_2d_body_entered(_body: Node2D) -> void:
	if Controller.player_health != 20:
		Controller.player_health = 20 if health + Controller.player_health >= 20 else Controller.player_health + health
		Controller.hearts_collected.append(uuid)
		queue_free()
	else:
		$Label.visible = true

func _on_area_2d_body_exited(_body: Node2D) -> void:
	$Label.visible = false
