#ifndef REWRITTEN_ALLEGRO_CRAP_CPP
#define REWRITTEN_ALLEGRO_CRAP_CPP

#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_font.h>

#include "globals.cpp"

// Renaming allegro functions to make it more sense to me

#define update() al_flip_display()
#define sleep(seconds) al_rest(seconds)
#define fill_screen(color) al_clear_to_color(color)
#define load_image(path) al_load_bitmap(path)
// Macro to load image with error checking, it checks that the image is actually there and loaded properly
#define load_image_with_checks(path, ptr) { \
    ALLEGRO_BITMAP *temp = load_image(path); \
    if (!temp) { \
        printf("Failed to load image: %s\n", path); \
        return 1; \
    } \
    ptr = temp; \
}
#define get_display_height() al_get_display_height(display)
#define get_display_width() al_get_display_width(display)

// Renaming drawing functions to use Vector2 and Vector2i and make more sense to me
void draw_rectangle(Vector2i top_left, Vector2i bottom_right, ALLEGRO_COLOR color) {
    al_draw_filled_rectangle(top_left.x, top_left.y, bottom_right.x, bottom_right.y, color);
}

void draw_rectangle_rounded(Vector2i top_left, Vector2i bottom_right, float radius, ALLEGRO_COLOR color) {
    al_draw_filled_rounded_rectangle(top_left.x, top_left.y, bottom_right.x, bottom_right.y, radius, radius, color);
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

// Made it so that this function draws the image centered at the position, instead of putting the top left corner there
void draw_image(ALLEGRO_BITMAP *image, Vector2i position) {
    int width = al_get_bitmap_width(image);
    int height = al_get_bitmap_height(image);
    Vector2i position_upper_left = {position.x - width / 2, position.y - height / 2};
    al_draw_bitmap(image, position_upper_left.x, position_upper_left.y, 0);
}

void draw_text(ALLEGRO_FONT *font, ALLEGRO_COLOR color, Vector2i position, const char *text) {
    al_draw_text(font, color, position.x, position.y, ALLEGRO_ALIGN_CENTRE, text);
}

Vector2i get_window_size() {
    Vector2i size;
    size.x = al_get_display_width(display);
    size.y = al_get_display_height(display);
    return size;
}

void draw_scaled_image(ALLEGRO_BITMAP *image, Vector2i position, Vector2 scale) {
    int width = al_get_bitmap_width(image) * scale.x;
    int height = al_get_bitmap_height(image) * scale.y;
    
    Vector2i position_upper_left;
    if (!FULLSCREEN) {
        position_upper_left = {position.x - width / 2, position.y - height / 2};
    } else {
        position_upper_left = {position.x - width / 2, position.y};
    }

    al_draw_scaled_bitmap(image, 0, 0, al_get_bitmap_width(image), al_get_bitmap_height(image), position_upper_left.x, position_upper_left.y, al_get_bitmap_width(image) * scale.x, al_get_bitmap_height(image) * scale.y, 0);
}

// Setup Allegro and its components
bool init_allegro() {
    if(!al_init() || !al_init_image_addon() || !al_init_primitives_addon()) {
        printf("failed to initalize libraries\n");
        return false;
    }

    if (FULLSCREEN) {
        al_set_new_display_flags(ALLEGRO_FULLSCREEN_WINDOW);
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