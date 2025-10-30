#include <allegro5/allegro.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    al_init();

    ALLEGRO_DISPLAY *display = al_create_display(1080, 720);

    if (!display) {
        printf("failed to create display\n");
        return -1;
    }
    
    ALLEGRO_COLOR white = al_map_rgb(255, 255, 255);

    al_set_window_title(display, "ALLEGRO Tutorial 1");
    al_clear_to_color(white);
    al_flip_display();
    al_rest(5.0);
    
    al_destroy_display(display);

    return 0;
}
