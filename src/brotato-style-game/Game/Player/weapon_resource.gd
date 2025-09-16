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
		rarity_text = Stats.RARITY_TO_TEXT[rarity]
		weight = Stats.RARITY_TO_WEIGHT[rarity]
var rarity_text: String
var weight: int
