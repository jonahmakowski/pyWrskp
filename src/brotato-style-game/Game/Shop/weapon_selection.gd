extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats
@onready var buy: Button = %Buy

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost:
		buy.disabled = true

func _process(_delta: float) -> void:
	if Stats.coins < data.cost or len(Stats.current_weapons) >= Stats.max_weapons:
		buy.disabled = true
	else:
		buy.disabled = false

func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		get_parent().get_parent().redo_selling()
		
		queue_free()
