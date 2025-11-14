#ifndef FUNCTIONS_CPP
#define FUNCTIONS_CPP

#include <allegro5/allegro.h>
#include <math.h>

#include "structs.cpp"
#include "rewritten_allegro_crap.cpp"

bool pressing_keybind(Keybind keybind, ALLEGRO_EVENT ev) {
    for (int i = 0; i < 20; i++) {
        if (keybind.keycodes[i] == -1) {
            break;
        } else if (keybind.keycodes[i] == ev.keyboard.keycode) {
            return true;
        }
    }
    return false;
}

void draw(ALLEGRO_BITMAP *image, Vector2i position, Vector2 scale) {
    Vector2i camera_fixed_position = {position.x + camera.position.x, position.y + camera.position.y};
    draw_scaled_image(image, camera_fixed_position, scale);
}

Vector2i get_camera_mouse_pos() {
    Vector2i cam_mouse_pos = {mouse_pos.x - camera.position.x, mouse_pos.y - camera.position.y};
    return cam_mouse_pos;
}

void draw_object(Object obj) {
    draw(obj.image, obj.position, obj.scale);
}

void update_position(Object &obj) {
    obj.position.x += obj.velocity.x;
    obj.position.y += obj.velocity.y;
}

Vector2 normalize(Vector2 vec) {
    float max = fmax(fabs(vec.x), fabs(vec.y));
    Vector2 normalized = {vec.x / max, vec.y / max};
    return normalized;
}

Vector2 get_direction_to(Vector2i from, Vector2i to) {
    Vector2 direction;
    direction.x = to.x - from.x;
    direction.y = to.y - from.y;
    return normalize(direction);
}

void update_camera_position() {
    camera.position.x -= camera.velocity.x;
    camera.position.y -= camera.velocity.y;
}

float distance_between(Vector2i a, Vector2i b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}

bool is_colliding(Object a, Object b) {
    int a_width = al_get_bitmap_width(a.image) * a.scale.x;
    int a_height = al_get_bitmap_height(a.image) * a.scale.y;
    int b_width = al_get_bitmap_width(b.image) * b.scale.x;
    int b_height = al_get_bitmap_height(b.image) * b.scale.y;

    bool x_overlap = (a.position.x < b.position.x + b_width) && (a.position.x + a_width > b.position.x);
    bool y_overlap = (a.position.y < b.position.y + b_height) && (a.position.y + a_height > b.position.y);

    return x_overlap && y_overlap;
}

bool is_within(Object obj, Vector2i point) {
    int obj_width = al_get_bitmap_width(obj.image) * obj.scale.x;
    int obj_height = al_get_bitmap_height(obj.image) * obj.scale.y;

    return (point.x >= obj.position.x && point.x <= obj.position.x + obj_width &&
            point.y >= obj.position.y && point.y <= obj.position.y + obj_height);
}

#endif