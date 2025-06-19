extends StaticBody2D

@export var box_color_id = ""
var not_solid = false

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$AnimatedSprite2D.animation = "solid_" + box_color_id.to_lower()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	not_solid = Controller.buttons_pressed[box_color_id.to_lower()]
	if not_solid:
		$CollisionShape2D.disabled = true
		$AnimatedSprite2D.animation = "non_solid_" + box_color_id.to_lower()
	else:
		$CollisionShape2D.disabled = false
		$AnimatedSprite2D.animation = "solid_" + box_color_id.to_lower()
