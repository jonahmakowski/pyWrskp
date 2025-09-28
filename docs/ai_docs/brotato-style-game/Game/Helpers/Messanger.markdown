# Documentation for src/brotato-style-game/Game/Helpers/Messanger.gd

# AI Summary
This file is a Node class that defines several signals. The signals are used to communicate changes in money, weapons, and shop-specific actions. The file does not contain any functions, only signal definitions.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is well-structured and adheres to conventions. The signals are clearly defined and commented. The quality rating is slightly lower due to the lack of functions and the simplicity of the file.
# Functions
# Overall File Contents
```gdscript
extends Node

@warning_ignore("unused_signal")
signal MONEY_CHANGE
@warning_ignore("unused_signal")
signal WEAPON_CHANGE

# Shop Specific
@warning_ignore("unused_signal")
signal REDO_SELLING
@warning_ignore("unused_signal")
signal REDO_SELECTION

```
