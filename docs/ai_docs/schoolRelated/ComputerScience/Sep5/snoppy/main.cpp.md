# Documentation for src/schoolRelated/ComputerScience/Sep5/snoppy/main.cpp

# AI Summary
This code is a simple C program that prompts the user for their age, height, and weight, then prints them in a formatted table.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 8/10

The reason for the AI's rating is:

The code is functional and concise, but could benefit from more comments and consistent formatting.
# Functions

## main
### Explanation
This function prompts the user for their age, height, and weight, then prints them in a formatted table.
### Code
```c
int main() {
    int age;
    int height;
    int weight;

    printf("How old are you?\n");
    scanf("%d", &age);

    printf("How tall are you (in cm)?\n");
    scanf("%d", &height);
    
    printf("How much do you weigh (in kg)?\n");
    scanf("%d", &weight);
    
    printf("Age\tHeight(cm)\tWeight(kg)\n");
    printf("---\t----------\t----------\n");
    printf("%3d\t%10d\t%10d\n", age, height, weight);
}
```
# Overall File Contents
```c
#include <stdio.h>

int main() {
    int age;
    int height;
    int weight;

    printf("How old are you?\n");
    scanf("%d", &age);

    printf("How tall are you (in cm)?\n");
    scanf("%d", &height);
    
    printf("How much do you weigh (in kg)?\n");
    scanf("%d", &weight);
    
    printf("Age\tHeight(cm)\tWeight(kg)\n");
    printf("---\t----------\t----------\n");
    printf("%3d\t%10d\t%10d\n", age, height, weight);
}

```
