extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})".format([data.name, data.rarity_text])
	
	stats.text = "Damage: {0}\n".format([data.damage])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])

func _on_sell_pressed() -> void:
	var index = 0
	for w in Stats.current_weapons:
		if w.name == data.name and data.cost == w.cost:
			Stats.current_weapons.remove_at(index)
			break
		index += 1
	
	Stats.coins += int(data.cost * (Stats.refund_rate / 100.0))
	get_parent().get_parent().redo_selling()
