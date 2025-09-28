# Documentation for src/brotato-style-game/Game/Shop/coin_label.gd

# AI Summary
This file is a script for a Label node in Godot. It updates the text of the label to display the current number of coins. The script connects to a MONEY_CHANGE signal to update the text whenever the number of coins changes.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. The naming conventions are clear and consistent. However, the code could be more concise by using a more direct approach to updating the text.
# Functions

## _ready
### Explanation
This function is called when the node is ready to be used. It connects the MONEY_CHANGE signal to the update_text function.
### Code
```gdscript
func _ready() -> void:
	Messanger.MONEY_CHANGE.connect(update_text)
```

## update_text
### Explanation
This function updates the text of the label to display the current number of coins.
### Code
```gdscript
func update_text():
	text = "Coins: {0}".format[Stats.coins]
```
# Overall File Contents
```gdscript
extends Label

func _ready() -> void:
	Messanger.MONEY_CHANGE.connect(update_text)

func update_text():
	text = "Coins: {0}".format([Stats.coins])

```
