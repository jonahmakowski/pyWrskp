extends CharacterBody2D

@onready var sprite: AnimatedSprite2D = $Sprite

@export var color = ""

@onready var idle_animation = color + "_idle"
@onready var run_animation = color + "_run"
@onready var shoot_animation = color + "_shoot"

func init(c):
	color = c

func _ready() -> void:
	if color not in ['red', 'blue', 'black', 'yellow']:
		push_error("Invalid Color for Archer Unit")
		return
	sprite.animation = idle_animation

func _process(_delta: float) -> void:
	pass
