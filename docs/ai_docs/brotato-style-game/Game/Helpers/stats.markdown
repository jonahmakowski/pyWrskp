# Documentation for src/brotato-style-game/Game/Helpers/stats.gd

# AI Summary
This file defines a Node class that extends the Node class in Godot. It contains variables and constants for player attributes, enemy attributes, currencies, level stats, and rarity constants. It also includes a dictionary of pretty names for these variables. The file also includes functions to define default values for these variables and to reset the game state to these default values.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is generally well-structured and easy to read. However, there are some inconsistencies in the naming conventions, such as the use of underscores in some variable names and camelCase in others. Additionally, the code could benefit from more comments to explain the purpose of certain variables and functions.
# Functions

## define_defaults
### Explanation
This function initializes the DEFAULTS dictionary with default values for various player and enemy attributes. It sets default values for player stats like speed multiplier, health, damage multiplier, etc., and also sets default values for enemy attributes like speed multiplier, health multiplier, etc. Additionally, it sets default values for game-related variables like enemies killed, coins, enemy spawn rate, level time, and level.
### Code
```gdscript
func define_defaults():
	DEFAULTS = {
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
		"projectile_bounces": 0,
		"arrow_tracing": 0,
		"coin_retrieval_percentage": 0,
		
		"enemy_speed_multiplyer": 1,
		"enemy_health_multiplyer": 1,
		"enemy_range_multiplyer": 1,
		"enemy_projectile_speed_multiplyer": 1,
		"enemy_damage_multiplyer": 1,
		
		"enemies_killed": 0,
		"coins": 0,
		
		"enemy_spawn_rate": 2,
		"level_time": 30,
		"level": 1
	}
```

## _ready
### Explanation
This function is called when the node is ready. It calls the define_defaults() function to initialize the DEFAULTS dictionary with default values.
### Code
```gdscript
func _ready():
	define_defaults()
```

## reset
### Explanation
This function resets the game state to its default values. It clears the current_weapons array and appends a duplicate of the base_weapon to it. Then, it iterates over the DEFAULTS dictionary and sets each variable to its default value using the set() function.
### Code
```gdscript
func reset():
	current_weapons.clear()
	current_weapons.append(base_weapon.duplicate(true))
	
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
var piercing: int = 0
var death_value = 1
var rotation_speed = 1.0
var max_weapons: int = 4
var num_of_upgrades: int = 3
var refund_rate = 50
@export var base_weapon: weapon
@onready var current_weapons: Array[weapon] = [base_weapon.duplicate(true)]
var weapons_in_shop: int = 3
var projectile_bounces: int = 0
var arrow_tracing = 0:
	set(value):
		if value >= 1:
			arrow_tracing = 1
		else:
			arrow_tracing = 0

var coin_retrieval_percentage: int = 0:
	set(value):
		if value >= 100:
			coin_retrieval_percentage = 100
		else:
			coin_retrieval_percentage = value

# Player Constants
const SPEED = 200
const PROJECTILE_SPEED = 250
const COIN_MOVEMENT_SPEED = 210

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
var coins = 0:
	set(value):
		coins = value
		Messanger.MONEY_CHANGE.emit()

# Level Stats
var enemy_spawn_rate = 2
var level_time = 30
var level = 1

# Rarity Constants
const RARITY_TO_WEIGHT = {1: 20, 2: 16, 3: 12, 4: 8, 5: 4, 6: 2, 7: 1}
const RARITY_TO_TEXT = {1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary", 6: "Mythic", 7: "Unique"}

# Pretty Names
const NAMES = {
	"enemies_killed": "Enemies Killed",
	
	"speed_multiplyer": "Speed Multiplyer",
	"max_health": "Max Health",
	"health_regen": "Health Regeneration (per second)",
	"damage_multiplyer": "Damage Multiplyer",
	"projectile_speed_multiplyer": "Projectile Speed Multiplyer",
	"piercing": "Piercing",
	"rotation_speed": "Rotation Speed",
	"max_weapons": "Max Weapons",
	"num_of_upgrades": "Number of Upgrades in Upgrade Panel",
	"refund_rate": "Refund Rate (in percentage returned)",
	"projectile_bounces": "Projectile Bounces (off edge of screen)",
	"arrow_tracing": "Arrow Tracing (Aimbot)",
	"coin_retrieval_percentage": "Coin Retrieval Percentage",
	
	"enemy_speed_multiplyer": "Enemy Speed Multiplyer",
	"enemy_health_multiplyer": "Enemy Health Multiplyer",
	"enemy_range_multiplyer": "Enemy Range Multiplyer",
	"enemy_projectile_speed_multiplyer": "Enemy Projectile Speed Multiplyer",
	"enemy_damage_multiplyer": "Enemy Damage Multiplyer",
	"enemy_spawn_rate": "Enemy Spawn Rate (in enemies per second)"
}

var DEFAULTS: Dictionary

# Reset System
func define_defaults():
	DEFAULTS = {
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
		"projectile_bounces": 0,
		"arrow_tracing": 0,
		"coin_retrieval_percentage": 0,
		
		"enemy_speed_multiplyer": 1,
		"enemy_health_multiplyer": 1,
		"enemy_range_multiplyer": 1,
		"enemy_projectile_speed_multiplyer": 1,
		"enemy_damage_multiplyer": 1,
		
		"enemies_killed": 0,
		"coins": 0,
		
		"enemy_spawn_rate": 2,
		"level_time": 30,
		"level": 1
	}

func _ready():
	define_defaults()

func reset():
	current_weapons.clear()
	current_weapons.append(base_weapon.duplicate(true))
	
	for var_name in DEFAULTS:
		set(var_name, DEFAULTS[var_name])

```
