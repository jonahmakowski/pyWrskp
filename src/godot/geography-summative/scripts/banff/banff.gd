extends Node

@onready var skiier: CharacterBody2D = %Skiier

@export var obstacle_scene:PackedScene

var side_obstacles_at_pos = []
var side_obstacles_at_neg = []

const width = 200
const seperation = 20
const distance_prep = 200

func _ready():
	TotalTimer.timer_on = true
	var skiier_position := int(skiier.position.y)
	for i in range(-distance_prep, distance_prep):
		add_sides(skiier_position + i)

func _process(_delta: float) -> void:
	var skiier_position := int(skiier.position.y) - (int(skiier.position.y) % 20)
	for i in range(-distance_prep, distance_prep):
		add_sides(skiier_position + i)

func add_obstacle_at(pos:Vector2, ty:String, to:String, scene=obstacle_scene):
	var instance = scene.instantiate()
	instance.init(pos, ty)
	get_node(to).add_child(instance)

func add_sides(pos:int):
	var already_exists_pos := false
	var already_exists_neg := false
	
	for y in side_obstacles_at_pos:
		if abs(y - pos) <= seperation:
			already_exists_pos = true
			break

	if not already_exists_pos:
		var obstacle := obstacle_scene.instantiate()
		obstacle.init(Vector2(width, pos), 'Log', true)
		$Sides.call_deferred("add_child", obstacle)
		side_obstacles_at_pos.append(pos)
	
	
	for y in side_obstacles_at_neg:
		if abs(y - pos) <= seperation:
			already_exists_neg = true
			break

	if not already_exists_neg:
		var obstacle := obstacle_scene.instantiate()
		obstacle.init(Vector2(-width, pos), 'Log', true)
		$Sides.call_deferred("add_child", obstacle)
		side_obstacles_at_neg.append(pos)
