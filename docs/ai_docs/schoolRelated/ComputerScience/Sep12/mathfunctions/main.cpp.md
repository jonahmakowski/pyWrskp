# Documentation for src/schoolRelated/ComputerScience/Sep12/mathfunctions/main.cpp

# AI Summary
This file contains three functions that perform mathematical operations on floating-point numbers. The floor function returns the largest integer less than or equal to the input value, the ceil function returns the smallest integer greater than or equal to the input value, and the round function returns the nearest integer to the input value. The main function demonstrates the usage of these functions by printing the results of applying them to the number 5.7.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, the naming of the functions could be more descriptive, and the use of the printf function in the main function could be improved for better readability.
# Functions

## floor
### Explanation
This function takes a float as input and returns the largest integer less than or equal to the input value.
### Code
```c++
int floor(float x) {
    return (int)x;
}
```

## ceil
### Explanation
This function takes a float as input and returns the smallest integer greater than or equal to the input value.
### Code
```c++
int ceil(float x) {
    if ((int)x == x) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}
```

## round
### Explanation
This function takes a float as input and returns the nearest integer to the input value.
### Code
```c++
int round(float x) {
    if (x - (int)x < 0.5) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}
```
# Overall File Contents
```c++
#include <stdio.h>

int floor(float x) {
    return (int)x;
}

int ceil(float x) {
    if ((int)x == x) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}

int round(float x) {
    if (x - (int)x < 0.5) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}

int main() {
    printf("5.7 floored is %d\n", floor(5.7));
    printf("5.7 ceiled is %d\n", ceil(5.7));
    printf("5.7 rounded is %d\n", round(5.7));
}

```
