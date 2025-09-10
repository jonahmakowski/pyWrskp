# Documentation for src/schoolRelated/ComputerScience/Sep10/strings/main.cpp

# AI Summary
The program is a simple C++ console application that collects three pieces of information (name, quest, favorite color) from the user and then prints them back in a formatted string. It demonstrates basic input/output operations using C-style I/O functions like scanf and fgets.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 1/10

The reason for the AI's rating is:

The provided code is written in C++, not Python. Therefore, it does not adhere to Python standards and conventions.
# Functions

## main
### Explanation
This function prompts the user for their name, quest, and favorite color, then displays the collected information back to the user. It uses scanf for name and color, and fgets for the quest to handle spaces. It includes getchar() to consume the newline character after the first scanf and null-terminates the quest string after fgets to remove the trailing newline.
### Code
```c++
int main() {
    char name[20];
    char quest[100];
    char color[20];

    printf("Enter your name:\n");
    scanf("%19s", name);
    getchar();

    printf("Enter your quest:\n");
    fgets(quest, 100, stdin);
    quest[strlen(quest) - 1] = '\0';

    printf("Enter your favorite color:\n");
    scanf("%19s", color);

    printf("Ah, so your name is %s, your quest is %s, and your favorite color is %s.\n", name, quest, color);
}
```
# Overall File Contents
```c++
// Jonah Makowski - Sep 10, 2025
// Simple program to get user input and display it back

#include <stdio.h>
#include <string.h>

int main() {
    char name[20];
    char quest[100];
    char color[20];

    printf("Enter your name:\n");
    scanf("%19s", name);
    getchar();

    printf("Enter your quest:\n");
    fgets(quest, 100, stdin);
    quest[strlen(quest) - 1] = '\0';

    printf("Enter your favorite color:\n");
    scanf("%19s", color);

    printf("Ah, so your name is %s, your quest is %s, and your favorite color is %s.\n", name, quest, color);
}

```
