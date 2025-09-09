# Documentation for src/schoolRelated/ComputerScience/Sep5/snoppy/main.cpp

# AI Summary
The program calculates the Body Mass Index (BMI) based on user-provided age, height, and weight. It then categorizes the BMI into Underweight, Normal, Overweight, or Obese and prints all the collected and calculated information in a formatted table.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional and straightforward, achieving its stated purpose. The variable names are clear, and comments explain sections of the code. However, it's a single `main` function, which isn't ideal for larger programs; breaking down logic into smaller functions would improve modularity and readability. The BMI calculation could also be slightly more robust by explicitly casting `height` to a float earlier to avoid potential integer division issues if `height / 100` resulted in 0 for small heights (though not an issue here with typical human heights). The use of `scanf` and `printf` is standard for C, but error checking for `scanf`'s return value is omitted, which could lead to unexpected behavior if the user inputs non-numeric data.
# Functions

## main
### Explanation
This function prompts the user for age, height (in cm), and weight (in kg). It then calculates the Body Mass Index (BMI) using the formula weight / (height in meters * height in meters). Finally, it prints a formatted table displaying the age, height, weight, calculated BMI, and a category (Underweight, Normal, Overweight, or Obese) based on the BMI value.
### Code
```c
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
    printf("%3d\t%10d\t%10.1f\t%8.2f\t", age, height, weight, bmi);

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
```
# Overall File Contents
```c
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
    printf("%3d\t%10d\t%10.1f\t%8.2f\t", age, height, weight, bmi);

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

```
