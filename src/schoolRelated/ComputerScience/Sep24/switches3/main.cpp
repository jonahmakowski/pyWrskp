#include <stdio.h>
#include <ctype.h>

int main() {
    char letter;

    printf("Enter a letter (A-Z): ");
    scanf(" %c", &letter);
    letter = toupper(letter);

    switch (letter) {
        case 'A':
        case 'B':
        case 'C':
            printf("2\n");
            break;
        case 'D':
        case 'E':
        case 'F':
            printf("3\n");
            break;
        case 'G':
        case 'H':
        case 'I':
            printf("4\n");
            break;
        case 'J':
        case 'K':
        case 'L':
            printf("5\n");
            break;
        case 'M':
        case 'N':
        case 'O':
            printf("6\n");
            break;
        case 'P':
        case 'R':
        case 'S':
            printf("7\n");
            break;
        case 'T':
        case 'U':
        case 'V':
            printf("8\n");
            break;
        case 'W':
        case 'X':
        case 'Y':
            printf("9\n");
            break;
        default:
            printf("Char (%c) doesn't have a corresponding number.\n", letter);
            break;
    }
}