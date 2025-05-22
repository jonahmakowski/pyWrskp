extends RigidBody2D

const SPEED = 1

var direction = 1

func _ready() -> void:
	pass

func _physics_process(delta: float) -> void:
	if $RayCastRight.is_colliding() or $RayCastLeft.is_colliding():
		direction = -1 if $RayCastRight.is_colliding() else 1
	
	$AnimatedSprite2D.set_flip_h(true if direction == -1 else false)
	
	position.x += direction * SPEED
	
