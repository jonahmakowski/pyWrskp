#include <stdio.h>
#include <string.h>

int main() {
    char sin[10];
    int sin_as_int[10];
    int sum = 0;

    printf("Enter a the sin number: ");
    fgets(sin, sizeof(sin), stdin);
    sin[strcspn(sin, "\n")] = '\0';

    for (int i = 0; i < strlen(sin); i++) {
        sin_as_int[i] = sin[i] - '0';
    }

    sin_as_int[1] *= 2;
    sin_as_int[3] *= 2;
    sin_as_int[5] *= 2;
    sin_as_int[7] *= 2;

    for (int i = 0; i < strlen(sin); i++) {
        printf("%d ", sin_as_int[i]);
    }


    for (int i = 0; i < strlen(sin); i++) {
        if (sin_as_int[i] >= 10) {
            sin_as_int[i] -= 9;
        }

        sum += sin_as_int[i];
    }

    if (sum % 10 == 0) {
        printf("\nThe SIN number is valid.\n");
    } else {
        printf("\nThe SIN number is not valid.\n");
    }

    return 0;
}