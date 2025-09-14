# Documentation for src/brotato-style-game/Game/Levels/death.gd

# AI Summary
The file contains a single function that changes the scene to the start screen when a button is pressed.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional and concise, but the function name could be more descriptive.
# Functions

## _on_button_pressed
### Explanation
This function is triggered when a button is pressed. It changes the current scene to the start screen.
### Code
```gdscript
func _on_button_pressed() -> void:
	get_tree().change_scene_to_packed(Scenes.start_screen)
```
# Overall File Contents
```gdscript
extends Control

func _on_button_pressed() -> void:
	get_tree().change_scene_to_packed(Scenes.start_screen)

```
