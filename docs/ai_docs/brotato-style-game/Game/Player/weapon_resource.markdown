# Documentation for src/brotato-style-game/Game/Player/weapon_resource.gd

# AI Summary
This file defines a weapon resource class in Godot, which is used to manage various properties of weapons in a game. The class includes properties for weapon type, style, damage, range, cooldown, melee status, sprite, cost, and rarity. The rarity property has a setter method that updates the rarity text and weight based on predefined values from the Stats class. The class extends the Resource class, which is a base class for data resources in Godot.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and adheres to Godot's conventions. The use of @export for variables that need to be editable in the editor is appropriate. The setter method for the rarity property is well-implemented and updates related properties correctly. The code is concise and focuses on the essential properties of a weapon resource.
# Functions
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
		rarity_text = Stats.RARITY_TO_TEXT[rarity]
		weight = Stats.RARITY_TO_WEIGHT[rarity]
var rarity_text: String
var weight: int

```
