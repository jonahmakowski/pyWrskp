# Documentation for src/brotato-style-game/Game/Helpers/scenes.gd

# AI Summary
This file is a collection of exported variables in the Godot game engine, specifically for scenes. It includes various scene types such as enemies, players, shop items, miscellaneous scenes, upgrades, and currencies. Each variable is annotated with an @export_group directive to organize them into logical groups. The file does not contain any functions, only variable declarations.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-organized and follows Godot's conventions for exporting variables. The use of @export_group directives helps in categorizing the variables effectively. The code is concise and easy to understand.
# Functions
# Overall File Contents
```gdscript
extends Node

# Enemies
@export_group("Enemies")
@export var enemy_arrow: PackedScene
@export var enemy: PackedScene

# Players
@export_group("Players")
@export var player_arrow: PackedScene
@export var player_weapon: PackedScene

# Shop
@export_group("Shop")
@export var shop_weapon_selling: PackedScene
@export var shop_weapon_selection: PackedScene
@export var shop: PackedScene

# Misc Scenes
@export_group("Misc")
@export var start_screen: PackedScene
@export var level1: PackedScene
@export var death_screen: PackedScene

# Upgrades
@export_group("Upgrades")
@export var upgrade_selection: PackedScene
@export var upgrade_selection_helper: PackedScene

# Currencies
@export_group("Currencies")
@export var coin: PackedScene

```
