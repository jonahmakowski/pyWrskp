# Documentation for src/brotato-style-game/Game/UpgradeSystem/stat_changes_class.gd

# AI Summary
This file defines a class called stat_changes that extends the Resource class. It has three exported variables: stat (a string), change_by (a float), and type (a string with an enum of "+" or "*"). The class is designed to handle changes to statistics, with the type variable determining whether the change is additive or multiplicative.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is well-structured and follows Godot's conventions. The class name and variable names are descriptive. However, the code could be more concise by removing unnecessary comments or simplifying the enum definition.
# Functions
# Overall File Contents
```gdscript
class_name stat_changes
extends Resource

@export var stat: String
@export var change_by: float
@export_enum("+", "*") var type: String

```
