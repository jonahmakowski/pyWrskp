/*****************************************************************************
 *	Name:     Lindsay Cullum                                                 *
 *	Date:     April 2018                                                     *
 *                                                                           *
 *	Purpose: Monarchs Template                                               *
 *	                                                                         *
 *	Usage:   Starter code for the Monarchs assignment - using Allegro        *
 *	                                                                         *
 *	Revision History:                                                        *
 *	                                                                         *
 *	Known Issues:                                                            *
 *	                                                                         *
 *****************************************************************************/

// To run: clang++ *.cpp -o ./target/testing $(pkg-config allegro-5 allegro_main-5 allegro_font-5 allegro_primitives-5 allegro_image-5 allegro_ttf-5 --libs --cflags); ./target/testing

#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>                   // For allegro, must be in compiler search path.
//#include <allegro5/allegro_native_dialog.h> 		// for message box
#include "monarchs.h"

void handle_mouse_input(ALLEGRO_EVENT ev, ALLEGRO_FONT *font, Person monarchs[], int number) {
    // Placeholder for mouse input handling
    if (ev.mouse.x < SCREEN_W / 10 && ev.mouse.y < SCREEN_H/15) {
        sort_by_age_at_death(monarchs, number);
    } else if (ev.mouse.x < SCREEN_W / 5 && ev.mouse.y < SCREEN_H/15) {
        sort_by_death_year(monarchs, number);
    } else if (ev.mouse.x < SCREEN_W/5 * 2 && ev.mouse.y < SCREEN_H/15) {
        printf("Enter 'a' to add a monarch or 'r' to remove a monarch:\n");
        char choice;
        scanf(" %c", &choice);
        if (choice == 'a') {
            add_monarch(monarchs, number);
        } else if (choice == 'r') {
            remove_monarch(monarchs, number);
        }
    }
    draw_stuff(font, monarchs, number);
    write_data_to_file(monarchs, number);
}

// NOTE: argc, argv parameters are required.
int main(int argc, char *argv[]) {
    show_instructions();

    //***************ALLEGRO SETUP REQUIREMENTS******************
    //initialize Allegro

    initializeAllegro();

    ALLEGRO_EVENT_QUEUE *event_queue = al_create_event_queue();
    al_register_event_source(event_queue, al_get_mouse_event_source());

    //declare and initialize display and font, and check they have been setup properly
    ALLEGRO_DISPLAY *display = al_create_display(SCREEN_W, SCREEN_H);
    ALLEGRO_FONT *font = al_load_ttf_font("SF_Cartoonist_Hand.ttf", 36, 0);
    checkSetup(display, font);

    //set window title
	al_set_window_title(display, "Monarchs");

	//******************POPULATE DATABASE*************************
	//create database of monarchs, reads in data from text file.
    Person monarchs[20];
    int number = 0;
    readFile(monarchs, number);


	//*********************PRINTS OUTPUT TO SCREEN*******************
	//Builds screen by printing to the buffer
	draw_stuff(font, monarchs, number);

    while(true) {
        ALLEGRO_EVENT ev;

        al_wait_for_event(event_queue, &ev);

        if (ev.type == ALLEGRO_EVENT_MOUSE_BUTTON_DOWN) {
            handle_mouse_input(ev, font, monarchs, number);
            // This is here because otherwise it removes monarchs added in the same run for some reason.
            readFile(monarchs, number);
        }
    }

    // Free up memory taken by display.
    al_destroy_display(display);

    // Exit with no errors
	return 0;
}
