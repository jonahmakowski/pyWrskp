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
