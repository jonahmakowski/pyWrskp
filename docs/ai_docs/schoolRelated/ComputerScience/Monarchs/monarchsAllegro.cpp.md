# Documentation for src/schoolRelated/ComputerScience/Monarchs/monarchsAllegro.cpp

# AI Summary
This file contains functions to initialize Allegro, check the setup of the display and font, and draw the title and database on the display. It uses Allegro for graphics and font handling.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and functional, but there are some areas where it could be more concise. The code follows most conventions, but there are a few inconsistencies.
# Functions

## initializeAllegro
### Explanation
Initializes required Allegro functions, including Allegro itself, font addons, and the mouse.
### Code
```c++
void initializeAllegro(){

    // Initialize Allegro
	al_init();

	//initialize font addons
	al_init_font_addon();
    al_init_ttf_addon();
    al_install_mouse();
}
```

## checkSetup
### Explanation
Checks if the display and font have been set up properly. Returns 0 if good, -1 if error.
### Code
```c++
int checkSetup(ALLEGRO_DISPLAY *display, ALLEGRO_FONT *font){
    // Check if your allegro routines worked successfully.
	if (!display) {
    	//al_show_native_message_box(display, "Error", "Error", "Failed to initialize display!",
        //                         nullptr, ALLEGRO_MESSAGEBOX_ERROR);
       	return -1;
	}

    if (!font){
        //al_show_native_message_box(display, "Error", "Error", "Could not load comic.ttf",
        //                            nullptr, ALLEGOR_MESSAGEBOX_ERROR);
        return -1;
    }

    return 0;
}
```

## draw_stuff
### Explanation
Clears the display to a background color, prints the title and database, and flips the display.
### Code
```c++
void draw_stuff(ALLEGRO_FONT *font, Person monarchs[], int number) {
    al_clear_to_color(BACKGROUND);
    printTitle(font);
    printDatabase(font, monarchs, number);
    al_flip_display();
}
```
# Overall File Contents
```c++
#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>                       // For allegro, must be in compiler search path.
//#include <allegro5/allegro_native_dialog.h> 		// for message box
#include "monarchs.h"

/**Initializes required allegro functions */
void initializeAllegro(){

    // Initialize Allegro
	al_init();

	//initialize font addons
	al_init_font_addon();
    al_init_ttf_addon();
    al_install_mouse();
}

/**Checks to see if the display and font have been set up properly.
A message box reports what wasn't set up properly.
Parameters: display and font variables
Returns: 0 if good, -1 if error
*/
int checkSetup(ALLEGRO_DISPLAY *display, ALLEGRO_FONT *font){
    // Check if your allegro routines worked successfully.
	if (!display) {
    	//al_show_native_message_box(display, "Error", "Error", "Failed to initialize display!",
        //                         nullptr, ALLEGRO_MESSAGEBOX_ERROR);
       	return -1;
	}

    if (!font){
        //al_show_native_message_box(display, "Error", "Error", "Could not load comic.ttf",
        //                            nullptr, ALLEGRO_MESSAGEBOX_ERROR);
        return -1;
    }

    return 0;
}

void draw_stuff(ALLEGRO_FONT *font, Person monarchs[], int number) {
    al_clear_to_color(BACKGROUND);
    printTitle(font);
    printDatabase(font, monarchs, number);
    al_flip_display();
}

```
