#include <stdio.h>
#include <string.h>

int main() {
    char line[100];
    FILE *fptr;

    fptr = fopen("test_file.txt", "r");
    
    if (fptr == nullptr) {
        perror("Error opening file");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        fgets(line, sizeof(line), fptr);
        line[strcspn(line, "\n")] = '\0';
        printf("Read line %d: %s\n", i + 1, line);
    }

    fclose(fptr);

    return 0;
}