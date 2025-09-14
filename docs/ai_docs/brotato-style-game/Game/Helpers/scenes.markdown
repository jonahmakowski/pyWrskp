# Documentation for src/brotato-style-game/Game/Helpers/scenes.gd

# AI Summary
This file is a simple script that extends the Node class and declares several exported variables of type PackedScene. These variables are used to reference different scenes in the game, such as enemy arrows, start screen, level 1, death screen, enemy, player arrows, and coins. The script does not contain any functions or complex logic, making it a straightforward and concise piece of code.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is well-structured and easy to read, with clear variable names and proper use of the @export annotation. However, it lacks any functions or complex logic, which could be improved to enhance its functionality.
# Functions
# Overall File Contents
```godot
extends Node

@export var enemy_arrow: PackedScene
@export var start_screen: PackedScene
@export var level1: PackedScene
@export var death_screen: PackedScene
@export var enemy: PackedScene
@export var player_arrow: PackedScene
@export var coin: PackedScene

```
