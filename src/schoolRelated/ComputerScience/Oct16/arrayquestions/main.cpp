#include <stdio.h>

int main() {
    // Question 1
    int q1_array[5] = {1, 2, 3, 4, 5};

    for (int i = sizeof(q1_array) / sizeof(q1_array[0]) - 1; i >= 0; i--) {
        printf("%d ", q1_array[i]);
    }
    printf("\n");

    // Question 2
    // Setting variables
    FILE *fptr;
    int sum = 0;
    
    // Writing into the file so I don't have to type 100 numbers manually
    fptr = fopen("data.txt", "w");
    for (int i = 1; i <= 100; i++) {
        fprintf(fptr, "%d\n", i);
    }
    fclose(fptr);

    // Reading from the file
    fptr = fopen("data.txt", "r");
    int q2_array[100];
    for (int i = 0; i < 100; i++) {
        fscanf(fptr, "%d", &q2_array[i]);
    }

    // Calculating the sum
    for (int i = 0; i < 100; i++) {
        sum += q2_array[i];
    }

    printf("Sum of 100 numbers: %d\n", sum);

    fclose(fptr);

    // Question 3
    int q3_array[100] = {0};
    int start_value = 1;

    for (int i = 0; i < 100; i++) {
        q3_array[i] = start_value;
        start_value+=2;
    }

    for (int i = 0; i < 100; i++) {
        printf("%d ", q3_array[i]);
    }

    printf("\n");

    // Question 5
    const int Q5_SIZE = 10;
    int q5_array[Q5_SIZE] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int temp;

    for (int i = 0; i < Q5_SIZE / 2; i++) {
        temp = q5_array[i];
        q5_array[i] = q5_array[Q5_SIZE - 1 - i];
        q5_array[Q5_SIZE - 1 - i] = temp;
    }

    for (int i = 0; i < Q5_SIZE; i++) {
        printf("%d ", q5_array[i]);
    }

    printf("\n");

    // Question 7
    int min = 1000000000;
    int max = -1000000000;

    int max_index = 0;
    int min_index = 0;

    int q7_array[10] = {34, -2, 45, 29, 8, 0, -15, 67, 23, 4};

    for (int i = 0; i < 10; i++) {
        if (q7_array[i] < min) {
            min = q7_array[i];
            min_index = i;
        }
        if (q7_array[i] > max) {
            max = q7_array[i];
            max_index = i;
        }
    }

    printf("Min: %d, Max: %d\n", min, max);
    printf("Min Index: %d, Max Index: %d\n", min_index, max_index);

    return 0;
}
