extends Control

@export var weapons: Array[weapon]
var weapons_with_weights: Array[weapon]
@onready var weapon_selling: HBoxContainer = %WeaponSelling
@onready var weapon_selection: HBoxContainer = %WeaponSelection

func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	redo_selling()
	
	for i in range(Stats.weapons_in_shop):
		var instance = Scenes.shop_weapon_selection.instantiate()
		instance.data = get_random_weapon()
		weapon_selection.add_child(instance)

func redo_selling():
	for child in weapon_selling.get_children():
		child.queue_free()
	
	for w in Stats.current_weapons:
		var instance = Scenes.shop_weapon_selling.instantiate()
		instance.data = w
		weapon_selling.add_child(instance)

func get_random_weapon():
	var index = randi_range(0, len(weapons_with_weights) - 1)
	return weapons_with_weights[index]

func _on_button_pressed() -> void:
	if Stats.enemy_spawn_rate > 1:
		Stats.enemy_spawn_rate -= 0.25
	elif Stats.enemy_spawn_rate > 0.05:
		Stats.enemy_spawn_rate -= 0.05
	elif Stats.enemy_spawn_rate > 0.005:
		Stats.enemy_spawn_rate -= 0.001
	
	Stats.enemy_health_multiplyer += 0.1
	Stats.enemy_damage_multiplyer += 0.1
	Stats.enemy_speed_multiplyer += 0.1
	Stats.enemy_projectile_speed_multiplyer += 0.05
	Stats.level_time += 2
	
	Stats.level += 1
	
	get_tree().change_scene_to_packed(Scenes.level1)
