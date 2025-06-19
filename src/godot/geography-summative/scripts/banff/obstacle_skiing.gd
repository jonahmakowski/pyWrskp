extends StaticBody2D

@export var type:String
var given_location = Vector2()
var idc_about_clipping = false

func init(p_location, p_type="Random", clipping=false):
	type = p_type
	given_location = p_location
	position = given_location
	idc_about_clipping = clipping

func _ready():
	position = given_location
	if type == "Random":
		type = "Rock" if round(randf_range(1, 2)) == 1 else "Tree"
	
	if type == "Rock":
		$Rock.visible = true
	elif type == "Log":
		$Log.visible = true
		$TileMapLayer.visible = true
	elif type =="Tree":
		$Tree.visible = true
		$LogRockArea2D.monitoring = false
		$TreeArea2D.monitoring = true

func _process(_delta: float) -> void:
	if len($NearbyObstacels.get_overlapping_bodies()) > 1:
		if not idc_about_clipping:
			queue_free()

func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
	$"../..".side_obstacles_at_pos.erase(int(position.y))
	$"../..".side_obstacles_at_neg.erase(int(position.y))
	queue_free()

func _on_area_2d_body_entered(_body: Node2D) -> void:
	Controller.new_scene = get_tree().current_scene.scene_file_path
	get_tree().change_scene_to_file("res://scenes/failure_screen.tscn")
