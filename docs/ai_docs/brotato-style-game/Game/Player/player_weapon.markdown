# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This GDScript file implements the logic for a player's weapon in a Brotato-style game. It handles initialization, sprite setup, attack mechanics for both melee and ranged weapons (including projectile firing), and managing attack cooldowns.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, handling both melee and ranged combat effectively. Good use of `@onready` and `@export` is observed. However, the repeated `get_parent().get_parent().get_parent()` for scene tree navigation is a brittle approach and could lead to issues if the scene structure changes, indicating a slight deviation from best practices in terms of scene management and tight coupling.
# Functions

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
Called when the node is ready. It initializes the weapon's sprite frames based on the provided `data`.
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
Handles the logic for firing a projectile. It finds a suitable target, instantiates a 'player_arrow' scene, initializes it, positions it, and adds it to the scene. It also marks the target for death if the projectile is lethal.
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
Called every frame to update the weapon's state. It checks if an attack can be initiated, plays the attack animation, and either deals melee damage to nearby enemies or fires a projectile based on the weapon type. It then starts the cooldown timer.
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
Resets the `attacking` flag to `false` when the cooldown timer finishes, allowing the weapon to attack again.
### Code
```gdscript
func _on_cooldown_timer_timeout() -> void:
	attacking = false
```

## _on_contact_area_2d_body_entered
### Explanation
Handles melee damage when a body enters the weapon's `contact_area_2d`. If the weapon has a range of 0 and the entered body is an 'enemy', it deals damage.
### Code
```gdscript
func _on_contact_area_2d_body_entered(body: Node2D) -> void:
	if data.weapon_range == 0:
		if body.is_in_group("enemy"):
			body.take_damage(data.damage * Stats.damage_multiplyer)
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

```
