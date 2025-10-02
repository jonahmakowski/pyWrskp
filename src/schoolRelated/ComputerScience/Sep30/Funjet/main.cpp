// Jonah Makowski - Funjet Project - September 30, 2025

#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    // Question 1
    int value = 100;

    while (value >= 10) {
        printf("Enter a value: ");
        scanf("%d", &value);
    }
    printf("You entered a value less than 10: %d\n", value);

    // Question 2
    char value_char = 'y';

    while (value_char == 'y') {
        printf("Do you want to continue? (y/n): ");
        scanf(" %c", &value_char);
    }

    printf("You chose to stop.\n");

    // Question 3
    value = -1;

    while (value % 2 != 0 || value < 0) {
        printf("Enter a value: ");
        scanf("%d", &value);
    }

    printf("You entered a positive, even value: %d\n", value);

    // Question 4
    char name[50];
    while (strcmp(name, "fred") != 0) {
        printf("Enter your name: ");
        scanf("%s", name);
        
        if (strcmp(name, "fred") != 0) {
            printf("That's not the correct name. Try again.\n");
        }
    }

    // Question 5
    char input[50];
    while (true) {
        printf("Enter a string (or 'exit' to quit): ");
        scanf("%s", input);
        
        if (strcmp(input, "exit") == 0) {
            break;
        }
        
        printf("You entered: %s\n", input);
    }

    // Question 6
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    for (int i = 0; i < age; i++) {
        printf("I am sooooo happy!!\n");
    }

    // Question 7
    int max = -100000;
    int min = 100000;
    int number;
    for (int i = 0; i < 9; i++) {
        printf("Enter a number: ");
        scanf("%d", &number);
        
        if (number > max) {
            max = number;
        }
        if (number < min) {
            min = number;
        }
    }

    printf("Max: %d, Min: %d, Range: %d\n", max, min, max - min);

    // Question 8
    for (int i = 0; i < 2; i++) {
        printf("Multiplication Table:\n");
        printf("\t\t%3s\t%3s\t%3s\t%3s\t%3s\t%3s\t%3s\t%3s\t%3s\t%3s\n\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10");
        for (int j = 1; j <= 10; j++) {
            printf("%3d\t\t", j);
            for (int k = 1; k <= 10; k++) {
                printf("%3d\t", j * k);
            }
            printf("\n");
        }
    }

    // Question 9
    char choice;
    while (true) {
        printf("Enter a string: ");
        scanf("%s", input);
        for (int i = 0; i <= strlen(input) - 1; i++) {
            printf("%c", input[i]);
            if (i < strlen(input) - 1) {
                printf("*");
            }
        }

        printf("\nDo you want to enter another string? (y/n): ");
        scanf(" %c", &choice);
        if (choice != 'y') {
            break;
        }
    }

    // Question 10
    printf("Enter a number: ");
    scanf("%d", &number);
    for (int i = 1; i <= number; i++) {
        if (i * i < number) {
            printf("%d\n", i * i);
        } else {
            break;
        }
    }

    // Question 11
    number = -1;
    while (number % 2 != 0 || number < 0) {
        printf("Enter a number: ");
        scanf("%d", &number);
    }

    for (int i = 0; i <= (number/2); i += 1) {
        printf("a string half as many times as the input\n");
    }

    // Question 12
    printf("Enter a number: ");
    scanf("%d", &number);

    for (int i = 0; i <= number; i++) {
        if (pow(2, i) < number) {
            printf("%d\n", (int)pow(2, i));
        } else {
            break;
        }
    }
}
