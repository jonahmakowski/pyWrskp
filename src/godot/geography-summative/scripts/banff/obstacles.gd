extends Node2D

@onready var skiier: CharacterBody2D = %Skiier
@onready var area_2d: Area2D = $Area2D

@export var obstacle:PackedScene
@export var flag:PackedScene

const max_obstacles_in_area = 6

var obstacles_in_area = 0

func obstacle_nearby(pos:int, seperation:int):
	var items = area_2d.get_overlapping_areas()
	for item in items:
		var x_pos = item.position.x
		if abs(x_pos-pos) <= seperation:
			return true
	
	return false

func _ready():
	var pos = skiier.position.y
	obstacles_in_area = len(area_2d.get_overlapping_areas())
	pos += $"..".distance_prep * 5
	position.y = pos

func _process(_delta: float) -> void:
	var pos = skiier.position.y
	obstacles_in_area = len(area_2d.get_overlapping_areas())
	pos += $"..".distance_prep * 5
	position.y = pos

func _physics_process(_delta: float) -> void:
	if obstacles_in_area < max_obstacles_in_area:
		if int(randf_range(1, 10)) == 1:
			var pos_x = randf_range(-$"..".width+20, $"..".width-20)
			var y_modifier = randf_range(-200, 200)
			$"..".add_obstacle_at(Vector2(pos_x, position.y+y_modifier+200), "Random", "Obstacles_Folder", flag)
			return
		
		var pos_x = randf_range(-$"..".width+10, $"..".width-10)
		
		while obstacle_nearby(pos_x, 20):
			pos_x = randf_range(-$"..".width+10, $"..".width-10)
		
		$"..".add_obstacle_at(Vector2(pos_x, position.y), "Random", "Obstacles_Folder")
