extends StaticBody2D

enum color_enum {WHITE, YELLOW}

@onready var pei_player: CharacterBody2D = $"../../PEIPlayer"
@export var color:color_enum

func init(c:String, pos:Vector2):
	position = pos
	color = color_enum[c]

func _ready():
	if color == 0:
		$White.show()
	else:
		$Yellow.show()

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body == self:
		return
	
	if color == 0: pei_player.score_of_white += 1
	else: pei_player.score_of_yellow += 1

	queue_free()
