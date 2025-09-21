# Documentation for src/brotato-style-game/Game/Player/weapon_resource.gd

# AI Summary
This file defines a weapon resource class in Godot. It includes various properties such as weapon type, style, damage, range, cooldown, melee status, sprite, cost, and rarity. The class also includes a method to set the rarity text and weight based on the rarity value.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and follows Godot conventions. However, there are some minor issues with variable naming and some lines are missing in the provided code.
# Functions

## set_rarity
### Explanation
This function sets the rarity text and weight of the weapon based on its rarity value. It uses the Stats.RARITY_TO_TEXT and Stats.RARITY_TO_WEIGHT dictionaries to map the rarity value to the corresponding text and weight.
### Code
```gdscript
func set_rarity():
	rarity_text = Stats.RARITY_TO_TEXT[rarity]
	weight = Stats.RARITY_TO_WEIGHT[rarity]
```
# Overall File Contents
```gdscript
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

```
