#ifndef KEYBINDS_CPP
#define KEYBINDS_CPP

#include <allegro5/allegro.h>
#include "structs.cpp"

// Defining keybinds

Keybind move_up = { { ALLEGRO_KEY_W, ALLEGRO_KEY_UP, -1 } };
Keybind move_down = { { ALLEGRO_KEY_S, ALLEGRO_KEY_DOWN, -1 } };
Keybind move_left = { { ALLEGRO_KEY_A, ALLEGRO_KEY_LEFT, -1 } };
Keybind move_right = { { ALLEGRO_KEY_D, ALLEGRO_KEY_RIGHT, -1 } };
Keybind kill_keybind = { { ALLEGRO_KEY_ESCAPE, -1 } };

#endif
