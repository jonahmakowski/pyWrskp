# Documentation for src/schoolRelated/ComputerScience/Sep22/randomswitches/main.cpp

# AI Summary
This program generates a random number between 0 and 3 and then prints a different message based on the value of the random number. The program uses the standard library functions srand, rand, and printf.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, the use of magic numbers (3, 56, -5, 240) could be improved by using named constants. Also, the default case in the switch statement is not necessary because the random number is guaranteed to be between 0 and 3.
# Functions

## main
### Explanation
The main function of the program. It initializes the random number generator, generates a random number between 0 and 3, and then uses a switch statement to print a different message based on the value of the random number.
### Code
```c
int main() {
    srand(time(0));

    int choice = rand() % 4;

    switch (choice) {
        case 0:
            printf("Value is 3\n");
            break;
        case 1:
            printf("Value is 56\n");
            break;
        case 2:
            printf("Value is -5\n");
            break;
        case 3:
            printf("Value is 240\n");
            break;
        default:
            printf("You screwed something up.\n");
            break;
    }

    return 0;
}
```
# Overall File Contents
```c
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main() {
    srand(time(0));

    int choice = rand() % 4;

    switch (choice) {
        case 0:
            printf("Value is 3\n");
            break;
        case 1:
            printf("Value is 56\n");
            break;
        case 2:
            printf("Value is -5\n");
            break;
        case 3:
            printf("Value is 240\n");
            break;
        default:
            printf("You screwed something up.\n");
            break;
    }

    return 0;
}

```
