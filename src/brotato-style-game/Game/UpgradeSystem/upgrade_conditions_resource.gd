extends Resource
class_name upgrade_conditions

@export var stat: String
@export_enum("Greater Than", "Less Than", "Equal To", "Greater Than or Equal To", "Less Than or Equal To") var type: String
@export var opposite: bool
@export var value: float

func check_condition():
	var current_value = Stats.get(stat)
	
	if current_value == null:
		push_error("Stat '{0}' does not exist.".format([stat]))
		return false
	
	if not opposite:
		if type == "Greater Than" and value > current_value:
			return true
		elif type == "Less Than" and value < current_value:
			return true
		elif type == "Equal To" and value == current_value:
			return true
		elif type == "Greater Than or Equal To" and value >= current_value:
			return true
		elif type == "Less Than or Equal To" and value <= current_value:
			return true
	else:
		if type == "Greater Than" and not value > current_value:
			return true
		elif type == "Less Than" and not value < current_value:
			return true
		elif type == "Equal To" and not value == current_value:
			return true
		elif type == "Greater Than or Equal To" and not value >= current_value:
			return true
		elif type == "Less Than or Equal To" and not value <= current_value:
			return true
	
	return false
