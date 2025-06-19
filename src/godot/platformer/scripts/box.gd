extends RigidBody2D

const PUSH_THRESHOLD := 0.1
const PUSH_FORCE_MULTIPLIER := 1.5

func _integrate_forces(state: PhysicsDirectBodyState2D) -> void:
	var push_velocity := 0.0

	if $RayCastLeft.is_colliding():
		var collider = $RayCastLeft.get_collider()
		if _is_valid_pusher(collider):
			var char_vel = collider.velocity
			if char_vel.x > PUSH_THRESHOLD:
				push_velocity = char_vel.x

	elif $RayCastRight.is_colliding():
		var collider = $RayCastRight.get_collider()
		if _is_valid_pusher(collider):
			var char_vel = collider.velocity
			if char_vel.x < -PUSH_THRESHOLD:
				push_velocity = char_vel.x

	state.linear_velocity = Vector2(push_velocity * PUSH_FORCE_MULTIPLIER, state.linear_velocity.y)

func _is_valid_pusher(collider: Object) -> bool:
	# Ensure collider is a CharacterBody2D with a velocity and standing on the ground
	if collider is CharacterBody2D and "velocity" in collider:
		if collider.has_method("is_on_floor") and collider.is_on_floor():
			return true
	return false
