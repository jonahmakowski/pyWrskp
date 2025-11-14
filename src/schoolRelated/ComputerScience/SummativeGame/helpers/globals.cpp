#ifndef GLOBALS_CPP
#define GLOBALS_CPP

#include <allegro5/allegro.h>
#include <allegro5/allegro_font.h>
#include "structs.cpp"

#define MAX_WIDTH 800
#define MAX_HEIGHT 800
#define FPS 30

#define SCREEN_WIDTH 2160
#define SCREEN_HEIGHT 1440
#define FULLSCREEN true

Object objects[MAX_WIDTH * MAX_HEIGHT] = {};
int object_count = 0;

void add_object(Object obj) {
    if (object_count < MAX_WIDTH * MAX_HEIGHT) {
        objects[object_count] = obj;
        object_count++;
    }
}

ALLEGRO_DISPLAY *display = nullptr;
ALLEGRO_EVENT_QUEUE *event_queue = nullptr;
ALLEGRO_TIMER *timer = nullptr;

ALLEGRO_FONT *default_font = nullptr;
Vector2i mouse_pos = {0, 0};
Camera camera = {{0, 0}, {0, 0}};

#endif
