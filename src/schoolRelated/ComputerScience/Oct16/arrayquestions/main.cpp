#include <stdio.h>
#include <stdlib.h>
#include <time.h>

bool drawn(int *cards_drawn, int card) {
    for (int i = 0; i < 54; i++) {
        if (cards_drawn[i] == card) {
            return true;
        }
    }
    return false;
}

bool all_drawn(int *cards_drawn) {
    for (int i = 0; i < 54; i++) {
        if (cards_drawn[i] == -3) {
            return false;
        }
    }
    return true;
}

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

    // Question 10
    const int PLAYERS = 4;
    srand(time(0));
    
    printf("Question 10:\n");
    int cards_drawn[54] = {-3};
    char suits[4][10] = {"Hearts", "Diamonds", "Clubs", "Spades"};
    char ranks[13][10] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};

    int player = 1;
    int index = 0;
    
    while (!all_drawn(cards_drawn)) {
        int card = rand() % 54 - 2; // -2 to 51, where -2 and -1 are jokers
        if (!drawn(cards_drawn, card)) {
            cards_drawn[index] = card;
            printf("Player %d drew %s of %s\n", player, ranks[card % 13], suits[card / 13]);
            player = (player % PLAYERS) + 1;
            index++;
        }
    }

    return 0;
}
