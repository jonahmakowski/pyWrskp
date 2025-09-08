#include <stdio.h>

int main() {
    /* The program calculates the positive difference between two numbers */
    int first, second, posdiff; 
    printf("Please enter two integers\n"); 
    scanf("%d %d", &first, &second); 
    if (first < second) { 
        posdiff = second -first; 
        printf("%d - %d = %d", second, first, posdiff); 
    } else {
        posdiff = first - second; 
        printf("%d - %d = %d", first,second, posdiff); 
    }