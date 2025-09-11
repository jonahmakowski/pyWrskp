// Jonah Makowski - September 10, 2025
// Funny headline generator

#include <stdio.h>
#include <string.h>

int main() {
    // initialize variables
    char name[20];
    char country[20];
    char verb[20];
    char place[20];
    char profession[20];
    char insult[20];
    int people;
    float percentage;

    // Get input for name
    printf("Enter a name:\n");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    // Get input for country
    printf("Enter a country:\n");
    fgets(country, sizeof(country), stdin);
    country[strcspn(country, "\n")] = '\0';

    // Get input for the verb
    printf("Enter a verb:\n");
    fgets(verb, sizeof(verb), stdin);
    verb[strcspn(verb, "\n")] = '\0';

    // Get input for place
    printf("Enter a place:\n");
    fgets(place, sizeof(place), stdin);
    place[strcspn(place, "\n")] = '\0';

    // Get input for profession
    printf("Enter a profession:\n");
    fgets(profession, sizeof(profession), stdin);
    profession[strcspn(profession, "\n")] = '\0';

    // Get input for insult
    printf("Enter an insult:\n");
    fgets(insult, sizeof(insult), stdin);
    insult[strcspn(insult, "\n")] = '\0';

    // Get input for percentage
    printf("Enter a float between 0-100:\n");
    scanf("%f", &percentage);

    // Get input for people
    printf("Enter an integer:\n");
    scanf("%d", &people);

    // Print the actual headlines
    // Headline #1
    printf("Breaking: %s has been elected to be", name);
    printf("leader of %s by a %.2f %% margin.\n", country, percentage);

    // Headline #2
    printf("%.2f %% of people call to bring %s to justice, ",
        percentage, name);
    printf("%s's government puts out warrant.\n", country);

    // Headline #3
    printf("BREAKING: %s has %s from %s to %s. %s say that ", 
        name, verb, place, country, profession);
    printf("there's a %.2f %% chance that he'll be caught\n", percentage);

    // Headline #4
    printf("Opinion: %s is a %s. %d people agree.\n", 
        name, insult, people);
}
