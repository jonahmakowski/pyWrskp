// to run:
// gcc testing.cpp -o ./target/testing $(pkg-config allegro-5 allegro_main-5 allegro_font-5 allegro_primitives-5 allegro_image-5 --libs --cflags); ./target/testing

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

#include <stdio.h>

#include "helpers/structs.cpp"
#include "helpers/globals.cpp"
#include "helpers/function.cpp"
#include "helpers/rewritten_allegro_crap.cpp"
#include "helpers/colors.cpp"

void frame_logic() {
    // Frame logic goes here
}

int main(int argc, char *argv[]) {
    printf("Running\n");
    
    if (!init_allegro()) {
        return -1;
    }

    al_start_timer(timer);
    while(true) {
        ALLEGRO_EVENT ev;

        al_wait_for_event(event_queue, &ev);

        if(ev.type == ALLEGRO_EVENT_TIMER) {
            frame_logic();
            update();
        }
    }

    al_destroy_display(display);
    return 0;
}
