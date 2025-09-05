extends Node

# Global Scenes
@export var main_menu: PackedScene
@export var options_menu: PackedScene

# President Scenes
@export var president_scene: PackedScene
@export var president_card_scene: PackedScene
@export var president_round_scene: PackedScene
@export var president_score_scene: PackedScene
@export var president_menu: PackedScene

var num_of_players = 3
var rankings = []
var president_hands = []
var president_scores = []
var style = 0
var card_select_enabled = true
var president_bum = -1

var default_options = {"style": 0}
var current_options = {}
