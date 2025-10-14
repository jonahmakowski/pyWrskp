extends Node3D
class_name Weapon

@onready var parent: Player = get_parent()
@onready var timer: Timer = %Timer

## The projectile this weapon should shoot
@export var projectile: PackedScene

## The cooldown between each firing in seconds
@export var firerate: int

var can_shoot = true

func _ready() -> void:
	timer.timeout.connect(reset_can_shoot)

func _process(_delta: float) -> void:
	if Input.is_action_pressed("shoot") and (can_shoot and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED):
		parent.fire_shot(projectile, parent.pivot_angle)
		timer.start(firerate)
		can_shoot = false
		get_viewport().set_input_as_handled()

func reset_can_shoot():
	can_shoot = true
