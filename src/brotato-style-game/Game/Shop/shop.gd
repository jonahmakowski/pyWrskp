extends Control

@export var weapons: Array[weapon]
var weapons_with_weights: Array[weapon]
@onready var weapon_selling: HBoxContainer = %WeaponSelling
@onready var weapon_selection: HBoxContainer = %WeaponSelection
@onready var reroll_button: Button = %RerollButton

var reroll_cost = 1

func _ready() -> void:
	for w in weapons:
		for i in range(w.weight):
			weapons_with_weights.append(w)
	
	Messanger.REDO_SELLING.connect(redo_selling)
	Messanger.REDO_SELECTION.connect(redo_selection)
	redo_selling()
	redo_selection()
	
	Messanger.MONEY_CHANGE.connect(reroll_enabled)
	reroll_enabled()

func redo_selection():
	for child in weapon_selection.get_children():
		child.queue_free()
	
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

func _on_reroll_button_pressed() -> void:
	if Stats.coins < reroll_cost:
		return
	
	Stats.coins -= reroll_cost
	reroll_cost *= 2
	reroll_button.text = "Reroll\n(Cost: {0})".format([reroll_cost])
	
	redo_selection()

func reroll_enabled() -> void:
	if Stats.coins < reroll_cost:
		reroll_button.disabled = true
	else:
		reroll_button.disabled = false
