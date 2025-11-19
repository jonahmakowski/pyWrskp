#ifndef FUNCTIONS_CPP
#define FUNCTIONS_CPP

#include <allegro5/allegro.h>
#include <math.h>

#include "structs.cpp"
#include "rewritten_allegro_crap.cpp"

#define abs(num) (num < 0) ? -num : num
#define max(a, b) (a > b) ? a : b
#define min(a, b) (a < b) ? a : b

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

Vector2i camera_fixed_position(Vector2i position) {
    Vector2i camera_fixed_pos = {position.x + camera.position.x, position.y + camera.position.y};
    return camera_fixed_pos;
}

void draw(ALLEGRO_BITMAP *image, Vector2i position, Vector2 scale) {
    Vector2i fixed_pos = camera_fixed_position(position);
    draw_scaled_image(image, fixed_pos, scale);
}

void draw(Object obj) {
    draw(obj.image, obj.position, obj.scale);
}

void draw(Panel panel) {
    if (!panel.camera_correction) {
        draw_rectangle_rounded(panel.top_left, panel.bottom_right, PANEL_ROUNDING, panel.color);
    } else {
        Vector2i camera_fixed_top_left = {panel.top_left.x + camera.position.x, panel.top_left.y + camera.position.y};
        Vector2i camera_fixed_bottom_right = {panel.bottom_right.x + camera.position.x, panel.bottom_right.y + camera.position.y};
        draw_rectangle_rounded(camera_fixed_top_left, camera_fixed_bottom_right, PANEL_ROUNDING, panel.color);
    }
}

Vector2i get_camera_mouse_pos() {
    Vector2i cam_mouse_pos = {mouse_pos.x - camera.position.x, mouse_pos.y - camera.position.y};
    return cam_mouse_pos;
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

Vector2 get_object_size(Object obj) {
    Vector2 size;
    size.x = al_get_bitmap_width(obj.image) * obj.scale.x;
    size.y = al_get_bitmap_height(obj.image) * obj.scale.y;
    return size;
}

Vector2i vector2_to_vector2i(Vector2 vec) {
    Vector2i veci;
    veci.x = (int)vec.x;
    veci.y = (int)vec.y;
    return veci;
}

bool is_colliding(Object a, Object b) {
    Vector2i a_size = vector2_to_vector2i(get_object_size(a));
    Vector2i b_size = vector2_to_vector2i(get_object_size(b));
    
    Vector2i a_position_upper_left = {a.position.x - a_size.x / 2, a.position.y - a_size.y / 2};
    Vector2i b_position_upper_left = {b.position.x - b_size.x / 2, b.position.y - b_size.y / 2};

    return (a_position_upper_left.x < b_position_upper_left.x + b_size.x &&
            a_position_upper_left.x + a_size.x > b_position_upper_left.x &&
            a_position_upper_left.y < b_position_upper_left.y + b_size.y &&
            a_position_upper_left.y + a_size.y > b_position_upper_left.y);
}

bool is_within(Object obj, Vector2i point) {
    Vector2i size = vector2_to_vector2i(get_object_size(obj));

    Vector2i obj_position_upper_left = camera_fixed_position({obj.position.x - size.x / 2, obj.position.y - size.y / 2});

    return (point.x >= obj_position_upper_left.x && point.x <= obj_position_upper_left.x + size.x &&
            point.y >= obj_position_upper_left.y && point.y <= obj_position_upper_left.y + size.y);
}

bool is_within(Panel panel, Vector2i point) {
    if (!panel.camera_correction) {
        return (point.x >= panel.top_left.x && point.x <= panel.bottom_right.x &&
                point.y >= panel.top_left.y && point.y <= panel.bottom_right.y);
    } else {
        Vector2i camera_fixed_top_left = camera_fixed_position(panel.top_left);
        Vector2i camera_fixed_bottom_right = camera_fixed_position(panel.bottom_right);
        return (point.x >= camera_fixed_top_left.x && point.x <= camera_fixed_bottom_right.x &&
                point.y >= camera_fixed_top_left.y && point.y <= camera_fixed_bottom_right.y);
    }
}

bool currently_clicking(Panel panel) {
    return is_within(panel, get_camera_mouse_pos());
}

bool currently_clicking(Object obj) {
    return is_within(obj, get_camera_mouse_pos());
}

#endif