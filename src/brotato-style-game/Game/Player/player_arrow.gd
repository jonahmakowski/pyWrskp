extends CharacterBody2D

var direction: Vector2
var target: Vector2
var damage: float
var hits = 0

func init(t, d):
	target = t
	damage = d

func _ready():
	rotation = global_position.angle_to_point(target)
	direction = global_position.direction_to(target)
	velocity = direction * Stats.PROJECTILE_SPEED * Stats.projectile_speed_multiplyer

func _physics_process(_delta: float) -> void:
	move_and_slide()

func _process(_delta: float) -> void:
	if hits > Stats.piercing:
		queue_free()

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()
