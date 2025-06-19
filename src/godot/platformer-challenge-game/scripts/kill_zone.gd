extends Area2D

func _on_body_entered(body: Node2D) -> void:
	if body in get_tree().get_nodes_in_group("player"):
		Controller.kill_player()
	else:
		body.reset()
