#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

int main() {
    srand(time(0));

    int num_of_dice = 6;
    int dice_values[num_of_dice];
    int attempt = 1;
    int allowed_rounds = 3000;
    int attempt_per_round[allowed_rounds];

    for (int a = 0; a < allowed_rounds; a++) {
        attempt = 1;
        printf("\n\n\n\nRound %d:\n", a + 1);
        while (true) {
            bool all_equal = true;

            for (int i = 0; i < num_of_dice; i++) {
                dice_values[i] = rand() % 6 + 1;
                if (i != 0 && dice_values[i] != dice_values[0]) {
                    all_equal = false;
                }
            }

            if (all_equal) {
                printf("Yahtzee! on attempt %d, all %ds\n", attempt, dice_values[0]);
                attempt_per_round[a] = attempt;
                break;
            }
            attempt++;
        }
    }

    printf("Attempts per round:\n");
    int min_value = pow(1000, 100);
    float average = 0;
    for (int a = 0; a < allowed_rounds; a++) {
        if (attempt_per_round[a] < min_value) {
            min_value = attempt_per_round[a];
        }
        printf("Round %d: %d attempts\n", a + 1, attempt_per_round[a]);
        average += attempt_per_round[a];
    }

    average /= allowed_rounds;
    printf("Average attempts in a round: %f\n", average);
    printf("Minimum attempts in a round: %d\n", min_value);
}
