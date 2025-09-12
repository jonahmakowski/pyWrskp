# Documentation for src/schoolRelated/ComputerScience/Sep12/math/main.cpp

# AI Summary
This C program calculates and prints the value of 3 raised to the power of numbers from 1 to 15.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is functional and concise, but it could benefit from better variable naming and comments for clarity.
# Functions

## main
### Explanation
This function calculates and prints the value of 3 raised to the power of numbers from 1 to 15.
### Code
```c
int main() {
    for (int value = 1; value <= 15; ++value) {
        printf("3 raised to the power of %d is %.1f\n", value, pow(3, value));
    }
}
```
# Overall File Contents
```c
#include <stdio.h>
#include <math.h>

int main() {
    for (int value = 1; value <= 15; ++value) {
        printf("3 raised to the power of %d is %.1f\n", value, pow(3, value));
    }
}
```
