extends CharacterBody2D

const max_size = 90
const out_distance = -400

func _ready():
	add_to_group("obstacles")
	var location = round(randf_range(-max_size, max_size))
	position.x = out_distance
	position.y = location
	if round(randf_range(1, 2)) == 1:
		$Rock.hide()
		$Log.show()

func _physics_process(_delta:float) -> void:
	if Input.is_action_pressed("sprint"):
		position.x += 2
	else:
		position.x += 1 

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	queue_free()

func _on_area_2d_body_entered(body: Node2D) -> void:
	if position.x > out_distance + 5:
		return
	if body.is_in_group("obstacles") and body != self:
		queue_free()
		$"../..".new_rock()
