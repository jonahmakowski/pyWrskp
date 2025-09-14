extends Node2D

@onready var nav_region: NavigationRegion2D = %NavigationRegion2D
@onready var enemy_spawner: Node2D = %EnemySpawner


func _ready() -> void:
	nav_region.bake_navigation_polygon(true)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
