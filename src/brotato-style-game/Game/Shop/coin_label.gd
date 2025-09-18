extends Label

func _process(_delta: float) -> void:
	text = "Coins: {0}".format([Stats.coins])
