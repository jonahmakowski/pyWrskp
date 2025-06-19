extends CharacterBody2D

var type

func init(pos: Vector2, t: String):
	position = pos
	$Sprite.animation = t
	type = t

func _physics_process(_delta: float) -> void:
	position.y += 1
