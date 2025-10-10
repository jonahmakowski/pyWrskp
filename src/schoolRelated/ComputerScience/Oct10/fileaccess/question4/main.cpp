#include <stdio.h>
#include <string.h>

int main() {
    FILE *ftpr;
    ftpr = fopen("test_file.txt", "a");

    char name[100];
    char address[200];

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Enter your address: ");
    fgets(address, sizeof(address), stdin);
    address[strcspn(address, "\n")] = '\0';

    fprintf(ftpr, "Name: %s\n", name);
    fprintf(ftpr, "Address: %s\n", address);
    fclose(ftpr);

    return 0;
}