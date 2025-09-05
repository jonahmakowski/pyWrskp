extends TextureRect

var card: Card
var mouse_in = false
var selected = false
var move = true

func setup(c: Card, m=true, s=false):
	card = c
	move = m
	selected = s

func _ready() -> void:
	texture = card.sprite
	if selected:
		position.y -= 75

func _process(_delta: float) -> void:
	if move and Globals.card_select_enabled:
		if mouse_in and Input.is_action_just_pressed("select_card"):
			if selected == false:
				position.y -= 75
				selected = true
			else:
				position.y += 75
				selected = false
	
	if Input.is_action_just_pressed("reset"):
		if selected:
			position.y += 75
			selected = false

func _on_mouse_entered() -> void:
	mouse_in = true

func _on_mouse_exited() -> void:
	mouse_in = false
