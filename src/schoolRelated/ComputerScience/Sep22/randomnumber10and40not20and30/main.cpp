#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

int main() {
    srand(time(0));

    int value = 21;

    while (value > 20 && value < 30) {
        value = rand() % (40 - 10 + 1) + 10;
    }

    printf("Random number between 10 and 40, not between 20 and 30: %d\n", value);

    return 0;
}
