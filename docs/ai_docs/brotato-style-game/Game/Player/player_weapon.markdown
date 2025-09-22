# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This file defines a player weapon in a Godot game. It includes functionality for setting weapon data, initializing the weapon, firing projectiles, processing attacks, handling cooldowns, and dealing contact damage. The weapon can be either melee or ranged, and it checks for enemies within its range to determine when to attack.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more closely to conventions.
# Functions

## set
### Explanation
Sets the weapon data and updates the sprite frames if the data and sprite are not null.
### Code
```gdscript
@export var data: weapon: # The weapon (ie club)
	set(new_weapon):
		data = new_weapon
		if data != null and sprite != null:
			%Sprite.sprite_frames = data.sprite
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
Initializes the weapon sprite frames and checks if the weapon data is null.
### Code
```gdscript
func _ready() -> void:
	if data == null:
		push_error("Weapon data is null")
		return

	%Sprite.sprite_frames = data.sprite
```

## fire_projectile
### Explanation
Fires a projectile towards the nearest enemy within the weapon range.
### Code
```gdscript
func fire_projectile(targets: Array):
	var enemy = targets[0]['instance']
	for t in targets:
		if not t['instance'].death_targeted and t['distance'] <= data.weapon_range:
			enemy = t['instance']
			break

	var instance = Scenes.player_arrow.instantiate()
	instance.init(enemy, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)

	if enemy.health - (data.damage * Stats.damage_multiplyer) <= 0:
		enemy.death_targeted = true
```

## _process
### Explanation
Processes the weapon's attack logic, including checking for enemies within range and initiating attacks.
### Code
```gdscript
func _process(_delta: float) -> void:
	if Engine.is_editor_hint():
		return

	if not attacking and data.weapon_range > 0:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= data.weapon_range:
			attacking = true

			sprite.play()

			if data.melee:
				for enemy in enemies:
					if enemy['distance'] <= data.weapon_range:
						enemy['instance'].take_damage(data.damage * Stats.damage_multiplyer)
			else:
				fire_projectile(enemies)

			cooldown_timer.wait_time = data.cooldown
			cooldown_timer.start()
```

## _on_cooldown_timer_timeout
### Explanation
Resets the attacking state when the cooldown timer times out.
### Code
```gdscript
func _on_cooldown_timer_timeout() -> void:
	attacking = false
```

## _on_contact_area_2d_body_entered
### Explanation
Handles contact damage when the weapon's contact area enters another body.
### Code
```gdscript
func _on_contact_area_2d_body_entered(body: Node2D) -> void:
	if data.weapon_range == 0:
		if body.is_in_group("enemy"):
			body.take_damage(data.damage * Stats.damage_multiplyer)
			print('Did contact damage')
```
# Overall File Contents
```gdscript
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

func fire_projectile(targets: Array):
	var enemy = targets[0]['instance']
	for t in targets:
		if not t['instance'].death_targeted and t['distance'] <= data.weapon_range:
			enemy = t['instance']
			break
	
	var instance = Scenes.player_arrow.instantiate()
	instance.init(enemy, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)
	
	if enemy.health - (data.damage * Stats.damage_multiplyer) <= 0:
		enemy.death_targeted = true

func _process(_delta: float) -> void:
	if Engine.is_editor_hint():
		return
	
	if not attacking and data.weapon_range > 0:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= data.weapon_range:
			attacking = true
			
			sprite.play()
			
			if data.melee:
				for enemy in enemies:
					if enemy['distance'] <= data.weapon_range:
						enemy['instance'].take_damage(data.damage * Stats.damage_multiplyer)
			else:
				fire_projectile(enemies)
			
			cooldown_timer.wait_time = data.cooldown
			cooldown_timer.start()

func _on_cooldown_timer_timeout() -> void:
	attacking = false

func _on_contact_area_2d_body_entered(body: Node2D) -> void:
	if data.weapon_range == 0:
		if body.is_in_group("enemy"):
			body.take_damage(data.damage * Stats.damage_multiplyer)
			print('Did contact damage')

```
