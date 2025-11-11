// to run:
// clang++ testing.cpp -o ./target/testing $(pkg-config allegro-5 allegro_main-5 allegro_font-5 allegro_primitives-5 allegro_image-5 --libs --cflags); ./target/testing

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

#include <stdio.h>

#include "helpers/structs.cpp"
#include "helpers/globals.cpp"
#include "helpers/function.cpp"
#include "helpers/rewritten_allegro_crap.cpp"
#include "helpers/colors.cpp"

ALLEGRO_BITMAP *sun_image = NULL;

void frame_logic() {
    fill_screen(WHITE);
    Vector2i center = {SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2};
    draw_image(sun_image, center);
}

void handle_input(ALLEGRO_EVENT ev) {
    printf("Key pressed!\n");
}

int main(int argc, char *argv[]) {
    printf("Running\n");
    
    if (!init_allegro()) {
        return -1;
    }

    long frames = 0;

    load_image_with_checks("images/sun.png", sun_image);

    al_start_timer(timer);
    while(true) {
        ALLEGRO_EVENT ev;

        al_wait_for_event(event_queue, &ev);

        if(ev.type == ALLEGRO_EVENT_TIMER) {
            frame_logic();
            update();
            frames += 1;
        }
        
        // Handling Input
        if (ev.type == ALLEGRO_EVENT_KEY_DOWN) {
            handle_input(ev);
        }
        
        if (frames > FPS * 5) {
            printf("Exiting after 5 seconds\n");
            break;
        }
    }

    al_destroy_display(display);
    return 0;
}
