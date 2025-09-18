# Documentation for src/brotato-style-game/Game/UIScenes/stats_display.gd

# AI Summary
This file defines a PanelContainer that displays game statistics. It toggles visibility based on user input and updates the displayed stats. The game tree is paused when the stats display is visible.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are areas where it could be more concise and adhere more closely to conventions.
# Functions

## _ready
### Explanation
This function sets the process mode to always process.
### Code
```gdscript
func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
```

## _process
### Explanation
This function toggles the visibility of the stats display and updates the stats shown. It also pauses the game tree when the stats display is visible.
### Code
```gdscript
func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("show_stats"):
		if not visible:
			visible = true
			get_tree().paused = true
		else:
			visible = false
			get_tree().paused = false
	
	for child in stats_here.get_children():
		child.queue_free()
	
	for stat in Stats.DEFAULTS.keys():
		var t = "{0}: {1}".format([stat, str(Stats.get(stat))])
		var instance = Label.new()
		instance.text = t
		stats_here.add_child(instance)
```
# Overall File Contents
```gdscript
extends PanelContainer

@onready var stats_here: VBoxContainer = %StatsHere

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("show_stats"):
		if not visible:
			visible = true
			get_tree().paused = true
		else:
			visible = false
			get_tree().paused = false
	
	for child in stats_here.get_children():
		child.queue_free()
	
	for stat in Stats.DEFAULTS.keys():
		var t = "{0}: {1}".format([stat, str(Stats.get(stat))])
		var instance = Label.new()
		instance.text = t
		stats_here.add_child(instance)

```
