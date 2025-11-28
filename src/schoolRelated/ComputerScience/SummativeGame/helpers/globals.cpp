#ifndef GLOBALS_CPP
#define GLOBALS_CPP

#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>

#include "structs.cpp"

#define MAX_WIDTH 800
#define MAX_HEIGHT 800
#define FPS 30

#define SCREEN_WIDTH 2160
#define SCREEN_HEIGHT 1440
#define FULLSCREEN false

#define PANEL_ROUNDING 10.0f

// Defining global variables

ALLEGRO_DISPLAY *display = nullptr;
ALLEGRO_EVENT_QUEUE *event_queue = nullptr;
ALLEGRO_TIMER *timer = nullptr;

Font default_font;
Vector2i mouse_pos = {0, 0};
Camera camera = {{0, 0}, {0, 0}, 1.0f};

#endif
