#include <stdio.h>
#include <math.h>

int main() {
    float item1, item2, item3, total, tax, grandtotal;
    const float TAXRATE = 0.13; // 13% tax
    
    printf("Enter the prices of three items (in dollars and cents), with spaces between:\n");
    scanf("%f %f %f", &item1, &item2, &item3);
    
    total = item1 + item2 + item3;
    tax = total * TAXRATE;
    grandtotal = total + tax;
    
    printf("Item 1: $%.2f\n", item1);
    printf("Item 2: $%.2f\n", item2);
    printf("Item 3: $%.2f\n", item3);
    printf("Sub-Total: $%.2f\n", total);
    printf("Tax: $%.2f\n", tax);
    printf("Total: $%.2f\n", grandtotal);
}