# Documentation for src/trigSolver/main.py

# AI Summary
This Python script calculates the missing values of a right-angled triangle given any three of the four values: the hypotenuse, the opposite side, the adjacent side, or the angle. It prompts the user to input these values and then uses trigonometric functions to compute the missing values. The script handles cases where some values are not provided by the user.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is generally well-structured and easy to follow. It adheres to Python conventions, such as using descriptive variable names and proper indentation. The use of trigonometric functions is appropriate for the task. However, the code could be more concise by using a loop or a dictionary to handle the different cases of missing values.
# Functions

## parse_input
### Explanation
This function takes a string input and attempts to convert it to a float. If the input string is empty, it returns None. If the conversion fails (raises a ValueError), it also returns None.
### Code
```python
def parse_input(input_str):
    if input_str == "":
        return None
    try:
        return float(input_str)
    except ValueError:
        return None
```
# Overall File Contents
```python
import math

print("If you don't have a value, simply press enter.")

hypotenuse_input = input("Enter the length of the hypotenuse: ")
opposite_input = input("Enter the length of the opposite side: ")
adjacent_input = input("Enter the length of the adjacent side: ")
angle_input = input("Enter the angle in degrees: ")

def parse_input(input_str):
    if input_str == "":
        return None
    try:
        return float(input_str)
    except ValueError:
        return None

hypotenuse = parse_input(hypotenuse_input)
opposite = parse_input(opposite_input)
adjacent = parse_input(adjacent_input)
angle = parse_input(angle_input)

if angle is None:
    if opposite is not None and adjacent is not None:
        angle = math.degrees(math.atan(opposite / adjacent))
    elif opposite is not None and hypotenuse is not None:
        angle = math.degrees(math.asin(opposite / hypotenuse))
    elif adjacent is not None and hypotenuse is not None:
        angle = math.degrees(math.acos(adjacent / hypotenuse))

if opposite is None:
    if angle is not None and adjacent is not None:
        opposite = math.tan(math.radians(angle)) * adjacent
    elif angle is not None and hypotenuse is not None:
        opposite = math.sin(math.radians(angle)) * hypotenuse
    elif adjacent is not None and hypotenuse is not None:
        opposite = math.sqrt(hypotenuse**2 - adjacent**2)

if hypotenuse is None:
    if angle is not None and opposite is not None:
        hypotenuse = opposite / math.sin(math.radians(angle))
    elif angle is not None and adjacent is not None:
        hypotenuse = adjacent / math.cos(math.radians(angle))
    elif opposite is not None and adjacent is not None:
        hypotenuse = math.sqrt(opposite**2 + adjacent**2)

if adjacent is None:
    if angle is not None and opposite is not None:
        adjacent = opposite / math.tan(math.radians(angle))
    elif angle is not None and hypotenuse is not None:
        adjacent = hypotenuse * math.cos(math.radians(angle))
    elif opposite is not None and hypotenuse is not None:
        adjacent = math.sqrt(hypotenuse**2 - opposite**2)

print("The adjacent side is:", adjacent)
print("The opposite side is:", opposite)
print("The hypotenuse is:", hypotenuse)
print("The angle is:", angle)
```
