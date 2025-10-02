#include <stdio.h>

int main() {
    const int length = 10;

    for (int i = 1; i <= length; i++) {
        for (int j = 1; j <= i; j++) {
            printf("1");
        }
        printf(" x ");
        for (int j = 1; j <= i; j++) {
            printf("1");
        }

        printf(" = ");

        for (int j = 1; j <= i; j++) {
            printf("%d", j);
        }
        for (int j = i-1; j >= 1; j--) {
            printf("%d", j);
        }

        printf("\n");
    }
}