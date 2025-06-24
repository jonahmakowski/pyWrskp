extends Node2D

@onready var main_scene = $"../.."

const SEPERATION_MIN = 100
const SEPERATION_MAX = 150

const HEIGHT_RANGE = 150

const SPEED = 1

func hit_pipe():
	Controller.death()

func _ready() -> void:
	var seperation = randf_range(SEPERATION_MIN, SEPERATION_MAX)
	var height = randf_range(-HEIGHT_RANGE, HEIGHT_RANGE)
	$Upper.position.y = height - (seperation / 2)
	$Lower.position.y = height + (seperation / 2)

func _process(_delta: float) -> void:
	position.x -= 1

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	Controller.score += 1
	queue_free()

func init(x_pos):
	position.x = x_pos
