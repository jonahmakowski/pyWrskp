class_name weapon
extends Resource

@export var weapon_type: String
@export var weapon_style: String
@export var damage: float
@export var weapon_range: float
@export var cooldown: float
@export var melee: bool
@export var sprite: SpriteFrames
@export var cost: int
@export var rarity: int:
	set(value):
		rarity = value
		call_deferred("set_rarity")

var merge_factor: int = 1:
	set(value):
		merge_factor = value
		damage *= 2
		cost *= 2
		cooldown /= 1.5

var rarity_text: String
var weight: int
@export var static_sprite: AtlasTexture
@export var name: String

func set_rarity():
	rarity_text = Stats.RARITY_TO_TEXT[rarity]
	weight = Stats.RARITY_TO_WEIGHT[rarity]
