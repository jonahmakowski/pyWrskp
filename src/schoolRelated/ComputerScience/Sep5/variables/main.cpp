/*
Jonah Makowski - Sep 5, 2024
This program demonstrates the use of variables in C
*/

#include <stdio.h>

int main() {
    float age = 30.54;
    int age_whole = 30;
    char initial = 'J';
    printf("I am %.2f years old %d.\n", age, age_whole);
    printf("My initial is %c I'm %d years old.\n", initial, age_whole);
    printf("I am %-10.2f years old.\n", age);
    return 0;
}
