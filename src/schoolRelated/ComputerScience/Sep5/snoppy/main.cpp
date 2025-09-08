/*
Jonah Makowski - Sep 5-8, 2024
This program gets the age, height and weight from the user, calculates the BMI, prints all the data, and categorizes the BMI.
*/

#include <stdio.h>

int main() {
    int age;
    int height;
    float weight;

    // Get the age
    printf("How old are you?\n");
    scanf("%d", &age);

    // Get the height in cm
    printf("How tall are you (in cm)?\n");
    scanf("%d", &height);
    
    // Get the weight in kg
    printf("How much do you weigh (in kg)?\n");
    scanf("%f", &weight);
    
    float bmi = weight / ((height / 100) * (height / 100)); // Calculate bmi weight / height in m squared

    // Print everything except the bmi category
    printf("Age\tHeight(cm)\tWeight(kg)\tBMI\t\tCategory\n");
    printf("---\t----------\t----------\t--------\t-----------\n");
    printf("%3d\t%10d\t%10.2f\t%8.2f\t", age, height, weight, bmi);

    // Choose the bmi using if/then (selection) statements
    if (bmi <= 18.4) {
        printf("Underweight\n");
    } else if ( 18.5 <= bmi && bmi <= 24.9) {
        printf("Normal\n");
    } else if (25.0 <= bmi && bmi <= 39.9) {
        printf("Overweight\n");
    } else {
        printf("Obese\n");
    }
}
