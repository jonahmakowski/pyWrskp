extends Label

func _ready() -> void:
	Messanger.MONEY_CHANGE.connect(update_text)
	update_text()

func update_text():
	text = "Coins: {0}".format([Stats.coins])
