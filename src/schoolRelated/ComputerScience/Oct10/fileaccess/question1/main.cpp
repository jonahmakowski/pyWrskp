#include <stdio.h>
#include <string.h>

int main() {
    char line1[100], line2[100];
    FILE *fptr;

    fptr = fopen("test_file.txt", "r");

    if (fptr == nullptr) {
        perror("Error opening file");
        return 1;
    }

    fgets(line1, sizeof(line1), fptr);
    fgets(line2, sizeof(line2), fptr);

    fclose(fptr);

    line1[strcspn(line1, "\n")] = '\0';
    line2[strcspn(line2, "\n")] = '\0';

    printf("Line 1: %s\n", line1);
    printf("Line 2: %s\n", line2);

    return 0;
}