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
