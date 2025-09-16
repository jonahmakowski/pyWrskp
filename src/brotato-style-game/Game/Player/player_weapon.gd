@tool
extends Node2D

@export var weapon_type: String: # The material (ie wooden)
	set(new_weapon_type):
		weapon_type = new_weapon_type
		update_weapons()

@export var weapon: String: # The weapon (ie club)
	set(new_weapon):
		weapon = new_weapon
		update_weapons()

var sprite: AnimatedSprite2D
var damage: float
var weapon_range: float
var cooldown: float
var melee: bool

var attacking = false

var WEAPON_POWERS = {
	"club": {"wooden": {"sprite": "Sprites/Wooden/Club", "damage": 5, "range": 30, "cooldown": 2, "melee": true}},
	"basicbow": {"wooden": {"sprite": "Sprites/Wooden/BasicBow", "damage": 2, "range": 150, "cooldown": 1.5, "melee": false}},
	"sword": {"wooden": {"sprite": "Sprites/Wooden/Sword", "damage": 2, "range": 0, "cooldown": 0, "melee": true}}
}

@onready var cooldown_timer: Timer = %CooldownTimer
@onready var contact_area_2d: Area2D = %ContactArea2D

func update_weapons():
	if (WEAPON_POWERS.has(weapon) and WEAPON_POWERS[weapon].has(weapon_type)) and Engine.is_editor_hint():
		sprite.hide()
		sprite = get_node(WEAPON_POWERS[weapon][weapon_type]["sprite"])
		sprite.show()
		print('Performed Sprite Update')
	
	if (weapon == "" or weapon_type == "") and sprite != null:
		sprite.hide()

func init(weapon_ty, w):
	weapon_type = weapon_ty
	weapon = w

func _ready() -> void:
	if not WEAPON_POWERS.has(weapon) or not WEAPON_POWERS[weapon].has(weapon_type):
		return
	
	sprite = get_node(WEAPON_POWERS[weapon][weapon_type]["sprite"])
	if not Engine.is_editor_hint():
		damage = WEAPON_POWERS[weapon][weapon_type]["damage"]
		weapon_range = WEAPON_POWERS[weapon][weapon_type]["range"]
		cooldown = WEAPON_POWERS[weapon][weapon_type]["cooldown"]
		melee = WEAPON_POWERS[weapon][weapon_type]["melee"]
	
	sprite.show()

func fire_projectile(target: Vector2):
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)

func _process(delta: float) -> void:
	if Engine.is_editor_hint():
		return
	
	if not attacking and weapon_range > 0:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= weapon_range:
			attacking = true
			
			sprite.play()
			
			if melee:
				enemies[0]['instance'].take_damage(damage * Stats.damage_multiplyer)
				print('Did melee damage')
			else:
				fire_projectile(enemies[0]['position'])
				print('Fired a projectile')
			
			cooldown_timer.wait_time = cooldown
			cooldown_timer.start()
	
	if weapon_range == 0:
		for body in contact_area_2d.get_overlapping_bodies():
			if body.is_in_group("enemy") and body.sprite.animation != "Hurt":
				body.take_damage(damage * Stats.damage_multiplyer)
				print('Did contact damage')

func _on_cooldown_timer_timeout() -> void:
	attacking = false
