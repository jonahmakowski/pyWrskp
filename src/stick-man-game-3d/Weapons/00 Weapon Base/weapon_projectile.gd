extends CharacterBody3D
class_name Projectile

var direction: Vector3

func _ready():
	velocity = direction

func _physics_process(_delta: float) -> void:
	move_and_slide()
