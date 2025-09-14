# Documentation for src/brotato-style-game/Game/Levels/start_screen.gd

# AI Summary
The file contains a single function that handles the start button press event, resetting game statistics and transitioning to the first level.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional and concise, but there is room for improvement in adhering to Python conventions.
# Functions

## _on_start_pressed
### Explanation
This function is triggered when the start button is pressed. It resets the game statistics and changes the scene to the first level.
### Code
```godot
func _on_start_pressed() -> void:
	Stats.reset()
	get_tree().change_scene_to_packed(Scenes.level1)
```
# Overall File Contents
```godot
extends Control

func _on_start_pressed() -> void:
	Stats.reset()
	get_tree().change_scene_to_packed(Scenes.level1)

```
