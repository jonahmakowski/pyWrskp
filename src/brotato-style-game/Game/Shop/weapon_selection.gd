extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats
@onready var buy: Button = %Buy

func _ready() -> void:
	image.texture = data.static_sprite
	
	if Stats.damage_multiplyer != 1:
		stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	else:
		stats.text = "Damage: {0}\n".format([data.damage])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	
	Messanger.MONEY_CHANGE.connect(can_buy)
	Messanger.WEAPON_CHANGE.connect(can_buy)
	can_buy()

func can_buy() -> void:
	if Stats.coins < data.cost or (len(Stats.current_weapons) >= Stats.max_weapons and not can_merge()):
		buy.disabled = true
	else:
		buy.disabled = false

func _on_buy_pressed() -> void:
	if Stats.coins < data.cost:
		return
	
	if len(Stats.current_weapons) < Stats.max_weapons:
		Stats.coins -= data.cost
		Stats.current_weapons.append(data.duplicate(true))
		
		Messanger.REDO_SELLING.emit()
		
		queue_free()
	elif len(Stats.current_weapons) == Stats.max_weapons:
		Stats.coins -= data.cost
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				w.merge_factor += 1
				Messanger.REDO_SELLING.emit()
				queue_free()
				break

func can_merge():
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			return true
	return false
