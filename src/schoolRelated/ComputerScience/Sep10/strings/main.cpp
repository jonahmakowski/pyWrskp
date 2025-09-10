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
