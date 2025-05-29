extends RigidBody2D

func _physics_process(delta: float) -> void:
	if $RayCastRight.is_colliding():
		position.x -= 1
	if $RayCastLeft.is_colliding():
		position.x += 1
