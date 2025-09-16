# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This file defines a weapon system for a game. It includes functions to set and initialize the weapon, handle the weapon's behavior each frame, and manage the cooldown timer. The weapon can be either melee or ranged, and it can deal damage to enemies.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some areas where it could be more concise and adhere more closely to conventions.
# Functions

## set
### Explanation
Sets the weapon data and updates the sprite frames if the data and sprite are not null.
### Code
```gdscript
	set(new_weapon):
		data = new_weapon
		if data != null and sprite != null:
			sprite.sprite_frames = data.sprite
```

## init
### Explanation
Initializes the weapon with the given data.
### Code
```gdscript
func init(w):
	data = w
```

## _ready
### Explanation
Initializes the weapon when the node is ready. It checks if the weapon data is null and updates the sprite frames accordingly.
### Code
```gdscript
func _ready() -> void:
	if data == null:
		push_error("Weapon data is null")
		return
	sprite.sprite_frames = data.sprite
```

## fire_projectile
### Explanation
Fires a projectile towards the target. It instantiates a projectile, initializes it with the target and damage, and adds it to the scene.
### Code
```gdscript
func fire_projectile(target: Vector2):
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)
```

## _process
### Explanation
Processes the weapon's behavior each frame. It checks if the weapon is not attacking and within range of an enemy, then attacks. It also handles contact damage for melee weapons.
### Code
```gdscript
func _process(delta: float) -> void:
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
```

## _on_cooldown_timer_timeout
### Explanation
Resets the attacking state when the cooldown timer times out.
### Code
```gdscript
func _on_cooldown_timer_timeout() -> void:
	attacking = false
```
# Overall File Contents
```gdscript
@tool
extends Node2D

@export var data: weapon: # The weapon (ie club)
	set(new_weapon):
		data = new_weapon
		if data != null and sprite != null:
			sprite.sprite_frames = data.sprite

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
	sprite.sprite_frames = data.sprite

func fire_projectile(target: Vector2):
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)

func _process(delta: float) -> void:
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

```
