add_to = int(input("Enter a number to add: "))
mult_to = int(input("Enter a number to multiply: "))

search_limit = max(abs(add_to), abs(mult_to)) + 10

for i in range(-search_limit, search_limit):
    for j in range(-search_limit, search_limit):
        if i + j == add_to and i * j == mult_to:
            print(f"Found numbers: {i} and {j}")
            break
