extends HBoxContainer

func _ready() -> void:
	for i in range(Stats.num_of_upgrades):
		var instance = Scenes.upgrade_selection_helper.instantiate()
		instance.rendered_upgrade = Upgrades.get_random_upgrade()
		add_child(instance)

func selected_upgrade():
	get_tree().change_scene_to_packed(Scenes.shop)
