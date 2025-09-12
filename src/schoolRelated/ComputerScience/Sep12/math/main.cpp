#include <stdio.h>
#include <math.h>

int main() {
    for (int value = 1; value <= 15; ++value) {
        printf("3 raised to the power of %d is %.1f\n", value, pow(3, value));
    }
}