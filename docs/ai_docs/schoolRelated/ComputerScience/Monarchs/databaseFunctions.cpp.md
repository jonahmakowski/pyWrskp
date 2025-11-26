# Documentation for src/schoolRelated/ComputerScience/Monarchs/databaseFunctions.cpp

# AI Summary
This file contains functions for managing a database of monarchs, including converting month names to numbers, calculating age at death, printing the database to the screen, printing the title, showing instructions, sorting the database by age at death or year of death, writing the database to a file, adding a new monarch, and removing a monarch.

The AI gave it a general rating of 7/10

The AI gave it a conventions rating of 6/10

The reason for the AI's rating is:

The code is generally functional and concise, but there are some areas where it could be improved, such as using more descriptive variable names and adding comments to explain complex logic. The code follows some conventions but could be more consistent with others.
# Functions

## month_to_number
### Explanation
Converts a month name to its corresponding number.
### Code
```c
int month_to_number(const char* month) {
    if (strcmp(month, "January") == 0) return 1;
    if (strcmp(month, "February") == 0) return 2;
    if (strcmp(month, "March") == 0) return 3;
    if (strcmp(month, "April") == 0) return 4;
    if (strcmp(month, "May") == 0) return 5;
    if (strcmp(month, "June") == 0) return 6;
    if (strcmp(month, "July") == 0) return 7;
    if (strcmp(month, "August") == 0) return 8;
    if (strcmp(month, "September") == 0) return 9;
    if (strcmp(month, "October") == 0) return 10;
    if (strcmp(month, "November") == 0) return 11;
    if (strcmp(month, "December") == 0) return 12;
    return 0; // Invalid month
}
```

## ageAtDeath
### Explanation
Calculates the age of a person at the time of their death.
### Code
```c
int ageAtDeath(const Person p) {
    int month_birth = month_to_number(p.birth.month);
    int month_death = month_to_number(p.death.month);

    if (month_death < month_birth) {
        return p.death.year - p.birth.year - 1;
    } else if (month_death == month_birth && p.death.day < p.birth.day) {
        return p.death.year - p.birth.year - 1;
    }

    return p.death.year - p.birth.year;
}
```

## printDatabase
### Explanation
Prints the contents of the database to the screen using Allegro.
### Code
```c
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
```

## printTitle
### Explanation
Prints the title to the top of the screen.
### Code
```c
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
```

## show_instructions
### Explanation
Shows instructions for interacting with the program.
### Code
```c
void show_instructions() {
    printf("Instructions:\n");
    printf(" - Click within the blue rectangle to sort the monarchs by age at death.\n");
    printf(" - Click within the green rectangle to sort the monarchs by year of death.\n");
    printf(" - Click the grey button to add/remove monarchs in the console.\n");
}
```

## sort_by_age_at_death
### Explanation
Sorts the database by age at death.
### Code
```c
void sort_by_age_at_death(Person p[], int counter) {
    for (int i = 0; i < counter; i++) {
        for (int j = 0; j < counter - i - 1; j++) {
            if (ageAtDeath(p[j]) > ageAtDeath(p[j + 1])) {
                Person temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}
```

## sort_by_death_year
### Explanation
Sorts the database by year of death.
### Code
```c
void sort_by_death_year(Person p[], int counter) {
    for (int i = 0; i < counter; i++) {
        for (int j = 0; j < counter - i - 1; j++) {
            if (p[j].death.year > p[j + 1].death.year) {
                Person temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}
```

## write_data_to_file
### Explanation
Writes the database to a file.
### Code
```c
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
```

## add_monarch
### Explanation
Adds a new monarch to the database.
### Code
```c
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
```

## remove_monarch
### Explanation
Removes a monarch from the database.
### Code
```c
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
```
# Overall File Contents
```c
#include <stdio.h>
#include <string.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>                       // For allegro, must be in compiler search path.
//#include <allegro5/allegro_native_dialog.h> 		// for message box
#include "monarchs.h"
#include <allegro5/allegro_primitives.h>

int month_to_number(const char* month) {
    if (strcmp(month, "January") == 0) return 1;
    if (strcmp(month, "February") == 0) return 2;
    if (strcmp(month, "March") == 0) return 3;
    if (strcmp(month, "April") == 0) return 4;
    if (strcmp(month, "May") == 0) return 5;
    if (strcmp(month, "June") == 0) return 6;
    if (strcmp(month, "July") == 0) return 7;
    if (strcmp(month, "August") == 0) return 8;
    if (strcmp(month, "September") == 0) return 9;
    if (strcmp(month, "October") == 0) return 10;
    if (strcmp(month, "November") == 0) return 11;
    if (strcmp(month, "December") == 0) return 12;
    return 0; // Invalid month
}

int ageAtDeath(const Person p) {
    int month_birth = month_to_number(p.birth.month);
    int month_death = month_to_number(p.death.month);

    if (month_death < month_birth) {
        return p.death.year - p.birth.year - 1;
    } else if (month_death == month_birth && p.death.day < p.birth.day) {
        return p.death.year - p.birth.year - 1;
    }
    
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
    for (int i = 0; i < counter; i++) {
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
    for (int i = 0; i < counter; i++) {
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

```
