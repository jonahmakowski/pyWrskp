# Documentation for src/schoolRelated/ComputerScience/Sep22/harrypotterenrichmentassignment/main.cpp

# AI Summary
This program is a simple game that prompts the user to enter names, and then selects and displays three random names from the entered names. If 'Harry Potter' is entered, it is automatically added as the fourth player. If 'Voldemort' is entered or if there are fewer than three names entered, the competition is cancelled.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 6/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are some areas where the code could be more concise or efficient. The code also does not follow all the conventions of the C programming language, such as using more descriptive variable names and including comments to explain the code.
# Functions

## main
### Explanation
The main function of the program. It initializes the random number generator, prompts the user to enter names, and then selects and displays three random names from the entered names. If 'Harry Potter' is entered, it is automatically added as the fourth player. If 'Voldemort' is entered or if there are fewer than three names entered, the competition is cancelled.
### Code
```c
int main() {
    srand(time(0));

    // Input variables
    char names[10][20];
    int number_of_names = 0;
    int display_num = 1;
    bool harry_potter = false;
    bool voldemort = false;

    for (int i = 0; i < 10; i++) {
        printf("Enter name %d: ", display_num);
        display_num++;
        fgets(names[i], sizeof(names[i]), stdin);
        names[i][strcspn(names[i], "\n")] = '\0';

        if (strcmp(names[i], "Harry Potter") == 0) {
            harry_potter = true;
            i--;
            continue;
        }
        
        if (strcmp(names[i], "Voldemort") == 0) {
            voldemort = true;
            i--;
            continue;
        }

        if (strcmp(names[i], "") == 0) {
            break;
        }

        number_of_names++;
    }

    int temp_number_of_names = number_of_names;
    if (harry_potter) {
        temp_number_of_names++;
    }

    if (temp_number_of_names < 3 || voldemort) {
        printf("The competition is cancelled!\n");
        return 0;
    }

    char selected_players[4][20];
    int used_indices[10];

    for (int i = 0; i < 3; i++) {
        int index = rand() % temp_number_of_names;
        
        for (int j = 0; j < i; j++) { // Make sure the index is unique
            if (used_indices[j] == index) {
                index = rand() % temp_number_of_names;
                j = 0;
            }
        }

        strcpy(selected_players[i], names[index]);
        used_indices[i] = index;
    }

    for (int i = 0; i < 3; i++) {
        printf("Player %d: %s\n", i + 1, selected_players[i]);
    }
    
    if (harry_potter) {
        printf("Player 4: Harry Potter\n");
    }
}
```
# Overall File Contents
```c
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>


int main() {
    srand(time(0));

    // Input variables
    char names[10][20];
    int number_of_names = 0;
    int display_num = 1;
    bool harry_potter = false;
    bool voldemort = false;

    for (int i = 0; i < 10; i++) {
        printf("Enter name %d: ", display_num);
        display_num++;
        fgets(names[i], sizeof(names[i]), stdin);
        names[i][strcspn(names[i], "\n")] = '\0';

        if (strcmp(names[i], "Harry Potter") == 0) {
            harry_potter = true;
            i--;
            continue;
        }
        
        if (strcmp(names[i], "Voldemort") == 0) {
            voldemort = true;
            i--;
            continue;
        }

        if (strcmp(names[i], "") == 0) {
            break;
        }

        number_of_names++;
    }

    int temp_number_of_names = number_of_names;
    if (harry_potter) {
        temp_number_of_names++;
    }

    if (temp_number_of_names < 3 || voldemort) {
        printf("The competition is cancelled!\n");
        return 0;
    }

    char selected_players[4][20];
    int used_indices[10];

    for (int i = 0; i < 3; i++) {
        int index = rand() % temp_number_of_names;
        
        for (int j = 0; j < i; j++) { // Make sure the index is unique
            if (used_indices[j] == index) {
                index = rand() % temp_number_of_names;
                j = 0;
            }
        }

        strcpy(selected_players[i], names[index]);
        used_indices[i] = index;
    }

    for (int i = 0; i < 3; i++) {
        printf("Player %d: %s\n", i + 1, selected_players[i]);
    }
    
    if (harry_potter) {
        printf("Player 4: Harry Potter\n");
    }
}

```
