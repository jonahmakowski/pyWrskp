extends Label

func _process(_delta: float):
	text = "White Mussels Collected: " + str($"../../../..".score_of_white) + "/" + str($"../../../..".max_of_white)
