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
