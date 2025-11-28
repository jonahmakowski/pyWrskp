#ifndef STRUCTS_CPP
#define STRUCTS_CPP

#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>

#include "colors.cpp"

// Vector with x,y positions as floats
struct Vector2 {
    float x;
    float y;
};

// Vector with x,y positions as integers
struct Vector2i {
    int x;
    int y;
};

// Object struct representing a game object
struct Object {
    ALLEGRO_BITMAP *image;
    Vector2 scale;
    Vector2i velocity;
    Vector2i position;
    bool exists;
};

// Keybind struct representing a set of keycodes
struct Keybind {
    int keycodes[20];
};

// Camera struct representing the camera's position, velocity, and zoom level
struct Camera {
    Vector2i position;
    Vector2i velocity;
    float zoom;
};

// Font struct representing a font and its size
struct Font {
    ALLEGRO_FONT *font;
    int size;
};

// Panel struct representing a UI panel
struct Panel {
    Vector2i top_left;
    Vector2i bottom_right;
    ALLEGRO_COLOR color;

    char text[250];
    ALLEGRO_COLOR text_color = BLACK;
    Font font;

    struct Panel* children[20];
    int child_count = 0;
};

// Tower struct representing a tower in the game
struct Tower {
    Object object;
    int level;
    float fire_rate;
    float range;
    int damage;
    float time_since_last_shot;
};

// Enemy struct representing an enemy in the game
struct Enemy {
    Object object;
    int health;
    int max_health;
    float speed;
    int reward;
    bool is_boss;
};

#endif
