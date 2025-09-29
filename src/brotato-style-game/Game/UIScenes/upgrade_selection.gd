extends Control

@onready var upgrade_box: HBoxContainer = %UpgradeBox

func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		upgrade_box.add_child(instance)
