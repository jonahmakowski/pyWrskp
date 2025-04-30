# Documentation for src/godot/platformer/scripts/character.gd

# Character Movement Script Documentation

## Overview

This script is designed for a character movement system in a 2D game environment. It handles basic movement, jumping, and animation states using the Godot Engine. The character can move left and right, jump, and change animations based on its state (idle, running, jumping).

## Table of Contents

- [Constants](#constants)
- [Functions](#functions)
  - [_physics_process](#_physics_process)
- [Example Usage](#example-usage)

## Constants

### SPEED
- **Description**: The speed at which the character moves horizontally.
- **Type**: `float`
- **Value**: `300.0`

### JUMP_VELOCITY
- **Description**: The initial velocity applied to the character when it jumps.
- **Type**: `float`
- **Value**: `-400.0`

## Functions

### _physics_process

**Description**: This function is called every physics frame. It handles the character's movement, jumping, and animation state changes.

**Parameters**:
- `delta` (`float`): The time elapsed since the last frame.

**Returns**: `void`

### Example Usage

```gdscript
extends CharacterBody2D

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

func _physics_process(delta: float) -> void:
    # Add the gravity.
    if not is_on_floor():
        velocity += get_gravity() * delta

    # Handle jump.
    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = JUMP_VELOCITY

    if not is_on_floor():
        $AnimatedSprite2D.play('jump')

    # Get the input direction and handle the movement/deceleration.
    # As good practice, you should replace UI actions with custom gameplay actions.
    var direction := Input.get_axis("move_left", "move_right")
    if direction:
        velocity.x = direction * SPEED
        $AnimatedSprite2D.set_flip_h(true if direction == -1 else false)
        if is_on_floor(): $AnimatedSprite2D.play('run')
    else:
        velocity.x = move_toward(velocity.x, 0, SPEED)
        if is_on_floor():
            $AnimatedSprite2D.play('idle')

    move_and_slide()
```

## Detailed Function Descriptions

### _physics_process

**Description**: This function is called every physics frame. It handles the character's movement, jumping, and animation state changes.

**Parameters**:
- `delta` (`float`): The time elapsed since the last frame.

**Returns**: `void`

**Detailed Explanation**:
- **Gravity**: If the character is not on the floor, gravity is applied to the character's velocity.
- **Jumping**: If the "jump" action is pressed and the character is on the floor, the character's vertical velocity is set to `JUMP_VELOCITY`.
- **Animation**: If the character is not on the floor, the "jump" animation is played. Otherwise, the character's horizontal movement direction is determined, and the appropriate animation ("run" or "idle") is played based on the direction.
- **Movement**: The character's horizontal velocity is set based on the input direction. If there is no input, the character's horizontal velocity is gradually reduced to zero.
- **Move and Slide**: The `move_and_slide()` function is called to move the character and handle collisions.

## Example Usage

To use this script, attach it to a `CharacterBody2D` node in your Godot scene. Ensure that the node has an `AnimatedSprite2D` child node with the appropriate animations ("idle", "run", "jump") set up.

```gdscript
# Attach this script to a CharacterBody2D node
extends CharacterBody2D

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

func _physics_process(delta: float) -> void:
    # Add the gravity.
    if not is_on_floor():
        velocity += get_gravity() * delta

    # Handle jump.
    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = JUMP_VELOCITY

    if not is_on_floor():
        $AnimatedSprite2D.play('jump')

    # Get the input direction and handle the movement/deceleration.
    # As good practice, you should replace UI actions with custom gameplay actions.
    var direction := Input.get_axis("move_left", "move_right")
    if direction:
        velocity.x = direction *