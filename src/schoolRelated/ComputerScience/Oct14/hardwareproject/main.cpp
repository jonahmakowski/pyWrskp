// Jonah Makowski - Display stats about laptops from different universities
#include <stdio.h>
#include <string.h>

int main() {
    // Define how many laptops are in the file
    const int MAX_LAPTOPS = 5;

    // Define variables to hold the data
    char line[200];
    char university[50], brand[50];
    int ram, storage;
    float price;

    // Define the pointer to the file
    FILE *fptr;

    // Open the file for reading
    fptr = fopen("laptop_data.txt", "r");

    // Make sure the file opened correctly
    if (fptr == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Process and display the data
    printf("University\t\tBrand\t\tRAM in GB\tStorage in GB\t\tPrice\t\tPrice per GB of RAM\tPrice per GB of Storage\n");
    printf("-----------------------------------------------------------------------------------------------------------------------------------------------\n");
    for (int i = 0; i < MAX_LAPTOPS; i++) {
        // Read the line from the file
        fgets(line, sizeof(line), fptr);

        // Parse the line
        sscanf(line, "%49[0-9a-zA-Z ]\t%s %d %d %f", university, brand, &ram, &storage, &price);
        
        // Display the parsed data
        printf("%-23s %-15s %-15d %-23d $%-14.2f $%-22.2f $%-20.2f\n", university, brand, ram, storage, price, price / ram, price / storage);
    }

    fclose(fptr);
    return 0;
}