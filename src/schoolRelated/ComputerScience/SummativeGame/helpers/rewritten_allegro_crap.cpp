#ifndef REWRITTEN_ALLEGRO_CRAP_CPP
#define REWRITTEN_ALLEGRO_CRAP_CPP

#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_font.h>

#include "globals.cpp"

#define update() al_flip_display()
#define sleep(seconds) al_rest(seconds)
#define fill_screen(color) al_clear_to_color(color)

bool init_allegro() {
    if(!al_init() || !al_init_image_addon() || !al_init_primitives_addon()) {
        printf("failed to initalize libraries\n");
        return false;
    }

    // Exit program if program fails to create display
    display = al_create_display(SCREEN_WIDTH, SCREEN_HEIGHT);
    if(!display) {
        printf("Display failed\n");
        return false;
    }

    timer = al_create_timer(1.0 / FPS);
   	if (!timer) {
   		printf("timer failed\n");
        return false;
   	}

   	event_queue = al_create_event_queue();
   	if (!event_queue) {
   		printf("queue failed\n");
        return false;
   	}

    al_register_event_source(event_queue, al_get_timer_event_source(timer));

    al_set_window_title(display, "Summative Game");

    return true;
}

#endif