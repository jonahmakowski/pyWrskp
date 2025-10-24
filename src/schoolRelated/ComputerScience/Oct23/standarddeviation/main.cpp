// Jonah Makowski - Standard Deviation Calculation
// This program reads numbers from a file, calculates their average and standard deviation, and prints the results.

#include <stdio.h>
#include <math.h>

int main() {
    // Init variables
    double numbers[200] = {0};
    int count = 0;
    double sum = 0, mean = 0, distances = 0, deviation = 0;

    FILE *fptr = fopen("nums.txt", "r");
    
    // Check if the file exists
    if (fptr == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Load the numbers from the file
    while (fscanf(fptr, "%lf", &numbers[count]) == 1) {
        sum += numbers[count];
        count++;
    }

    fclose(fptr);

    // Calculate mean and standard deviation
    mean = sum / count;

    for (int i = 0; i < count; i++) {
        distances += pow(fabs(numbers[i] - mean), 2);
    }

    deviation = sqrt(distances / count);

    // Print results
    printf("Average: %.3lf\n", mean);
    printf("Standard Deviation: %.3lf\n", deviation);
}
