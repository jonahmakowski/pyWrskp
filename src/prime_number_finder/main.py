current_number = 1


def is_prime(n: int) -> bool:
    current = 2
    while True:
        if current * current >= n:
            return True
        if n % current == 0:
            return False
        current += 1


while True:
    if is_prime(current_number):
        print(f"{current_number} is a prime number.")
    current_number += 1
