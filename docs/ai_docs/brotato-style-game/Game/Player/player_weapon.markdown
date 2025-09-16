# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This file defines a player weapon in a game. It includes functions for updating the weapon sprite, initializing the weapon, setting up the weapon when the node is ready, firing projectiles, handling the weapon's attack logic, and managing the cooldown timer. The weapon's properties, such as damage, range, and cooldown, are defined in a dictionary called WEAPON_POWERS.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise, such as the update_weapons function. The code also follows the conventions of the Godot game engine, but there are some areas where the code could be more consistent, such as the use of snake_case for variable names.
# Functions

## update_weapons
### Explanation
This function updates the weapon sprite based on the current weapon type and weapon. It hides the current sprite and shows the new one if the weapon and weapon type are valid. It also prints a message indicating that the sprite update was performed.
### Code
```gdscript
func update_weapons():
	if (WEAPON_POWERS.has(weapon) and WEAPON_POWERS[weapon].has(weapon_type)) and Engine.is_editor_hint():
		sprite.hide()
		sprite = get_node(WEAPON_POWERS[weapon][weapon_type]["sprite"])
		sprite.show()
		print('Performed Sprite Update')

	if (weapon == "" or weapon_type == "") and sprite != null:
		sprite.hide()
```

## init
### Explanation
This function initializes the weapon type and weapon.
### Code
```gdscript
func init(weapon_ty, w):
	weapon_type = weapon_ty
	weapon = w
```

## _ready
### Explanation
This function is called when the node is ready. It sets up the weapon sprite and properties based on the current weapon type and weapon. It also hides the sprite if the weapon or weapon type is empty.
### Code
```gdscript
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
```

## fire_projectile
### Explanation
This function fires a projectile towards a target. It creates an instance of the player_arrow scene, initializes it with the target position and damage, and adds it to the game scene.
### Code
```gdscript
func fire_projectile(target: Vector2):
	var instance = Scenes.player_arrow.instantiate()
	instance.init(target, damage * Stats.damage_multiplyer)
	instance.global_position = global_position
	get_parent().get_parent().get_parent().add_child(instance)
```

## _process
### Explanation
This function is called every frame. It handles the weapon's attack logic. If the weapon has a range, it checks for enemies within range and attacks them. If the weapon is melee, it deals damage directly to the enemy. If the weapon is ranged, it fires a projectile. If the weapon has no range, it checks for overlapping enemies and deals damage to them.
### Code
```gdscript
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
```

## _on_cooldown_timer_timeout
### Explanation
This function is called when the cooldown timer times out. It sets the attacking variable to false, allowing the weapon to attack again.
### Code
```gdscript
func _on_cooldown_timer_timeout() -> void:
	attacking = false
```
# Overall File Contents
```gdscript
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

```
