// Jonah Makowski - Simple Calculator - September 30, 2025

#include <stdio.h>
#include <math.h>

int main() {
    // Variable Init
    float value1 = 0;
    float value2 = 0;
    char operation;
    float result = 0;

    // Input Section
    printf("Enter the first value: ");
    scanf("%f", &value1);

    printf("Enter the second value: ");
    scanf("%f", &value2);

    printf("Enter the operation (+, -, *, /, ^, %%, r(oot)): ");
    scanf(" %c", &operation);

    // Perform Calculation
    switch (operation) {
        case '+':
            result = value1 + value2;
            break;
        case '-':
            result = value1 - value2;
            break;
        case '*':
            result = value1 * value2;
            break;
        case '/':
            if (value2 != 0) {
                result = value1 / value2;
            } else {
                printf("Error: Division by zero is not allowed.\n");
                return 0;
            }
            break;
        case '^':
            result = pow(value1, value2);
            break;
        case '%':
            if ((int)value2 != 0) {
                result = (int)value1 % (int)value2;
            } else {
                printf("Error: Modulus by zero is not allowed.\n");
                return 0;
            }
            break;
        case 'r':
            if (value1 >= 0) {
                result = sqrt(value1);
            } else {
                printf("Error: Cannot compute the square root of a negative number.\n");
                return 0;
            }
            break;
        default:
            printf("Error: Invalid operation.\n");
            return 0;
            break;
    }

    // Output Result
    if (operation == 'r') {
        printf("The square root of %.2f is %.2f\n", value1, result);
    } else {
        printf("%.2f %c %.2f = %.2f\n", value1, operation, value2, result);
    }
    return 0;
}
