#include <stdio.h>

int main() {
    int age;
    int height;
    int weight;

    printf("How old are you?\n");
    scanf("%d", &age);

    printf("How tall are you (in cm)?\n");
    scanf("%d", &height);
    
    printf("How much do you weigh (in kg)?\n");
    scanf("%d", &weight);
    
    printf("Age\tHeight(cm)\tWeight(kg)\n");
    printf("---\t----------\t----------\n");
    printf("%3d\t%10d\t%10d\n", age, height, weight);
}
