// Jonah Makowski - Rectangle, Bar, and right angle triangle functions

#include <stdio.h>

void printBar(char symbol, int number) {
    for (int i = 0; i < number; i++) {
        printf("%c", symbol);
    }
    printf("\n");
}

void printRectangle(char symbol, int width, int height, int x_pos, int y_pos) {
    for (int i = 0; i < y_pos; i++) {
        printf("\n");
    }

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < x_pos; j++) {
            printf(" ");
        }

        printf("%c", symbol);

        for (int j = 0; j < width - 2; j++) {
            if (i == 0 || i == height - 1) {
                printf("%c", symbol);
            } else {
                printf(" ");
            }
        }

        printf("%c", symbol);

        printf("\n");
    }
}

void printRightTriangle(int base, int height, int x_pos, int y_pos) {
    for (int i = 0; i < y_pos; i++) {
        printf("\n");
    }

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < x_pos; j++) {
            printf(" ");
        }

        for (int j = 0; j <= (base * i + 1) / height; j++) {
            if (j == 0 || i == height - 1 || j == (base * i + 1) / height) {
                printf("*");
            } else {
                printf(" ");
            }
        }

        printf("\n");
    }
}

int main() {
    printBar('*', 35);
	printBar('?', 50);
	printBar('+', 20);
	printBar('#', 60);

    printRectangle('*', 5, 4, 3, 6);

    printRightTriangle(6, 6, 3, 2);

    return 0;
}
