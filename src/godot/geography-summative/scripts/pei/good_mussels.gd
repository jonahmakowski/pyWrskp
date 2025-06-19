extends Label

func _process(_delta: float):
	text = "Yellow Mussels Collected: " + str($"../../../..".score_of_yellow) + "/" + str($"../../../..".yellow_required)
