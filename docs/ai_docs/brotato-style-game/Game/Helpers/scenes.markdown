# Documentation for src/brotato-style-game/Game/Helpers/scenes.gd

# AI Summary
This file is a collection of exported variables in a Godot script. It extends the Node class and declares several PackedScene variables that are marked with the @export annotation. These variables are likely used to reference different scenes in the game, such as enemy arrows, start screen, level 1, death screen, enemy, player arrow, player weapon, coin, upgrade selection, and upgrade selection helper. The file does not contain any functions, only variable declarations.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is well-structured and follows Godot's conventions. The variable names are descriptive and the use of @export annotation is appropriate. However, the lack of functions and comments could be improved for better readability and maintainability.
# Functions
# Overall File Contents
```gdscript
extends Node

@export var enemy_arrow: PackedScene
@export var start_screen: PackedScene
@export var level1: PackedScene
@export var death_screen: PackedScene
@export var enemy: PackedScene
@export var player_arrow: PackedScene
@export var player_weapon: PackedScene
@export var coin: PackedScene
@export var upgrade_selection: PackedScene
@export var upgrade_selection_helper: PackedScene

```
