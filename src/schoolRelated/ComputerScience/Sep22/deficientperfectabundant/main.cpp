#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int sum = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    if (sum < n) {
        printf("deficient\n");
    } else if (sum == n) {
        printf("perfect\n");
    } else {
        printf("abundant\n");
    }
    return 0;
}
