# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This file defines a player weapon in a game, handling various aspects such as setting weapon data, initializing the weapon, firing projectiles, dealing damage to enemies, and managing the cooldown timer. It also includes logic for contact damage when the weapon range is zero.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more strictly to conventions.
# Functions

## set
### Explanation
Sets the weapon data and updates the sprite frames if the data and sprite are not null.
### Code
```gdscript
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
Called when the node is ready. Sets up the sprite frames if the weapon data is not null.
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
Fires a projectile at the nearest enemy within range. Creates an instance of the projectile, initializes it, and adds it to the scene.
### Code
```gdscript
func fire_projectile(targets: Array):
	var enemy = targets[0]['instance']
	var target = targets[0]['position']
	for t in targets:
		if not t['instance'].death_targeted and t['distance'] <= data.weapon_range:
			target = t['position']
			enemy = t['instance']
			break
	
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, data.damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)
	
	if enemy.health - (data.damage * Stats.damage_multiplyer) <= 0:
		enemy.death_targeted = true
```

## _process
### Explanation
Called every frame. Handles the attacking logic, including playing the sprite animation, dealing damage to enemies, and starting the cooldown timer.
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
Called when the cooldown timer times out. Resets the attacking state.
### Code
```gdscript
func _on_cooldown_timer_timeout() -> void:
	attacking = false
```

## _on_contact_area_2d_body_entered
### Explanation
Called when a body enters the contact area. Deals damage to the enemy if the weapon range is zero.
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
	var target = targets[0]['position']
	for t in targets:
		if not t['instance'].death_targeted and t['distance'] <= data.weapon_range:
			target = t['position']
			enemy = t['instance']
			break
	
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, data.damage * Stats.damage_multiplyer)
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
