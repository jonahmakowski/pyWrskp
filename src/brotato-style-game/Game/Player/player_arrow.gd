extends CharacterBody2D

var direction: Vector2
var target: CharacterBody2D
var damage: float
var hits = 0
var bounces = 0

func init(t, d):
	target = t
	damage = d

func _ready():
	rotation = global_position.angle_to_point(target.global_position)
	direction = global_position.direction_to(target.global_position)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _physics_process(_delta: float) -> void:
	move_and_slide()

func enemy_sort(a, b): # by distance
	if a["distance"] < b["distance"]:
		return true
	return false

func get_enemies() -> Array:
	var enemies = []
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			if child.sprite.animation == "Death":
				continue
			enemies.append({"enemy": child.enemy_type, "position": child.global_position, "distance": global_position.distance_to(child.global_position), "instance": child})
	
	enemies.sort_custom(enemy_sort)
	
	return enemies

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
		return
	
	if target == null and Stats.arrow_tracing > 0:
		target = get_enemies()[0]['instance']
	
	if Stats.arrow_tracing > 0:
		rotation = global_position.angle_to_point(target.global_position)
		direction = global_position.direction_to(target.global_position)
		velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()

func _on_bounce_detecter_screen_exited() -> void:
	if bounces >= Stats.projectile_bounces:
		return
	
	velocity *= -1
	rotation_degrees += 180
	bounces += 1
