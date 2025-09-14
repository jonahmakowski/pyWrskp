# Documentation for src/brotato-style-game/Game/Helpers/stats.gd

# AI Summary
This GDScript file (stats.gd) defines various game statistics for player attributes, enemy modifiers, and in-game currencies. It organizes these into variables and constants. A `DEFAULTS` dictionary is provided for easy resetting of these statistics to their initial values via the `reset()` function. The file extends `Node`, indicating it's likely a singleton or an attached script meant to manage game-wide statistical data.

The AI gave it a general rating of 9/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is highly functional and concise. It clearly defines game statistics using appropriate variable types and constants. The `reset` function is an elegant way to restore default values. Adherence to GDScript conventions is strong, with clear variable naming and proper use of `var`, `const`, and `func` keywords. The organization into logical sections also contributes to its readability and maintainability.
# Functions

## reset
### Explanation
This function iterates through the `DEFAULTS` dictionary and resets all the game statistics (player stats, enemy multipliers, currencies) to their initial default values. It uses the `set()` method to dynamically update the instance variables.
### Code
```gdscript
func reset():
	for var_name in DEFAULTS:
		set(var_name, DEFAULTS[var_name])
```
# Overall File Contents
```gdscript
extends Node

# Player
var speed_multiplyer = 1
var current_health = 10
var max_health = 10
var health_regen = 0
var damage_multiplyer = 1
var projectile_speed_multiplyer = 1
var piercing = 0
var death_value = 1

# Player Constants
const SPEED = 200
const PROJECTILE_SPEED = 250

# Enemies
var enemy_speed_multiplyer = 1
var enemy_health_multiplyer = 1
var enemy_range_multiplyer = 1
var enemy_projectile_speed_multiplyer = 1
var enemy_damage_multiplyer = 1

# Enemy Constants
const ENEMY_HEALTHS = {"Orc": 5, "Swordsman": 4, "Archer": 2}
const ENEMY_RANGE = {"Orc": 30, "Swordsman": 30, "Archer": 150}
const ENEMY_COOLDOWN = {"Orc": 1.2, "Swordsman": 1, "Archer": 3}
const ENEMY_PROJECTILE_SPEED = 250
const ENEMY_SPEED = 50
const ENEMY_DAMAGE = {"Orc": 3, "Swordsman": 1.5, "Archer": 1}

# Currencies
var enemies_killed = 0
var coins = 0

# Reset System
const DEFAULTS = {
	"speed_multiplyer": 1,
	"current_health": 10,
	"max_health": 10,
	"health_regen": 0,
	"damage_multiplyer": 1,
	"projectile_speed_multiplyer": 1,
	"piercing": 0,
	
	"enemy_speed_multiplyer": 1,
	"enemy_health_multiplyer": 1,
	"enemy_range_multiplyer": 1,
	"enemy_projectile_speed_multiplyer": 1,
	"enemy_damage_multiplyer": 1,
	
	"enemies_killed": 0,
	"coins": 0
}


func reset():
	for var_name in DEFAULTS:
		set(var_name, DEFAULTS[var_name])

```
