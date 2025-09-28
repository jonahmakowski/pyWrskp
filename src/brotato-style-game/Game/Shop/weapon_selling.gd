extends Control

var data: weapon
@onready var image: TextureRect = %Image
@onready var title: Label = %Title
@onready var stats: Label = %Stats
@onready var merge: Button = $VBoxContainer/Merge

func _ready() -> void:
	image.texture = data.static_sprite
	
	title.text = "{0} ({1})\n(Merge Factor: {2})".format([data.name, data.rarity_text, data.merge_factor])
	
	stats.text = "Damage: {0} -> {1}\n".format([data.damage, data.damage * Stats.damage_multiplyer])
	stats.text += "Range: {0}\n".format([data.weapon_range])
	stats.text += "Cooldown: {0}\n".format([data.cooldown])
	stats.text += "Melee: {0}\n".format([data.melee])
	stats.text += "Cost: {0}\n".format([data.cost])
	stats.text += "Refund Value: {0}".format([int(data.cost * (Stats.refund_rate / 100.0))])
	
	check_merge()
	Messanger.WEAPON_CHANGE.connect(check_merge)

func _on_sell_pressed() -> void:
	var index = 0
	for w in Stats.current_weapons:
		if w.name == data.name and data.cost == w.cost:
			Stats.current_weapons.remove_at(index)
			break
		index += 1
	
	Stats.coins += int(data.cost * (Stats.refund_rate / 100.0))
	get_parent().get_parent().get_parent().redo_selling()

func check_merge() -> void:
	if not can_merge():
		merge.disabled = true
	else:
		merge.disabled = false

func _on_merge_pressed() -> void:
	if can_merge():
		var merger: weapon
		var index = 0
		for w in Stats.current_weapons:
			if w.name == data.name and w.merge_factor == data.merge_factor:
				@warning_ignore("unassigned_variable")
				if merger == null:
					merger = w
				else:
					break
			index += 1
		
		Stats.current_weapons.remove_at(index)
		merger.merge_factor += 1
		Messanger.REDO_SELLING.emit()

func can_merge():
	var existing = 0
	for w in Stats.current_weapons:
		if w.name == data.name and w.merge_factor == data.merge_factor:
			existing += 1
			
			if existing == 2:
				return true
	return false
