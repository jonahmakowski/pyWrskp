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

// NOTE: argc, argv parameters are required.
int main(int argc, char *argv[]) {

    //***************ALLEGRO SETUP REQUIREMENTS******************
    //initialize Allegro
    initializeAllegro();

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
	al_clear_to_color(BACKGROUND);
    printTitle(font);
    printDatabase(font, monarchs, number);

    //flips the buffer to the screen
    al_flip_display();

    //wait for 20 seconds.
    al_rest(20.0);

    // Free up memory taken by display.
    al_destroy_display(display);

    // Exit with no errors
	return 0;
}
