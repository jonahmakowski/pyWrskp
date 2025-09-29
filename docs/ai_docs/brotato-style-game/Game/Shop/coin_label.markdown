# Documentation for src/brotato-style-game/Game/Shop/coin_label.gd

# AI Summary
This file defines a Label node that displays the current number of coins. It connects to a MONEY_CHANGE signal to update the text whenever the number of coins changes.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and follows the conventions of the Godot engine. The functionality is clear and concise.
# Functions

## _ready
### Explanation
This function is called when the node is ready. It connects the update_text function to the MONEY_CHANGE signal and calls update_text to initialize the text.
### Code
```gdscript
func _ready() -> void:
	Messanger.MONEY_CHANGE.connect(update_text)
	update_text()
```

## update_text
### Explanation
This function updates the text of the label to display the current number of coins.
### Code
```gdscript
func update_text():
	text = "Coins: {0}".format([Stats.coins])
```
# Overall File Contents
```gdscript
extends Label

func _ready() -> void:
	Messanger.MONEY_CHANGE.connect(update_text)
	update_text()

func update_text():
	text = "Coins: {0}".format([Stats.coins])

```
