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
#define load_image(path) al_load_bitmap(path)
#define load_image_with_checks(path, ptr) { \
    ALLEGRO_BITMAP *temp = load_image(path); \
    if (!temp) { \
        printf("Failed to load image: %s\n", path); \
        return 1; \
    } \
    ptr = temp; \
}

void draw_rectangle(Vector2i top_left, Vector2i bottom_right, ALLEGRO_COLOR color) {
    al_draw_filled_rectangle(top_left.x, top_left.y, bottom_right.x, bottom_right.y, color);
}

void draw_circle(Vector2i center, float radius, ALLEGRO_COLOR color) {
    al_draw_filled_circle(center.x, center.y, radius, color);
}

void draw_triangle(Vector2i point1, Vector2i point2, Vector2i point3, ALLEGRO_COLOR color) {
    al_draw_filled_triangle(point1.x, point1.y, point2.x, point2.y, point3.x, point3.y, color);
}

void draw_line(Vector2i start, Vector2i end, ALLEGRO_COLOR color, float thickness) {
    al_draw_line(start.x, start.y, end.x, end.y, color, thickness);
}

void draw_image(ALLEGRO_BITMAP *image, Vector2i position_upper_left) {
    al_draw_bitmap(image, position_upper_left.x, position_upper_left.y, 0);
}

void draw_scaled_image(ALLEGRO_BITMAP *image, Vector2i position_upper_left, float scale_x, float scale_y) {
    al_draw_scaled_bitmap(image, 0, 0, al_get_bitmap_width(image), al_get_bitmap_height(image), position_upper_left.x, position_upper_left.y, al_get_bitmap_width(image) * scale_x, al_get_bitmap_height(image) * scale_y, 0);
}

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

    // Init keyboard
   	if (!al_install_keyboard()) {
        printf("keyboard failed\n");
        return false;
    }

    // Init mouse
    if (!al_install_mouse()) {
        printf("mouse failed\n");
        return false;
    }

    al_register_event_source(event_queue, al_get_timer_event_source(timer));
    al_register_event_source(event_queue, al_get_keyboard_event_source());
    al_register_event_source(event_queue, al_get_mouse_event_source());

    al_set_window_title(display, "Summative Game");

    default_font = al_create_builtin_font();

    return true;
}

#endif