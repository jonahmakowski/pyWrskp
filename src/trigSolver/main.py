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