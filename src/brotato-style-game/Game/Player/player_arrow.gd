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

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()
	
	if Stats.arrow_tracing > 0 and target != null:
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
