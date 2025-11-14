#include <stdio.h>

char const daysOfWeek[7][20] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

int average(int array[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += array[i];
    }
    return sum / length;
}

int min_index(int array[], int length) {
    int min_idx = 0;
    for (int i = 1; i < length; i++) {
        if (array[i] < array[min_idx]) {
            min_idx = i;
        }
    }
    return min_idx;
}

int max_index(int array[], int length) {
    int max_idx = 0;
    for (int i = 1; i < length; i++) {
        if (array[i] > array[max_idx]) {
            max_idx = i;
        }
    }
    return max_idx;
}

int main() {
    int temperatures[7];

    printf("Enter the temperatures for the week:\n");
    for (int i = 0; i < 7; i++) {
        printf("%s: ", daysOfWeek[i]);
        scanf("%d", &temperatures[i]);
    }

    int avg_temp = average(temperatures, 7);
    int min_temp_idx = min_index(temperatures, 7);
    int max_temp_idx = max_index(temperatures, 7);

    printf("\nAverage temperature for the week: %d\n", avg_temp);
    printf("Lowest temperature: %d on %s\n", temperatures[min_temp_idx], daysOfWeek[min_temp_idx]);
    printf("Highest temperature: %d on %s\n", temperatures[max_temp_idx], daysOfWeek[max_temp_idx]);

    return 0;
}
