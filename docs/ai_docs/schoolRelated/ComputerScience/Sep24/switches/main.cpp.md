# Documentation for src/schoolRelated/ComputerScience/Sep24/switches/main.cpp

# AI Summary
The `main` function is a simple command-line program that calculates the total cost of fuel based on user input for fuel type and quantity. It demonstrates basic input/output operations, character manipulation (to_upper), and a switch statement for conditional logic. The code is straightforward and easy to understand.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional, concise, and clearly demonstrates the use of a switch statement. It handles invalid input gracefully by printing an error message. For C++, using `<iostream>` (cin/cout) instead of `<stdio.h>` (printf/scanf) would be more conventional, but given the simplicity, `<stdio.h>` is acceptable. Variable names are clear.
# Functions

## main
### Explanation
This function prompts the user to enter a fuel type and the number of liters purchased. It then uses a switch statement to calculate and display the total cost based on the entered fuel type and a predefined price per liter for premium, super, regular, and diesel fuels. It also converts the fuel type input to uppercase for case-insensitive comparison and handles invalid fuel type inputs.
### Code
```c
#include <stdio.h>
#include <ctype.h>

int main() {
    float liters_purchased = 0.0;
    char fuel_type;

    printf("Enter the fuel type (P for premium, S for super, R for regular, D for diesel): ");
    scanf(" %c", &fuel_type);
    fuel_type = toupper(fuel_type);

    printf("Enter the number of litres purchased: ");
    scanf("%f", &liters_purchased);

    switch (fuel_type) {
        case 'P':
            printf("Total cost for premium fuel: $%.3f\n", liters_purchased * 1.583);
            break;
        case 'S':
            printf("Total cost for super fuel: $%.3f\n", liters_purchased * 1.435);
            break;
        case 'R':
            printf("Total cost for regular fuel: $%.3f\n", liters_purchased * 1.383);
            break;
        case 'D':
            printf("Total cost for diesel fuel: $%.3f\n", liters_purchased * 1.024);
            break;
        default:
            printf("Invalid fuel type (%c) entered.\n", fuel_type);
            break;
    }
}식이
```
# Overall File Contents
```c
#include <stdio.h>
#include <ctype.h>

int main() {
    float liters_purchased = 0.0;
    char fuel_type;

    printf("Enter the fuel type (P for premium, S for super, R for regular, D for diesel): ");
    scanf(" %c", &fuel_type);
    fuel_type = toupper(fuel_type);

    printf("Enter the number of litres purchased: ");
    scanf("%f", &liters_purchased);

    switch (fuel_type) {
        case 'P':
            printf("Total cost for premium fuel: $%.3f\n", liters_purchased * 1.583);
            break;
        case 'S':
            printf("Total cost for super fuel: $%.3f\n", liters_purchased * 1.435);
            break;
        case 'R':
            printf("Total cost for regular fuel: $%.3f\n", liters_purchased * 1.383);
            break;
        case 'D':
            printf("Total cost for diesel fuel: $%.3f\n", liters_purchased * 1.024);
            break;
        default:
            printf("Invalid fuel type (%c) entered.\n", fuel_type);
            break;
    }
}

```
