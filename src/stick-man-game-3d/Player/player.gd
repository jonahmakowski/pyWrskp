extends CharacterBody3D
class_name Player


const SPEED = 5.0
const JUMP_VELOCITY = 4.5
const MOUSE_SENSATIVITY = 0.002
const PITCH_LIMIT = 85.0

@onready var pivot: Node3D = %Pivot

var pivot_angle: Vector2:
	get():
		return Vector2(pivot.rotation.x, rotation.y)

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity += get_gravity() * delta

	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	var input_dir := Input.get_vector("left", "right", "forward", "back")
	var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()

func _input(event: InputEvent) -> void:
	# Release the mouse
	if event.is_action_pressed("release_mouse"):
		Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
		get_viewport().set_input_as_handled()
	
	if event.is_action_pressed("lock_mouse"):
		Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
		get_viewport().set_input_as_handled()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
		rotate_y(-event.relative.x * MOUSE_SENSATIVITY)
		pivot.rotate_x(-event.relative.y * MOUSE_SENSATIVITY)
		var current_pitch : float = pivot.rotation.x
		var min_pitch : float = deg_to_rad(-PITCH_LIMIT)
		var max_pitch : float = deg_to_rad(PITCH_LIMIT)
		pivot.rotation.x = clamp(current_pitch, min_pitch, max_pitch)
		get_viewport().set_input_as_handled()

func fire_shot(scene: PackedScene, direction: Vector3):
	var instance: Projectile = scene.instantiate()
	instance.direction = direction
	instance.rotation = rotation
	get_parent().add_child(instance)
	instance.global_position = global_position
