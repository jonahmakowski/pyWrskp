extends PanelContainer

@onready var stats_here: VBoxContainer = %StatsHere

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("show_stats"):
		if not visible:
			visible = true
			get_tree().paused = true
		else:
			visible = false
			get_tree().paused = false
	
	for child in stats_here.get_children():
		child.queue_free()
	
	for stat in Stats.DEFAULTS.keys():
		var t = "{0}: {1}".format([stat, Stats.get(stat)])
		var instance = Label.new()
		instance.text = t
		stats_here.add_child(instance)
