extends CharacterBody2D

const speed = 100

func _physics_process(_delta: float) -> void:
	var direction = Input.get_vector("move_left", "move_right", "move_up", "move_down").normalized()
	velocity = direction * speed
	
	if direction.y == 0 and direction.x == 0:
		$AnimatedSprite2D.animation = "idle"
	elif abs(direction.x) > abs(direction.y):
		$AnimatedSprite2D.animation = "walking_sideways"
		$AnimatedSprite2D.flip_h = true if direction.x > 0 else false
	elif direction.y > 0:
		$AnimatedSprite2D.animation = "walking_down"
	else:
		$AnimatedSprite2D.animation = "walking_up"
	
	move_and_slide()
