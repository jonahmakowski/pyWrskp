# Documentation for src/brotato-style-game/Game/Helpers/stats.gd

# AI Summary
This file is a Godot script that extends the Node class and manages various statistics and properties for a game. It includes variables for player attributes, enemy attributes, currencies, level stats, and constants for rarity and reset system. The script also provides a reset function to revert all variables to their default values.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some inconsistencies in naming conventions and some variables could be better organized or documented.
# Functions
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
var rotation_speed = 1.0
var max_weapons = 4
var num_of_upgrades = 3
var refund_rate = 50
@export var base_weapon: weapon
@onready var current_weapons: Array[weapon] = [base_weapon]
var weapons_in_shop = 3

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

# Level Stats
var max_enemies = 30
var enemy_spawn_rate = 1
var level_time = 30
var level = 1

# Rarity Constants
const RARITY_TO_WEIGHT = {1: 20}
const RARITY_TO_TEXT = {1: "Common"}

# Reset System
var DEFAULTS = {
	"speed_multiplyer": 1,
	"current_health": 10,
	"max_health": 10,
	"health_regen": 0,
	"damage_multiplyer": 1,
	"projectile_speed_multiplyer": 1,
	"piercing": 0,
	"rotation_speed": 1.0,
	"max_weapons": 4,
	"num_of_upgrades": 3,
	"refund_rate": 50,
	"current_weapons": [base_weapon],
	
	"enemy_speed_multiplyer": 1,
	"enemy_health_multiplyer": 1,
	"enemy_range_multiplyer": 1,
	"enemy_projectile_speed_multiplyer": 1,
	"enemy_damage_multiplyer": 1,
	
	"enemies_killed": 0,
	"coins": 0,
	
	"max_enemies": 30,
	"enemy_spawn_rate": 1,
	"level_time": 30,
	"level": 1
}

func reset():
	for var_name in DEFAULTS:
		set(var_name, DEFAULTS[var_name])

```
