extends VBoxContainer

var rendered_upgrade: upgrade

@onready var title: Label = %Title
@onready var image: TextureRect = %Image
@onready var description: Label = %Description

func _ready() -> void:
	title.text = rendered_upgrade.name + " ({0})".format([rendered_upgrade.rarity_text])
	
	if rendered_upgrade.has_icon:
		image.show()
		image.texture = rendered_upgrade.icon
	
	description.text = rendered_upgrade.desription

func _on_button_pressed() -> void:
	rendered_upgrade.apply()
	get_parent().selected_upgrade()
