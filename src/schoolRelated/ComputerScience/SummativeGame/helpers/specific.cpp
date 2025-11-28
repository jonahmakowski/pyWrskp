#ifndef SPECIFIC_CPP
#define SPECIFIC_CPP

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

#include "colors.cpp"
#include "functions.cpp"
#include "globals.cpp"
#include "keybinds.cpp"
#include "rewritten_allegro_crap.cpp"
#include "structs.cpp"

// Macro to check for exit keybind
#define check_for_exit(ev) { \
    if (ev.type == ALLEGRO_EVENT_KEY_DOWN && pressing_keybind(kill_keybind, ev)) { \
        printf("Exiting due to kill keybind\n"); \
        al_destroy_display(display); \
        return 0; \
    } \
}

#endif
