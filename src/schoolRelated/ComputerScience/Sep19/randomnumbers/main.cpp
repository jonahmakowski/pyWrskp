#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

int main() {
    srand(time(0));

    // Input variables
    int max_value;
    int min_value;
    int number_of_randoms;

    // Input
    printf("Enter the maximum value: ");
    scanf("%d", &max_value);
    printf("Enter the minimum value: ");
    scanf("%d", &min_value);
    printf("Enter the number of random numbers to generate: ");
    scanf("%d", &number_of_randoms);

    // Output variables
    int random_numbers[number_of_randoms];
    int max_number = min_value;
    int min_number = max_value;
    int average = 0;

    // Generate random numbers
    printf("Random numbers:\n");

    for (int i = 0; i < number_of_randoms; i++) {
        random_numbers[i] = rand() % (max_value - min_value + 1) + min_value;
        printf("%d\n", random_numbers[i]);

        if (random_numbers[i] > max_number) {
            max_number = random_numbers[i];
        }
        
        if (random_numbers[i] < min_number) {
            min_number = random_numbers[i];
        }

        average += random_numbers[i];
    }

    // Display output variables
    printf("Max number: %d\n", max_number);
    printf("Min number: %d\n", min_number);
    printf("Average: %.1f\n", (float)average / number_of_randoms);


    return 0;
}
