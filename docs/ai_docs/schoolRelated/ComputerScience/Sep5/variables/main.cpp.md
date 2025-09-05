# Documentation for src/schoolRelated/ComputerScience/Sep5/variables/main.cpp

# AI Summary
This program demonstrates the use of variables in C. It initializes variables for age, whole age, and initial, then prints formatted strings using these variables. The code is well-structured and easy to understand.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code follows C conventions well and is functional and concise.
# Functions

## main
### Explanation
The main function of the program. It initializes variables for age, whole age, and initial, then prints formatted strings using these variables.
### Code
```c
int main() {
    float age = 30.54;
    int age_whole = 30;
    char initial = 'J';
    printf("I am %.2f years old %d.\n", age, age_whole);
    printf("My initial is %c I'm %d years old.\n", initial, age_whole);
    printf("I am %-10.2f years old.\n", age);
    return 0;
}
```
# Overall File Contents
```c
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

```
