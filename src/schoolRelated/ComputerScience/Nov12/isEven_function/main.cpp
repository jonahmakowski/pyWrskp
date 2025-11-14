#include <stdio.h>

int isEven(int input1);

int main() {
    int even_num = 2;
    int odd_num = 1;

    printf("Result from running with even number: %d\n", isEven(even_num));
    printf("Result from running with odd number: %d\n", isEven(odd_num));

    return 0;
}

int isEven(int input1) {
    if (input1 % 2 == 0) {
        return 0;
    } else {
        return 1;
    }
}
