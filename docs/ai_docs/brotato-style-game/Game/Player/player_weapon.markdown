# Documentation for src/brotato-style-game/Game/Player/player_weapon.gd

# AI Summary
This code defines a player weapon in a game. It includes functions to update the weapon sprite, initialize the weapon, set up the weapon properties when the node is ready, fire projectiles, handle the attack process, and handle the cooldown timer timeout.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some areas where it could be more concise and adhere more closely to conventions.
# Functions

## update_weapons
### Explanation
This function updates the weapon sprite based on the current weapon type and weapon. It hides the current sprite and shows the new one if the weapon and weapon type are valid and the engine is in editor hint mode. If the weapon or weapon type is empty, it hides the sprite.
### Code
```gdscript
func update_weapons():
	if (WEAPON_POWERS.has(weapon) and WEAPON_POWERS[weapon].has(weapon_type)) and Engine.is_editor_hint():
		sprite.hide()
		sprite = get_node(WEAPON_POWERS[weapon][weapon_type]["sprite"])
		sprite.show()
	
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
This function is called when the node is ready. It sets up the sprite, damage, weapon range, cooldown, and melee properties based on the current weapon and weapon type. It also shows the sprite if the engine is not in editor hint mode.
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
This function fires a projectile towards a target. It instantiates a player arrow, initializes it with the target and damage, sets its global position, and adds it to the parent's parent's parent.
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
This function is called every frame. It checks if the player is not attacking and if there are enemies within weapon range. If so, it sets attacking to true, deals damage or fires a projectile based on the melee property, and starts the cooldown timer.
### Code
```gdscript
func _process(delta: float) -> void:
	if Engine.is_editor_hint():
		return
	
	if not attacking:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= weapon_range:
			attacking = true
			
			if melee:
				enemies[0]['instance'].take_damage(damage * Stats.damage_multiplyer)
				print('Did melee damage')
			else:
				fire_projectile(enemies[0]['position'])
				print('Fired a projectile')
			
			cooldown_timer.wait_time = cooldown
			cooldown_timer.start()
```

## _on_cooldown_timer_timeout
### Explanation
This function is called when the cooldown timer times out. It sets attacking to false.
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
var sprite: Sprite2D
var damage: float
var weapon_range: float
var cooldown: float
var melee: bool

var attacking = false

var WEAPON_POWERS = {
	"club": {"wooden": {"sprite": "Sprites/Wooden/Club", "damage": 5, "range": 30, "cooldown": 2, "melee": true}},
	"basicbow": {"wooden": {"sprite": "Sprites/Wooden/BasicBow", "damage": 2, "range": 150, "cooldown": 1.5, "melee": false}}
}

@onready var cooldown_timer: Timer = %CooldownTimer

func update_weapons():
	if (WEAPON_POWERS.has(weapon) and WEAPON_POWERS[weapon].has(weapon_type)) and Engine.is_editor_hint():
		sprite.hide()
		sprite = get_node(WEAPON_POWERS[weapon][weapon_type]["sprite"])
		sprite.show()
	
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
	
	if not attacking:
		var enemies = get_parent().get_parent().enemies_list
		if len(enemies) > 0 and enemies[0]['distance'] <= weapon_range:
			attacking = true
			
			if melee:
				enemies[0]['instance'].take_damage(damage * Stats.damage_multiplyer)
				print('Did melee damage')
			else:
				fire_projectile(enemies[0]['position'])
				print('Fired a projectile')
			
			cooldown_timer.wait_time = cooldown
			cooldown_timer.start()

func _on_cooldown_timer_timeout() -> void:
	attacking = false

```
