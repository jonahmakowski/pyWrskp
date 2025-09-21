# Documentation for src/brotato-style-game/Game/Shop/weapon_selection.gd

# AI Summary
This GDScript file (`weapon_selection.gd`) defines a control node that represents a weapon item in a game's shop. It displays the weapon's image, name, rarity, and statistics, allowing players to purchase it. The script manages the buy button's availability based on the player's current coins and weapon inventory capacity. Upon a successful purchase, it updates the player's currency and inventory, and refreshes the shop display.

The AI gave it a general rating of 9/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is well-structured and easy to understand, utilizing Godot's conventions for functions like `_ready` and `_process`. Variable names are clear, and type hints are used. The logic for purchasing and updating the UI is sound. However, the repeated `stats.text +=` for building the stats string could be more concise by formatting the entire string at once. Additionally, using `get_parent().get_parent().redo_selling()` creates a tight coupling; a custom signal for shop updates would offer more flexibility and robustness.
# Functions

## _ready
### Explanation
This function initializes the weapon selection UI. It displays the weapon's image, name, rarity, and detailed statistics (damage, range, cooldown, melee, and cost). It also disables the buy button if the player does not have enough coins to purchase the weapon.
### Code
```gdscript
func _ready() -> void:
	image.texture = data.static_sprite

	title.text = "{0} ({1})".format([data.name, data.rarity_text])

	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])	stats.text += "Cost: {0}\n".format([data.cost])

	if Stats.coins < data.cost:
		buy.disabled = true
```

## _process
### Explanation
This function is called every frame and continuously updates the state of the buy button. It disables the button if the player does not have enough coins or if their weapon inventory is full (reached `Stats.max_weapons`). Otherwise, the buy button is enabled.
### Code
```gdscript
func _process(_delta: float) -> void:
	if Stats.coins < data.cost or len(Stats.current_weapons) >= Stats.max_weapons:
		buy.disabled = true
	else:
		buy.disabled = false
```

## _on_buy_pressed
### Explanation
This function is executed when the "Buy" button is pressed. It first checks if the player has sufficient coins. If not, the function returns. If the player has enough coins and space in their inventory, it deducts the weapon's cost from the player's coins, adds a duplicate of the weapon to their current weapons list, signals the shop to refresh its selling display, and then removes this weapon selection UI element.
### Code
```gdscript
func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return

	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))

		get_parent().get_parent().redo_selling()

		queue_free()
```
# Overall File Contents
```gdscript
extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats
@onready var buy: Button = %Buy

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost:
		buy.disabled = true

func _process(_delta: float) -> void:
	if Stats.coins < data.cost or len(Stats.current_weapons) >= Stats.max_weapons:
		buy.disabled = true
	else:
		buy.disabled = false

func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		get_parent().get_parent().redo_selling()
		
		queue_free()

```
