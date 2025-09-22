#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main() {
    srand(time(0));

    float random_number = rand() % 10001;
    random_number = random_number / 10000.0;

    printf("Random number between 0 and 1: %.4f\n", random_number);

    return 0;
}