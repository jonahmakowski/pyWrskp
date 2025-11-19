#ifndef STRUCTS_CPP
#define STRUCTS_CPP

struct Vector2 {
    float x;
    float y;
};

struct Vector2i {
    int x;
    int y;
};

struct Object {
    ALLEGRO_BITMAP *image;
    Vector2 scale;
    Vector2i velocity;
    Vector2i position;
    bool exists;
};

struct Keybind {
    int keycodes[20];
};

struct Camera {
    Vector2i position;
    Vector2i velocity;
};

struct Panel {
    Vector2i top_left;
    Vector2i bottom_right;
    ALLEGRO_COLOR color;
    bool camera_correction;
};

#endif
