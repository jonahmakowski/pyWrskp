#include <stdio.h>

int floor(float x) {
    return (int)x;
}

int ceil(float x) {
    if ((int)x == x) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}

int round(float x) {
    if (x - (int)x < 0.5) {
        return (int)x;
    } else {
        return (int)x + 1;
    }
}

int main() {
    printf("5.7 floored is %d\n", floor(5.7));
    printf("5.7 ceiled is %d\n", ceil(5.7));
    printf("5.7 rounded is %d\n", round(5.7));
}
