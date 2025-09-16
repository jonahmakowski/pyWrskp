extends Node2D

@onready var nav_region: NavigationRegion2D = %NavigationRegion2D
@onready var enemy_spawner: Node2D = %EnemySpawner
@onready var level_over_timer: Timer = $LevelOverTimer


func _ready() -> void:
	nav_region.bake_navigation_polygon(true)
	level_over_timer.wait_time = Stats.level_time
	level_over_timer.start()


func _on_level_over_timer_timeout() -> void:
	Stats.current_health = Stats.max_health
	get_tree().change_scene_to_packed(Scenes.upgrade_selection)
