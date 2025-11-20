#include <stdio.h>
#include <string.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>                       // For allegro, must be in compiler search path.
//#include <allegro5/allegro_native_dialog.h> 		// for message box
#include "monarchs.h"
#include <allegro5/allegro_primitives.h>

int ageAtDeath(const Person p) {
    return p.death.year - p.birth.year;
}

/***This function prints the contents of the database to the screen using allegro
Parameters: p[] is the database
counter is the number of entries in the database*/
void printDatabase(ALLEGRO_FONT *font, Person p[], int counter){
    al_draw_filled_rounded_rectangle(0, 0, SCREEN_W/10, SCREEN_H/15, 10, 10, al_map_rgb(0, 0, 255));
    al_draw_filled_rounded_rectangle(SCREEN_W/10, 0, SCREEN_W/5, SCREEN_H/15, 10, 10, al_map_rgb(0, 255, 0));
    al_draw_filled_rounded_rectangle(SCREEN_W/5, 0, SCREEN_W/5 * 2, SCREEN_H/15, 10, 10, al_map_rgb(200, 200, 200));

    //creates the print string to be fed into al_draw_text()
    char printString[200] = "";

    for (int i = 0; i < counter; i++){

        //prints name to the buffer
        sprintf(printString, "%s %s", p[i].name, p[i].regnal);
        al_draw_text(font, FOREGROUND, COL_1, 50 + i*40 + SCREEN_H/15, ALLEGRO_ALIGN_LEFT, printString);

        //prints birth day to the buffer
        sprintf(printString, "%d %s %d", p[i].birth.year, p[i].birth.month, p[i].birth.day);
        al_draw_text(font, FOREGROUND, COL_2, 50 + i*40 + SCREEN_H/15, ALLEGRO_ALIGN_LEFT, printString);
        //prints death day to the buffer
        sprintf(printString, "%d %s %d", p[i].death.year, p[i].death.month, p[i].death.day);
        al_draw_text(font, FOREGROUND, COL_3, 50 + i*40 + SCREEN_H/15, ALLEGRO_ALIGN_LEFT, printString);

        // Adding age at death column
        sprintf(printString, "%d", ageAtDeath(p[i]));
        al_draw_text(font, FOREGROUND, COL_4, 50 + i*40 + SCREEN_H/15, ALLEGRO_ALIGN_LEFT, printString);
    }

}

/**prints the title to the top of the screen*/
void printTitle(ALLEGRO_FONT *font){
    //print Monarch title
    al_draw_text(font, FOREGROUND, COL_1, 5+SCREEN_H/15, ALLEGRO_ALIGN_LEFT, "Monarch");

    //print Monarch title
    al_draw_text(font, FOREGROUND, COL_2, 5+SCREEN_H/15, ALLEGRO_ALIGN_LEFT, "Birth Date");

    //print Monarch title
    al_draw_text(font, FOREGROUND, COL_3, 5+SCREEN_H/15, ALLEGRO_ALIGN_LEFT, "Death Date");

    //print Monarch title
    al_draw_text(font, FOREGROUND, COL_4, 5+SCREEN_H/15, ALLEGRO_ALIGN_LEFT, "Age at Death");
}

void show_instructions() {
    printf("Instructions:\n");
    printf(" - Click within the blue rectangle to sort the monarchs by age at death.\n");
    printf(" - Click within the green rectangle to sort the monarchs by year of death.\n");
    printf(" - Click the grey button to add/remove monarchs in the console.\n");
}

void sort_by_age_at_death(Person p[], int counter) {
    for (int i = 0; i < counter - 1; i++) {
        for (int j = 0; j < counter - i - 1; j++) {
            if (ageAtDeath(p[j]) > ageAtDeath(p[j + 1])) {
                Person temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

void sort_by_death_year(Person p[], int counter) {
    for (int i = 0; i < counter - 1; i++) {
        for (int j = 0; j < counter - i - 1; j++) {
            if (p[j].death.year > p[j + 1].death.year) {
                Person temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

void write_data_to_file(Person p[], int counter) {
    FILE *file = fopen("monarchsData.txt", "w");
    for (int i = 0; i < counter; i++) {
        fprintf(file, "%s %s %d %s %d to %d %s %d\n",
                p[i].name,
                p[i].regnal,
                p[i].birth.year,
                p[i].birth.month,
                p[i].birth.day,
                p[i].death.year,
                p[i].death.month,
                p[i].death.day);
    }
    fclose(file);
}

void add_monarch(Person p[], int &counter) {
    if (counter >= 20) {
        printf("Database is full. Cannot add more monarchs.\n");
        return;
    }

    Person new_monarch;
    printf("Enter name: ");
    scanf("%s", new_monarch.name);
    printf("Enter regnal number: ");
    scanf("%s", new_monarch.regnal);
    printf("Enter birth year, month, day: ");
    scanf("%d %s %d", &new_monarch.birth.year, new_monarch.birth.month, &new_monarch.birth.day);
    printf("Enter death year, month, day: ");
    scanf("%d %s %d", &new_monarch.death.year, new_monarch.death.month, &new_monarch.death.day);

    p[counter] = new_monarch;
    counter++;
}

void remove_monarch(Person p[], int &counter) {
    if (counter <= 0) {
        printf("Database is empty. Cannot remove monarchs.\n");
        return;
    }

    char name[14];
    char regnal[6];
    printf("Enter name of monarch to remove: ");
    scanf("%s", name);
    printf("Enter regnal number of monarch to remove: ");
    scanf("%s", regnal);

    for (int i = 0; i < counter; i++) {
        if (strcmp(p[i].name, name) == 0 && strcmp(p[i].regnal, regnal) == 0) {
            // Shift remaining monarchs down
            for (int j = i; j < counter - 1; j++) {
                p[j] = p[j + 1];
            }
            counter--;
            printf("Monarch %s %s removed from database.\n", name, regnal);
            return;
        }
    }
    printf("Monarch %s %s not found in database.\n", name, regnal);
}
