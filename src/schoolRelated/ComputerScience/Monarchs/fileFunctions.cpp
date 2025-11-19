#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>                       // For allegro, must be in compiler search path.
#include <allegro5/allegro_native_dialog.h> 		// for message box
#include "monarchs.h"

/** This function reads in the data from the textfile and saves it to the database
    Parameters: p[] is the array of Persons that will be populated by this function.
    counter is the number of monarchs in the array.
    Returns a 0 if all good, 1 if there is an error reading the text file.
*/
int readFile(Person p[], int &counter){
    FILE *inFile = fopen("MonarchsData.txt", "r");

    if (!inFile) {
        return 1;
    }

    counter = 0;
    char line[100];
    char trash[100];
    while (fgets(line, sizeof(line), inFile)) {
        sscanf(line, "%13s %5s %d %13s %d %s %d %13s %d",
               p[counter].name,
               p[counter].regnal,
               &p[counter].birth.year,
               p[counter].birth.month,
               &p[counter].birth.day,
               trash,
               &p[counter].death.year,
               p[counter].death.month,
               &p[counter].death.day);
        counter++;
    }

    fclose(inFile);
    return 0;
}
