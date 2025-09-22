#include <stdlib.h>
#include <time.h>
#include <stdio.h>

// rand() % (max_value - min_value + 1) + min_value

int main() {
    srand(time(0));

    int dice_values[6] = {0, 0, 0, 0, 0, 0};

    for (int i = 0; i < 100; i++) {
        int random_number = rand() % 6 + 1;
        dice_values[random_number - 1]++;
    }

    for (int i = 0; i < 6; i++) {
        printf("Side %d: %d times\n", i + 1, dice_values[i]);
    }

    return 0;
}
