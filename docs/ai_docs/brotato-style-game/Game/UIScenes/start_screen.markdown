# Documentation for src/brotato-style-game/Game/UIScenes/start_screen.gd

# AI Summary
This file contains a single function that handles the start button press event. It resets the game statistics and transitions to the first level of the game.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and adheres to conventions. The function name is descriptive, and the code is concise.
# Functions

## _on_start_pressed
### Explanation
This function is triggered when the start button is pressed. It resets the game statistics and changes the scene to the first level.
### Code
```gdscript
func _on_start_pressed() -> void:
	Stats.reset()
	get_tree().change_scene_to_packed(Scenes.level1)
```
# Overall File Contents
```gdscript
extends Control

func _on_start_pressed() -> void:
	Stats.reset()
	get_tree().change_scene_to_packed(Scenes.level1)

```
