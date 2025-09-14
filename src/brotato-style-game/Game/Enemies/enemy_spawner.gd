extends Node2D

@export var max_x: int
@export var max_y: int
var interval = 1
var max_enemies = 10

var current_interval = 0.0

func _ready() -> void:
	pass

func spawn_enemy() -> void:
	var x_pos = randf_range(max_x, -max_x)
	var y_pos = randf_range(max_y, -max_y)
	var pos = Vector2(x_pos, y_pos)
	var type = ["Archer", "Swordsman", "Orc"][randi_range(0, 2)]
	
	var instance = Scenes.enemy.instantiate()
	instance.init(type)
	instance.position = pos
	
	get_parent().add_child(instance)

func count_enemies():
	var enemies = 0
	for child in get_parent().get_children():
		if child.is_in_group("enemy"):
			enemies += 1
	
	return enemies

func _process(delta: float) -> void:
	current_interval += delta
	if current_interval >= interval:
		current_interval = 0.0
		if count_enemies() < max_enemies:
			spawn_enemy()
