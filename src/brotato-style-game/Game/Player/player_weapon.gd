@tool
extends Node2D

@export var data: weapon: # The weapon (ie club)
	set(new_weapon):
		data = new_weapon
		if data != null and sprite != null:
			%Sprite.sprite_frames = data.sprite

@onready var sprite: AnimatedSprite2D = %Sprite

var attacking = false

@onready var cooldown_timer: Timer = %CooldownTimer
@onready var contact_area_2d: Area2D = %ContactArea2D

func init(w):
	data = w

func _ready() -> void:
	if data == null:
		push_error("Weapon data is null")
		return
	
	%Sprite.sprite_frames = data.sprite

func fire_projectile(target: Vector2):
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)

func _process(_delta: float) -> void:
	if Engine.is_editor_hint():
		return
	
	if not attacking and data.weapon_range > 0:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= data.weapon_range:
			attacking = true
			
			sprite.play()
			
			if data.melee:
				enemies[0]['instance'].take_damage(data.damage * Stats.damage_multiplyer)
				print('Did melee damage')
			else:
				fire_projectile(enemies[0]['position'])
				print('Fired a projectile')
			
			cooldown_timer.wait_time = data.cooldown
			cooldown_timer.start()

	if data.weapon_range == 0:
		for body in contact_area_2d.get_overlapping_bodies():
			if body.is_in_group("enemy") and body.sprite.animation != "Hurt":
				body.take_damage(data.damage * Stats.damage_multiplyer)
				print('Did contact damage')

func _on_cooldown_timer_timeout() -> void:
	attacking = false
