// Jonah Makowski - September 10, 2025
// Funny headline generator

#include <stdio.h>

int main() {
    // initialize variables
    char name[20];
    char country[20];
    float percentage;

    // Get input for name
    printf("Enter a name:\n");
    fgets(name, sizeof(name), stdin); // Clear newline character from the end
    for(int i = 0; i < sizeof(name); i++) {
        if(name[i] == '\n') {
            name[i] = '\0';
        }
    }
    
    // Get input for country
    printf("Enter a country:\n");
    fgets(country, sizeof(country), stdin); // Clear newline character from the end
    for(int i = 0; i < sizeof(country); i++) {
        if(country[i] == '\n') {
            country[i] = '\0';
        }
    }

    // Get input for percentage
    printf("Enter a float between 0-100:\n");
    scanf("%f", &percentage);

    printf("Breaking: %s has been elected to be leader of %s by a %.2f %% margin.\n", name, country, percentage);
    printf("%.2f %% of people call to bring %s to justice, %s's government puts out warrant.\n", percentage, name, country);
}
