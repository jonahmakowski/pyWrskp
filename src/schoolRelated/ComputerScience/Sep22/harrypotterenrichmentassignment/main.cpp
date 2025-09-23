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
