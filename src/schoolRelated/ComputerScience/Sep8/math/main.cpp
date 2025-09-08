#include <math.h>
#include <stdio.h>

int main() {
    int height;
    printf("Enter your height in cm: ");
    scanf("%d", &height);

    if (height >= 137)
        printf("You are tall enough to ride the roller coaster!\n");
    else
        printf("You are not tall enough to ride the roller coaster.\n");
    
    bool even = (height % 2 == 0);
    if (even)
        printf("Your height is even.\n");
    else
        printf("Your height is odd.\n");
    
    bool multiple_of_3 = (height % 3 == 0);
    if (multiple_of_3)
        printf("Your height is a multiple of 3.\n");
    else
        printf("Your height is not a multiple of 3.\n");
    
    if (height >= 0)
        printf("The root of your height is %.2f\n", sqrt(height));
    else
        printf("there is no real square root for a negative number\n");

    return 0;
}
