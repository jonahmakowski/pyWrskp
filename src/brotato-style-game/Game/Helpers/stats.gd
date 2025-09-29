extends Node

# Player
var speed_multiplyer = 1
var current_health = 10
var max_health: int = 10
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

@onready var current_weapons: Array[weapon] = [base_weapon.duplicate(true)]:
	set(value):
		current_weapons = value
		Messanger.WEAPON_CHANGE.emit()

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

# Reset System
var DEFAULTS: Dictionary

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

# Increase difficulty for next level
func next_level():
	if enemy_spawn_rate > 1:
		enemy_spawn_rate -= 0.25
	elif enemy_spawn_rate > 0.05:
		enemy_spawn_rate -= 0.05
	elif enemy_spawn_rate > 0.005:
		enemy_spawn_rate -= 0.001
	
	enemy_health_multiplyer += 0.1
	enemy_damage_multiplyer += 0.1
	enemy_speed_multiplyer += 0.1
	enemy_projectile_speed_multiplyer += 0.05
	level_time += 2
	
	level += 1
